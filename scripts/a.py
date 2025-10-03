import urllib.request, concurrent.futures, json, os, re, requests

def get_flag(code):
    return ''.join(chr(ord(c) + 127397) for c in code) if code else ''

def sort_lines(lines):
    def sort_key(line):
        parts = line.split('?', 1) if '?' in line else line.split('@', 1)
        return (len(line), parts[1] if len(parts) > 1 else line)
    
    return sorted(lines, key=sort_key)

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=3) as r:
            return r.read().decode().splitlines()
    except Exception:
        return []

def main():
    url_map = {
        '0': "your set of links",
        '1': "https://github.com/y9felix/s/raw/refs/heads/main/b"}
    urls = []
    old_lines = set()
    new_lines = set()
    existing_lines = set()

    user_input = input("Enter numbers: ")
    thing = input("Enter thing: ")
    use_old = input("Use old.json? (y/n): ") == 'y'
    filter_all = input("Filter all.txt too? (y/n): ") == 'y'
    add_flags = input("Add flags to lines? (y/n): ") == 'y'
    update_old = input("Update old.json dump? (y/n): ") == 'y'

    if os.path.exists('all.txt'):
        with open('all.txt') as f:
            for line in f:
                cleaned = line.split('#')[0].strip()
                if cleaned: existing_lines.add(cleaned)

    if use_old and os.path.exists('old.json'):
        with open('old.json') as f:
            old_lines = set(json.load(f))

    if filter_all:
        existing_lines = {line for line in existing_lines if thing in line.lower()}

    for num in user_input:
        urls.extend(url_map.get(num, '').split())
            
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
    sorted_lines = sort_lines(existing_lines)
    
    if add_flags:
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

        processed = []
        for i, line in enumerate(sorted_lines, 1):
            match = re.search(r'@([^:]+):', line)
            ip = match.group(1) if match else ''
            country_code = get_country(ip)
            flag = get_flag(country_code)
            print(f"{ip} is {flag}")
            processed.append(f"{line}#{flag}{i:04d}")

        save_json('iplist.json', iplist)
        
        with open('all.txt', 'w') as f:
            f.write('\n'.join(processed))
    else:
        with open('all.txt', 'w') as f:
            for i, line in enumerate(sorted_lines, 1):
                f.write(f"{line}#{i:05d}\n")

    print(f"Added {added} new lines. Total: {len(sorted_lines)}")
    
    if update_old:
        existing_data = set()
        if os.path.exists('old.json'):
         with open('old.json', 'r') as f:
                existing_data = set(json.load(f))
        combined_data = existing_data.union(sorted_lines)
        save_json('old.json', list(combined_data))
        
        print(f"Updated old.json with {len(combined_data)} total lines")

if __name__ == "__main__":
    main()
