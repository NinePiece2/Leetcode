import os
import re
import requests
from pathlib import Path

SRC_DIR = "Solutions"
SITE_README_PATH = Path("Site_README.md")
GITHUB_README_PATH = Path("README.md")

LINK_ICON = "🔗"  # Unicode link icon

def fetch_problem_data(slug: str):
    """Fetch problem number, difficulty, and tags from LeetCode GraphQL API."""
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
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": f"https://leetcode.com/problems/{slug}/"
    }
    try:
        resp = requests.post(url, json=query, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()["data"]["question"]
        number = data.get("frontendQuestionId", "")
        difficulty = data.get("difficulty", "")
        tags = [t["name"] for t in data.get("topicTags", [])]
        return number, difficulty, tags
    except Exception as e:
        print(f"Failed to fetch {slug}: {e}")
        return "", "", []

# MkDocs HTML badge
def difficulty_badge_site(difficulty: str) -> str:
    colors = {"Easy": "#46c6c2", "Medium": "#fac31d", "Hard": "#f8615c"}
    if not difficulty:
        return ""
    color = colors.get(difficulty, "#9E9E9E")
    return f'<span style="background-color:#ffffff1a; color:{color}; padding:2px 6px; border-radius:6px;">{difficulty}</span>'

# GitHub Shields.io badge
def difficulty_badge_github(difficulty: str) -> str:
    colors = {"Easy": "4c1", "Medium": "f9c851", "Hard": "e05d44"}
    if not difficulty:
        return ""
    color = colors.get(difficulty, "9e9e9e")
    badge_url = f"https://img.shields.io/badge/Difficulty-{difficulty}-{color}.svg"
    return f"![{difficulty}]({badge_url})"

def generate_table_rows(problems, badge_func):
    rows = []
    for slug, number, title, difficulty, tags in problems:
        diff_badge = badge_func(difficulty)
        tags_str = ", ".join(tags)
        solution_link = f"https://leetcode.romitsagu.com/solutions/leetcode{number}#/"
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
    problems = []

    # Step 1: Read all problem folders and fetch data
    for folder in sorted(os.listdir(SRC_DIR)):
        folder_path = Path(SRC_DIR) / folder
        if not folder_path.is_dir():
            continue

        match = re.match(r"(\d+)-(.+)", folder)
        if not match:
            continue
        folder_number, slug = match.groups()
        folder_number = str(int(folder_number))
        title = f"{folder_number}. " + " ".join([w.capitalize() for w in slug.split("-")])

        # Fetch API data once
        number, difficulty, tags = fetch_problem_data(slug)
        problems.append((slug, number, title, difficulty, tags))

    # Step 2: Generate table rows
    site_rows = generate_table_rows(problems, difficulty_badge_site)
    github_rows = generate_table_rows(problems, difficulty_badge_github)

    # Step 3: Update both READMEs
    update_readme(SITE_README_PATH, site_rows)
    update_readme(GITHUB_README_PATH, github_rows)

if __name__ == "__main__":
    main()
