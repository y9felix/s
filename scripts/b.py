import requests
import re
import json
from urllib.parse import unquote

def get_flag(code):
    return ''.join(chr(ord(c) + 127397) for c in code) if code else ''

try:
    with open('iplist.json', 'r') as f:
        iplist = json.load(f)
except FileNotFoundError:
    iplist = {}

cache = iplist.copy()

def get_country(ip):
    if ip not in cache:
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}?fields=countryCode", timeout=5)
            cache[ip] = r.json().get('countryCode', '')
            iplist[ip] = cache[ip] 
        except:
            cache[ip] = ''
    return cache[ip]

with open('all.txt') as f:
    lines = f.readlines()

processed = []
for idx, line in enumerate(lines):
    line = line.strip()
    
    if '#' in line:
        parts = line.rsplit('#', 1)
        server_info = parts[0].strip()
        existing_metadata = unquote(parts[1])
        if len(existing_metadata) >= 2 and ord(existing_metadata[-1]) > 127397:
            flag = existing_metadata[-2:]
            country_code = ''
            ip = re.search(r'@([^:]+):', server_info).group(1) if re.search(r'@([^:]+):', server_info) else ''
        else:
            match = re.search(r'@([^:]+):', server_info)
            ip = match.group(1) if match else ''
            country_code = get_country(ip)
            flag = get_flag(country_code)
    else:
        server_info = line
        match = re.search(r'@([^:]+):', server_info)
        ip = match.group(1) if match else ''
        country_code = get_country(ip)
        flag = get_flag(country_code)
    
    print(f"{ip} is {flag}")
    processed.append(f"{server_info}#{idx+1:03d}{flag}")

with open('iplist.json', 'w') as f:
    json.dump(iplist, f)

processed.sort(key=lambda x: (len(x), re.search(r'@([^:]+):', x).group(1) if re.search(r'@([^:]+):', x) else '')) 

with open('all.txt', 'w') as f:
    f.write('\n'.join(processed))
