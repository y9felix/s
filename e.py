import requests
from urllib.parse import unquote

file_path = "/home/felix/Documents/all.txt"
existing_lines = set()

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            pos = line.rfind('#')
            clean_line = unquote(line[:pos].strip() if pos != -1 else line.strip())
            if clean_line: existing_lines.add(clean_line)
except FileNotFoundError:
    pass

urls = [url.strip() for url in input("URLs: ").replace(',', ' ').split()]
new_lines = set()

for url in urls:
    try:
        response = requests.get(url, timeout=10)
        text = response.text
        for line in text.splitlines():
            pos = line.rfind('#')
            clean_line = unquote(line[:pos].strip() if pos != -1 else line.strip())
            if clean_line: new_lines.add(clean_line)
    except:
        continue

original_count = len(existing_lines)
existing_lines.update(new_lines)
new_count = len(existing_lines) - original_count

def sort_key(line):
    q_pos = line.find('?')
    return (len(line), line[q_pos:] if q_pos != -1 else line)

sorted_lines = sorted(existing_lines, key=sort_key)

host_to_flag = {}

def country_to_flag(cc):
    return ''.join(chr(ord(c) + 127397) for c in cc) if cc else ''

for line in sorted_lines:
    host = None
    at_pos = line.find('@')
    if at_pos != -1:
        rest = line[at_pos+1:]
        colon_pos = rest.find(':')
        if colon_pos != -1:
            host_candidate = rest[:colon_pos]
            if host_candidate.startswith('[') and host_candidate.endswith(']'):
                host = host_candidate[1:-1]
            else:
                host = host_candidate
    
    print(host)
    if host and host not in host_to_flag:
        try:
            response = requests.get(f"http://ip-api.com/json/{host}?fields=countryCode", timeout=5)
            if response.status_code == 200:
                data = response.json()
                host_to_flag[host] = country_to_flag(data.get('countryCode', ''))
            else:
                host_to_flag[host] = ''
        except:
            host_to_flag[host] = ''

with open(file_path, 'w', encoding='utf-8') as f:
    for idx, line in enumerate(sorted_lines, 1):
        host = None
        at_pos = line.find('@')
        if at_pos != -1:
            rest = line[at_pos+1:]
            colon_pos = rest.find(':')
            if colon_pos != -1:
                host_candidate = rest[:colon_pos]
                if host_candidate.startswith('[') and host_candidate.endswith(']'):
                    host = host_candidate[1:-1]
                else:
                    host = host_candidate
        flag_emoji = host_to_flag.get(host, '') if host else ''
        f.write(f"{line}#{idx:03d}{flag_emoji}\n")

print(f"New: {new_count}, Total: {len(existing_lines)}")