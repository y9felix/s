import urllib.request
import concurrent.futures
import json
import os

url_map = {
    '0': "your set of links",
    '1': "https://github.com/y9felix/s/raw/refs/heads/main/b"
}

existing_lines = set()
try:
    with open('all.txt') as f:
        for line in f:
            cleaned = line.split('#')[0].strip()
            if cleaned: existing_lines.add(cleaned)
except FileNotFoundError:
    pass

user_input = input("Enter numbers: ").split()
thing = input("Enter thing: ")

use_old = input("Use old.json? (y/n): ").lower() == 'y'
old_lines = set()
if use_old and os.path.exists('old.json'):
    try:
        with open('old.json') as f:
            old_lines = set(json.load(f))
    except:
        pass

filter_all = input("Filter all.txt too? (y/n): ").lower() == 'y'
if filter_all:
    existing_lines = {line for line in existing_lines if thing in line.lower()}

urls = []
for num in user_input:
    urls.extend(url_map.get(num, '').split())

new_lines = set()
def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=3) as r:
            return r.read().decode().splitlines()
    except Exception:
        return []
        
with concurrent.futures.ThreadPoolExecutor() as executor:
    for result in executor.map(fetch, urls):
        for line in result:
            if thing in line.lower():
                cleaned = line.split('#')[0].strip()
                if cleaned and cleaned not in old_lines:
                    new_lines.add(cleaned)

before = len(existing_lines)
existing_lines.update(new_lines)
added = len(existing_lines) - before

def sort_key(line):
    parts = line.split('?', 1) if '?' in line else line.split('@', 1)
    return (len(line), parts[1] if len(parts) > 1 else line)

sorted_lines = sorted(existing_lines, key=sort_key)
with open('all.txt', 'w') as f:
    for i, line in enumerate(sorted_lines, 1):
        f.write(f"{line}#{i:05d}\n")

print(f"Added {added} new lines. Total: {len(sorted_lines)}")
