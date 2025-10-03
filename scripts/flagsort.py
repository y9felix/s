import re
from collections import Counter

with open('all.txt', 'r') as f:
    lines = f.readlines()

def get_group_key(line):
    after_hash = line.split('#')[-1]
    match = re.match(r'([^\d]*)', after_hash)
    return match.group(1) if match else ''

group_keys = [get_group_key(line) for line in lines]
group_counts = Counter(group_keys)
lines.sort(key=lambda x: (-group_counts[get_group_key(x)], x.split('#')[-1]))

with open('all.txt', 'w') as f:
    f.writelines(lines)