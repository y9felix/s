import requests
import base64
import matplotlib.pyplot as plt
from collections import defaultdict, Counter

# Configuration
REPO_OWNER = "y9felix"
REPO_NAME = "s"
FILE_PATH = "c"
GITHUB_TOKEN = "hoobabooba"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

REGIONAL_INDICATORS = {c: chr(ord(c) - 127397) for c in [chr(i) for i in range(127462, 127488)]}

def get_commits():
    commits = []
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits?path={FILE_PATH}"
    while url:
        response = requests.get(url, headers=HEADERS)
        commits.extend(response.json())
        url = response.links.get('next', {}).get('url')
    return commits[::-1]

def get_file_content(commit_sha):
    content_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}?ref={commit_sha}"
    content_data = requests.get(content_url, headers=HEADERS).json()
    return base64.b64decode(content_data['content']).decode('utf-8').splitlines()

def main():
    commits = get_commits()
    line_persistence = defaultdict(list)
    country_counts = Counter()
    commit_data = []
    
    # First pass: collect all data
    for idx, commit in enumerate(commits):
        lines = get_file_content(commit['sha'])
        current_flags = Counter()
        
        for line in lines:
            clean_line = line.split('#')[0].strip()
            if clean_line:
                line_persistence[clean_line].append(idx)
            if len(line) >= 2:
                flag_code = ''.join(REGIONAL_INDICATORS.get(c, '') for c in line[-2:])
                if len(flag_code) == 2:
                    current_flags[flag_code] += 1
                    country_counts[flag_code] += 1
        
        total = sum(current_flags.values())
        commit_data.append({k: v/total*100 for k, v in current_flags.items()} if total else {})

    # Identify top countries
    top_countries = [c for c, _ in country_counts.most_common(7)]
    
    # Remove duplicate commits where top 7 countries didn't change
    unique_commits = []
    prev_top7 = None
    
    for idx, data in enumerate(commit_data):
        # Get percentages for top 7 countries in this commit
        current_top7 = tuple(round(data.get(country, 0), 2) for country in top_countries)
        
        # Only keep commit if top 7 distribution changed
        if current_top7 != prev_top7:
            unique_commits.append(idx)
            prev_top7 = current_top7

    # Filter commit data to only include unique commits
    filtered_commit_data = [commit_data[i] for i in unique_commits]
    
    # Plotting
    plt.figure(figsize=(12, 6))
    for country in top_countries:
        percentages = [d.get(country, 0) for d in filtered_commit_data]
        plt.plot(percentages, marker='o', label=country)
    
    plt.legend()
    plt.xticks(range(len(filtered_commit_data)), [f"Commit {i+1}" for i in range(len(filtered_commit_data))], rotation=45)
    plt.tight_layout()
    plt.savefig('flag_history.png', dpi=300)

    # Generate report
    with open('yo.txt', 'w') as f:
        f.write(f"Total commits analyzed: {len(commits)}\n")
        f.write(f"Unique commits after deduplication: {len(unique_commits)}\n")
        f.write(f"Total flags found: {sum(country_counts.values())}\n")
        f.write(f"Unique countries: {len(country_counts)}\n\n")
        
        for country, count in country_counts.most_common():
            f.write(f"{country}: {count} flags ({(count/sum(country_counts.values())*100):.2f}%)\n")
        
        f.write("\n\nLINES WITH MOST RECOMMITS:\n")
        for line, commits in sorted(line_persistence.items(), key=lambda x: len(x[1]), reverse=True):
            f.write(f"{line}#{len(commits)}\n")

if __name__ == "__main__":
    main()