with open('all.txt') as f:
    lines = f.readlines()

lines.sort(key=lambda x: x.split('#')[-1].lstrip('0123456789'))

with open('all.txt', 'w') as f:
    f.writelines(lines)
