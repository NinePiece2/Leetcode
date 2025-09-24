import os
import re
from pathlib import Path
import requests

SRC_DIR = "Solutions"
README_PATH = Path("README.md")

LINK_ICON = "🔗"  # Unicode link icon

def fetch_difficulty_and_tags(slug: str):
    """Fetch difficulty and tags from LeetCode GraphQL API."""
    url = "https://leetcode.com/graphql"
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
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
        difficulty = question.get("difficulty", "")
        tags = [t['name'] for t in question.get("topicTags", [])]
        return difficulty, tags
    except Exception as e:
        print(f"Failed to fetch {slug}: {e}")
        return "", []

def difficulty_badge(difficulty: str) -> str:
    colors = {
        "Easy": "#46c6c2",      # green
        "Medium": "#fac31d",    # amber
        "Hard": "#f8615c",      # red
    }
    color = colors.get(difficulty, "#9E9E9E")
    if not difficulty:
        return ""
    return f'<span style="background-color:{color}; color:white; padding:2px 6px; border-radius:6px;">{difficulty}</span>'

def generate_table_rows():
    rows = []
    for folder in sorted(os.listdir(SRC_DIR)):
        folder_path = Path(SRC_DIR) / folder
        if not folder_path.is_dir():
            continue
        match = re.match(r"(\d+)-(.+)", folder)
        if not match:
            continue
        number, slug = match.groups()
        number = str(int(number))
        title = ' '.join([w.capitalize() for w in slug.split('-')])

        difficulty, tags = fetch_difficulty_and_tags(slug)
        diff_badge = difficulty_badge(difficulty)
        tags_str = ', '.join(tags)
        # Use Unicode link icon
        solution_link = f"https://leetcode.romitsagu.com/solutions/{slug}/"
        icon_md = f"[{LINK_ICON}]({solution_link})"

        rows.append(f"| {title} | {icon_md} | {diff_badge} | {tags_str} |")
    return "\n".join(rows)

def update_readme_table():
    if not README_PATH.exists():
        raise FileNotFoundError(f"{README_PATH} does not exist")

    readme_text = README_PATH.read_text()

    # Match the table block (without details)
    pattern = re.compile(
        r'(\| Problem \| Solution \| Difficulty \| Tags \|\n\|[-| ]+\|\n)(.*?)(\n|$)',
        re.DOTALL
    )

    new_rows = generate_table_rows()
    if pattern.search(readme_text):
        updated_text = pattern.sub(r"\1" + new_rows + r"\3", readme_text)
        print("Updated solutions table rows.")
    else:
        # Add table at the end if not found
        new_table = (
            "| Problem | Solution | Difficulty | Tags |\n"
            "|---------|---------|------------|------|\n"
            + new_rows
        )
        updated_text = readme_text.strip() + "\n\n" + new_table
        print("Added new solutions table.")

    README_PATH.write_text(updated_text)
    print("README.md updated successfully.")

if __name__ == "__main__":
    update_readme_table()
