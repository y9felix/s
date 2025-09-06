import requests
import re

def get_flag(code):
    return ''.join(chr(ord(c) + 127397) for c in code) if code else ''

cache = {}
def get_country(ip):
    if ip not in cache:
        try:
            r = requests.get(f'http://ip-api.com/json/{ip}?fields=countryCode', timeout=5)
            cache[ip] = r.json().get('countryCode', '')
        except:
            cache[ip] = ''
    return cache[ip]

with open('all.txt') as f:
    lines = [line.strip() for line in f.readlines()]

lines = [line.split('#')[0].strip() for line in lines]
lines.sort(key=lambda x: (len(x), re.search(r'@([^:]+):', x).group(1) if re.search(r'@([^:]+):', x) else ''))

processed = []
for idx, line in enumerate(lines):
    match = re.search(r'@([^:]+):', line)
    ip = match.group(1) if match else ''
    country_code = get_country(ip)
    flag = get_flag(country_code)
    processed.append(f"{line} #{idx+1:03d}{flag}")

with open('all.txt', 'w') as f:
    f.write('\n'.join(processed))
