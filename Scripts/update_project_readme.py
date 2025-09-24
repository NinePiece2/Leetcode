import os
import re
from pathlib import Path
import requests

SRC_DIR = "Solutions"
README_PATH = Path("README.md")

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
        "Easy": "#4CAF50",
        "Medium": "#FFC107",
        "Hard": "#F44336",
    }
    color = colors.get(difficulty, "#9E9E9E")
    if not difficulty:
        return ""
    return f'<span style="background-color:#ffffff1a; color:{color}; padding:2px 6px; border-radius:6px;">{difficulty}</span>'

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
        solution_link = f"./{SRC_DIR}/{folder}/README.md"

        rows.append(f"| {title} | [Link]({solution_link}) | {diff_badge} | {tags_str} |")
    return "\n    ".join(rows)  # indent for Markdown inside <details>

def update_readme_table():
    if not README_PATH.exists():
        raise FileNotFoundError(f"{README_PATH} does not exist")

    readme_text = README_PATH.read_text()

    # Match the <details> block
    pattern = re.compile(
        r'(<details open>\s*<summary>My Solutions</summary>\s*\n\n\s*\| Problem \| Solution \| Difficulty \| Tags \|.*?\n\s*\|[-| ]+\|\n)(.*?)(\n</details>)',
        re.DOTALL
    )

    new_rows = generate_table_rows()
    if pattern.search(readme_text):
        updated_text = pattern.sub(r"\1    " + new_rows + r"\3", readme_text)
        print("Updated solutions table rows.")
    else:
        # If block does not exist, add it at the end
        new_block = (
            "<details open>\n"
            "    <summary>My Solutions</summary>\n\n"
            "    | Problem | Solution | Difficulty | Tags |\n"
            "    |---------|----------|------------|------|\n"
            "    " + new_rows + "\n</details>"
        )
        updated_text = readme_text.strip() + "\n\n" + new_block
        print("Added new solutions table.")

    README_PATH.write_text(updated_text)
    print("README.md updated successfully.")

if __name__ == "__main__":
    update_readme_table()
