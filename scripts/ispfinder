import requests
import re
from collections import defaultdict
import time

def main():
    with open('all.txt', 'r') as f:
        lines = f.readlines()
    
    isp_lines = defaultdict(list)
    targets = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        match = re.search(r'@([^:]+):', line)
        if match:
            targets.append((match.group(1), line))
    
    for i in range(0, len(targets), 100):
        batch = targets[i:i+100]
        batch_queries = [target for target, _ in batch]
        
        try:
            resp = requests.post('http://ip-api.com/batch?fields=isp', 
                               json=batch_queries, timeout=10)
            results = resp.json()
            
            for j, result in enumerate(results):
                target, line = batch[j]
                isp = result.get('isp', 'Unknown') if result else 'Unknown'
                isp_lines[isp].append(line)
                
        except Exception as e:
            print(f"Batch {i//100 + 1} failed: {e}")
            for target, line in batch:
                isp_lines['Unknown'].append(line)
        
        print(f"Processed {min(i + 100, len(targets))}/{len(targets)}")
        time.sleep(1)
    
    with open('all.txt', 'w') as f:
        for isp, lines_list in sorted(isp_lines.items(), 
                                    key=lambda x: len(x[1]), reverse=True):
            f.write(f"{isp}:\n")
            for line in sorted(lines_list):
                f.write(f"{line}\n")
            f.write("\n")

if __name__ == "__main__":
    main()
