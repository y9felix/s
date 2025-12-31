import urllib.request, concurrent.futures, json, os, re, requests, subprocess

def main():
    existing_lines = set()
    old_lines = set()
    new_lines = set()

    user_input = input("Enter numbers: ")
    things = input("Enter thing(s): ").split()
    use_old = input("Use old.json? (y/n): ") == 'y'
    update_old = input("Update old.json dump? (y/n): ") == 'y'
    check_links = input("Check links for validity? (y/n): ") == 'y'

    if os.path.exists('all.txt'):
        with open('all.txt') as f:
            for line in f:
                cleaned = line.split('#')[0].strip()
                if cleaned:
                    existing_lines.add(cleaned)

    if use_old and os.path.exists('old.json'):
        with open('old.json') as f:
            old_lines = set(json.load(f))

    with open('sources.json') as f:
        sources = json.load(f)

    urls = []
    for num in user_input:
        urls.extend(sources.get(num, []))

    def fetch(url):
        try:
            with urllib.request.urlopen(url, timeout=3) as r:
                return r.read().decode().splitlines()
        except:
            return []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for result in executor.map(fetch, urls):
            for line in result:
                cleaned = line.split('#')[0].strip()
                if cleaned and any(word in line.lower() for word in things) and cleaned not in old_lines:
                    new_lines.add(cleaned)

    before = len(existing_lines)
    existing_lines.update(new_lines)
    added = len(existing_lines) - before
    def sort_key(line):
        parts = line.split('?', 1) if '?' in line else line.split('@', 1)
        return (len(line), parts[1] if len(parts) > 1 else line)

    sorted_lines = sorted(existing_lines, key=sort_key)
    total_lines = len(sorted_lines)
    digits_needed = len(str(total_lines))

    processed = []

    if total_lines < 1500:
        print(f"Adding flags automatically for {total_lines} lines...")

        def get_flag(code):
            return ''.join(chr(ord(c) + 127397) for c in code) if code else ''

        def get_country_batch(ip_list):
            url = "http://ip-api.com/batch?fields=countryCode,query"
            try:
                response = requests.post(url, json=ip_list, timeout=5)
                if response.status_code == 200:
                    return {item['query']: item.get('countryCode', '') for item in response.json()}
            except:
                pass
            return {}

        ips = []
        for line in sorted_lines:
            m = re.search(r'@([^:]+):', line)
            if m:
                ips.append(m.group(1))

        ip_country = {}
        batch_size = 100
        for i in range(0, len(ips), batch_size):
            batch = ips[i:i + batch_size]
            print(f"Processing batch {i // batch_size + 1}/{(len(ips)-1)//batch_size + 1}")
            ip_country.update(get_country_batch(batch))

        for i, line in enumerate(sorted_lines, 1):
            m = re.search(r'@([^:]+):', line)
            ip = m.group(1) if m else ''
            flag = get_flag(ip_country.get(ip, ''))
            processed.append(f"{line}#{i:0{digits_needed}d}{flag}")
    else:
        for i, line in enumerate(sorted_lines, 1):
            processed.append(f"{line}#{i:0{digits_needed}d}")

    with open('all.txt', 'w') as f:
        f.write('\n'.join(processed))

    print(f"Added {added} new lines. Total: {len(sorted_lines)}")

    if update_old:
        existing_data = set()
        if os.path.exists('old.json'):
            with open('old.json') as f:
                existing_data = set(json.load(f))
        combined = existing_data.union(sorted_lines)
        with open('old.json', 'w') as f:
            json.dump(list(combined), f, indent=2)
        print(f"Updated old.json with {len(combined)} total lines")

    if check_links:
        subprocess.run(['python', 'a2ray.py'])

if __name__ == "__main__":
    main()