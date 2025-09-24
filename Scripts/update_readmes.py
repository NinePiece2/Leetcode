import os
import re
from pathlib import Path
import shutil
import yaml
import subprocess
import requests

SRC_DIR = "Solutions"
DST_DIR = "docs/solutions"

# Clean previous docs
if Path(DST_DIR).exists():
    shutil.rmtree(DST_DIR)
os.makedirs(DST_DIR, exist_ok=True)

nav_entries = []

def fetch_difficulty_from_leetcode(slug: str) -> str:
    """Fetch difficulty from LeetCode GraphQL API using problem slug."""
    url = "https://leetcode.com/graphql"
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            difficulty
          }
        }
        """,
        "variables": {"titleSlug": slug},
    }
    try:
        resp = requests.post(url, json=query, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        question = data.get("data", {}).get("question")
        if not question:
            print(f"⚠️ No question data returned for slug: {slug}")
            return ""
        return question.get("difficulty", "")
    except Exception as e:
        print(f"❌ Failed to fetch difficulty for {slug}: {e}")
        return ""

def difficulty_badge(difficulty: str) -> str:
    """Return a colored HTML badge for difficulty."""
    colors = {
        "Easy": "#4CAF50",      # green
        "Medium": "#FFC107",    # amber
        "Hard": "#F44336",      # red
    }
    color = colors.get(difficulty, "#9E9E9E")  # default gray
    if not difficulty:
        return ""
    return f'<span style="background-color:{color}; color:white; padding:2px 8px; border-radius:6px; font-size:0.85em;">{difficulty}</span>'

for prob_folder in sorted(os.listdir(SRC_DIR)):
    prob_path = Path(SRC_DIR) / prob_folder
    if not prob_path.is_dir():
        continue

    match = re.match(r'(\d+)-(.+)', prob_folder)
    if not match:
        continue
    number, title_slug = match.groups()
    number = str(int(number))  # remove leading zeros
    title = ' '.join([w.capitalize() for w in title_slug.split('-')])

    readme_path = prob_path / "README.md"
    readme_content = ""
    if readme_path.exists():
        with open(readme_path, "r") as f:
            readme_content = f.read().strip()

    # Always fetch difficulty from LeetCode
    difficulty = fetch_difficulty_from_leetcode(title_slug)
    badge_html = difficulty_badge(difficulty)

    # Prepare a single tabbed solution block with commit submission data
    tab_lines = []

    for sol_file in sorted(prob_path.iterdir()):
        if sol_file.suffix in [".py", ".js", ".cs", ".sql"]:
            with open(sol_file, "r") as f:
                code = f.read().rstrip()

            # Get commit info for the file
            try:
                result = subprocess.run(
                    ["git", "log", "--diff-filter=A", "--pretty=format:%s", "--", str(sol_file)],
                    capture_output=True,
                    text=True,
                    check=True
                )
                submission_info = result.stdout.strip()
            except subprocess.CalledProcessError:
                submission_info = ""

            # Parse submission info (from "[LeetCode Sync] Runtime - ..., Memory - ...")
            stats_block = ""
            if submission_info.startswith("[LeetCode Sync]"):
                stats_match = re.search(
                    r'Runtime\s*-\s*(.*?)\s*\((.*?)\),\s*Memory\s*-\s*(.*?)\s*\((.*?)\)',
                    submission_info
                )
                if stats_match:
                    runtime, runtime_pct, memory, memory_pct = stats_match.groups()
                    stats_block = (
                        "\n\t**Submission Stats:**\n\n"
                        f"\t- Runtime: {runtime} ({runtime_pct})\n"
                        f"\t- Memory: {memory} ({memory_pct})"
                    )

            lang_map = {"js": "JS", "py": "Python3", "cs": "C#", "sql": "SQL"}
            lang_display = lang_map.get(sol_file.suffix.lstrip("."), sol_file.suffix.lstrip(".").capitalize())
            lang_block = sol_file.suffix.lstrip(".")

            # indent code for tab rendering
            indented_code = '\n'.join(['\t' + line if line else '' for line in code.splitlines()])

            tab_content = (
                f'=== "{lang_display}"\n\n'
                f'\t```{lang_block}\n{indented_code}\n\t```\n'
            )
            if stats_block:
                tab_content += f"\n{stats_block}\n"

            tab_lines.append(tab_content)

    # Build sections in correct order
    problem_section = f"## Problem - {title} {badge_html}\n\n"

    solutions_section = "## Solutions\n\n" + "\n".join(tab_lines)

    # Order: Problem first, then README, then Solutions
    full_md = problem_section
    if readme_content:
        full_md += readme_content + "\n\n"
    full_md += solutions_section

    md_filename = f"{number}.md"
    with open(Path(DST_DIR) / md_filename, "w") as f:
        f.write(full_md)

    nav_entries.append({f"{number}. {title}": f"solutions/{md_filename}"})

# Update mkdocs.yml nav
mkdocs_yml_path = Path("mkdocs.yml")
with open(mkdocs_yml_path, "r") as f:
    mkdocs_config = yaml.safe_load(f)

mkdocs_config['nav'] = [{"Overview": "README.md"}, {"Solutions": nav_entries}]

with open(mkdocs_yml_path, "w") as f:
    yaml.dump(mkdocs_config, f, sort_keys=False)
