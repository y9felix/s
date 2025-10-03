#!/usr/bin/env python3
import requests
import re
from collections import defaultdict
import time

def main():
    with open('all.txt', 'r') as f:
        lines = f.readlines()
    
    isp_lines = defaultdict(list)
    
    for i, line in enumerate(lines):
        line = line.strip()
        match = re.search(r'@([^:]+):', line)
        if match:
            target = match.group(1)
            try:
                time.sleep(0.2)  # Rate limiting
                resp = requests.get(f'http://ip-api.com/json/{target}?fields=isp', timeout=5)
                isp = resp.json().get('isp', 'Unknown')
                isp_lines[isp].append(line)
            except:
                isp_lines['Unknown'].append(line)
        
        if (i + 1) % 10 == 0:
            print(f"Processed {i + 1}/{len(lines)}")
    
    with open('all.txt', 'w') as f:
        for isp in sorted(isp_lines):
            f.write(f"{isp}:\n")
            for line in sorted(isp_lines[isp]):
                f.write(f"{line}\n")
            f.write("\n")

if __name__ == "__main__":
    main()