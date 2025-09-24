import os
import re
from pathlib import Path
import requests

SRC_DIR = "Solutions"
README_PATH = Path("README.md")

# URL to a small logo to use for the solution link
SOLUTION_LOGO_URL = "https://img.icons8.com/ios-filled/24/link.png"  # Example link icon

def fetch_difficulty_and_tags(slug: str):
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

def generate_table_rows_html():
    rows = []
    for idx, folder in enumerate(sorted(os.listdir(SRC_DIR))):
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
        solution_link = f"https://leetcode.romitsagu.com/solutions/{number}"

        # Alternate row colors
        row_bg = "#f9f9f9" if idx % 2 == 0 else "#ffffff"

        rows.append(
            f"<tr style='background-color:{row_bg};'>"
            f"<td>{title}</td>"
            f"<td><a href='{solution_link}'><img src='{SOLUTION_LOGO_URL}' alt='link' width='20' /></a></td>"
            f"<td>{diff_badge}</td>"
            f"<td>{tags_str}</td>"
            f"</tr>"
        )
    return "\n".join(rows)

def update_readme_table_html():
    if not README_PATH.exists():
        raise FileNotFoundError(f"{README_PATH} does not exist")

    readme_text = README_PATH.read_text()

    pattern = re.compile(
        r'(<details open>\s*<summary>My Solutions</summary>\s*\n)(.*?)(\n</details>)',
        re.DOTALL
    )

    table_rows = generate_table_rows_html()
    new_table_html = (
        "<details open>\n"
        "  <summary>My Solutions</summary>\n\n"
        "  <table>\n"
        "    <thead>\n"
        "      <tr><th>Problem</th><th>Solution</th><th>Difficulty</th><th>Tags</th></tr>\n"
        "    </thead>\n"
        "    <tbody>\n"
        f"{table_rows}\n"
        "    </tbody>\n"
        "  </table>\n"
        "</details>"
    )

    if pattern.search(readme_text):
        updated_text = pattern.sub(new_table_html, readme_text)
        print("Updated solutions HTML table.")
    else:
        updated_text = readme_text.strip() + "\n\n" + new_table_html
        print("Added new solutions HTML table.")

    README_PATH.write_text(updated_text)
    print("README.md updated successfully.")

if __name__ == "__main__":
    update_readme_table_html()
