import re

def extract_text_between_symbols(line):
    match = re.search(r'@([^:]*):', line)
    return match.group(1) if match else None

with open('all.txt', 'r') as f:
    all_lines = f.readlines()

with open('yo.txt', 'r') as f:
    yo_lines = f.readlines()

all_texts = {extract_text_between_symbols(line) for line in all_lines if extract_text_between_symbols(line)}
yo_texts = {extract_text_between_symbols(line) for line in yo_lines if extract_text_between_symbols(line)}

matching_lines = [line for line in all_lines if extract_text_between_symbols(line) in yo_texts]

with open('yo.txt', 'a') as f:
    f.writelines(matching_lines)

non_matching_lines = [line for line in all_lines if extract_text_between_symbols(line) not in yo_texts]

with open('all.txt', 'w') as f:
    f.writelines(non_matching_lines)