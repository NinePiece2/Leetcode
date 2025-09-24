import os
import re
from pathlib import Path
import requests

SRC_DIR = "Solutions"
SITE_README_PATH = Path("Site_README.md")
GITHUB_README_PATH = Path("README.md")

LINK_ICON = "🔗"  # Unicode link icon

def fetch_problem_data(slug: str):
    """Fetch difficulty, tags, and real problem number from LeetCode GraphQL API."""
    url = "https://leetcode.com/graphql"
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            frontendQuestionId
            difficulty
            topicTags { name }
          }
        }
        """,
        "variables": {"titleSlug": slug},
    }
    try:
        resp = requests.post(url, json=query, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        question = data.get("data", {}).get("question", {})
        number = question.get("frontendQuestionId", "")
        difficulty = question.get("difficulty", "")
        tags = [t['name'] for t in question.get("topicTags", [])]
        return number, difficulty, tags
    except Exception as e:
        print(f"Failed to fetch {slug}: {e}")
        return "", "", []

# MkDocs badge (HTML)
def difficulty_badge_site(difficulty: str) -> str:
    colors = {"Easy": "#46c6c2", "Medium": "#fac31d", "Hard": "#f8615c"}
    color = colors.get(difficulty, "#9E9E9E")
    if not difficulty:
        return ""
    return f'<span style="background-color:#ffffff1a; color:{color}; padding:2px 6px; border-radius:6px;">{difficulty}</span>'

# GitHub badge (Shields.io)
def difficulty_badge_github(difficulty: str) -> str:
    colors = {"Easy": "4c1", "Medium": "f9c851", "Hard": "e05d44"}
    if not difficulty:
        return ""
    color = colors.get(difficulty, "9e9e9e")
    badge_url = f"https://img.shields.io/badge/Difficulty-{difficulty}-{color}.svg"
    return f"![{difficulty}]({badge_url})"

def generate_table_rows(cached_data, badge_func):
    rows = []
    for slug, real_number, title_slug in cached_data:
        difficulty, tags = cached_data[(slug, real_number)]
        title = f"{real_number}. " + ' '.join([w.capitalize() for w in title_slug.split('-')])
        diff_badge = badge_func(difficulty)
        tags_str = ', '.join(tags)
        solution_link = f"https://leetcode.romitsagu.com/solutions/leetcode{real_number}#/"
        icon_md = f"[{LINK_ICON}]({solution_link})"

        rows.append(f"| {title} | {icon_md} | {diff_badge} | {tags_str} |")
    return "\n".join(rows)

def update_readme(readme_path, rows_str):
    if not readme_path.exists():
        raise FileNotFoundError(f"{readme_path} does not exist")

    readme_text = readme_path.read_text()
    pattern = re.compile(
        r'(\| Problem \| Solution \| Difficulty \| Tags \|\n\|[-| ]+\|\n)(.*?)(\n|$)',
        re.DOTALL
    )

    if pattern.search(readme_text):
        updated_text = pattern.sub(r"\1" + rows_str + r"\3", readme_text)
        print(f"Updated table rows in {readme_path.name}")
    else:
        new_table = (
            "| Problem | Solution | Difficulty | Tags |\n"
            "|---------|---------|------------|------|\n"
            + rows_str
        )
        updated_text = readme_text.strip() + "\n\n" + new_table
        print(f"Added new table in {readme_path.name}")

    readme_path.write_text(updated_text)
    print(f"{readme_path.name} updated successfully.")

def main():
    cached_data = []
    api_cache = {}

    # Fetch real number, difficulty, and tags for each problem
    for folder in sorted(os.listdir(SRC_DIR)):
        folder_path = Path(SRC_DIR) / folder
        if not folder_path.is_dir():
            continue
        match = re.match(r"(\d+)-(.+)", folder)
        if not match:
            continue
        _, slug = match.groups()

        if slug not in api_cache:
            real_number, difficulty, tags = fetch_problem_data(slug)
            api_cache[slug] = (difficulty, tags)
        else:
            real_number, _, _ = fetch_problem_data(slug)

        cached_data.append((slug, real_number, slug))

    # Generate rows for both READMEs
    site_rows = generate_table_rows(api_cache, difficulty_badge_site)
    github_rows = generate_table_rows(api_cache, difficulty_badge_github)

    # Update both READMEs
    update_readme(SITE_README_PATH, site_rows)
    update_readme(GITHUB_README_PATH, github_rows)

if __name__ == "__main__":
    main()
