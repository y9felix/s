import requests
import base64

# Configuration
GITHUB_TOKEN = "YOUR_TOKEN"
REPO_OWNER = "y9felix"
REPO_NAME = "s"
FILES = ["a", "b"]
OUTPUT_FILE = "all.txt"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_file_commits(file_path):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"
    params = {"path": file_path, "per_page": 100}
    response = requests.get(url, headers=headers, params=params)
    return response.json() if response.status_code == 200 else []

def get_file_content(commit_sha, file_path):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_path}"
    params = {"ref": commit_sha}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        content = response.json()["content"]
        return base64.b64decode(content).decode('utf-8')
    return ""

def has_country_flag(line):
    # Country flags are in the Unicode range U+1F1E6 to U+1F1FF
    return any(0x1F1E6 <= ord(char) <= 0x1F1FF for char in line)

unique_lines = set()

for file in FILES:
    print(f"Processing file: {file}")
    commits = get_file_commits(file)
    
    for commit in commits:
        sha = commit["sha"]
        content = get_file_content(sha, file)
        
        if content:
            for line in content.splitlines():
                if has_country_flag(line):
                    unique_lines.add(line.strip())

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for line in sorted(unique_lines):
        f.write(line + "\n")

print(f"Done! Found {len(unique_lines)} unique lines with country flags. Saved to {OUTPUT_FILE}")