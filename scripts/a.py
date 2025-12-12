import urllib.request, concurrent.futures, json, os, re, requests

def main():
    url_map = {
        '0': "your set of links",}

    urls = []
    old_lines = set()
    new_lines = set()
    existing_lines = set()
    user_input = input("Enter numbers: ")
    things = input("Enter thing(s): ").split()
    
    use_old = input("Use old.json? (y/n): ") == 'y'
    update_old = input("Update old.json dump? (y/n): ") == 'y'

    if os.path.exists('all.txt'):
        with open('all.txt') as f:
            for line in f:
                cleaned = line.split('#')[0].strip()
                if cleaned:
                    existing_lines.add(cleaned)

    if use_old and os.path.exists('old.json'):
        with open('old.json') as f:
            old_lines = set(json.load(f))

    for num in user_input:
        urls.extend(url_map.get(num, '').split())

    def fetch(url):
        try:
            with urllib.request.urlopen(url, timeout=3) as r:
                return r.read().decode().splitlines()
        except Exception:
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
                data = json.dumps(ip_list)
                headers = {'Content-Type': 'application/json'}
                response = requests.post(url, data=data, headers=headers, timeout=5)
                if response.status_code == 200:
                    results = response.json()
                    return {item['query']: item.get('countryCode', '') for item in results}
            except Exception:
                pass
            return {}

        ips_to_resolve = []
        for line in sorted_lines:
            match = re.search(r'@([^:]+):', line)
            ip = match.group(1) if match else ''
            if ip:
                ips_to_resolve.append(ip)

        ip_country = {}
        batch_size = 100
        for i in range(0, len(ips_to_resolve), batch_size):
            batch_ips = ips_to_resolve[i:i + batch_size]
            print(f"Processing batch {i // batch_size + 1}/{(len(ips_to_resolve)-1)//batch_size + 1}")
            batch_results = get_country_batch(batch_ips)
            ip_country.update(batch_results)

        for i, line in enumerate(sorted_lines, 1):
            match = re.search(r'@([^:]+):', line)
            ip = match.group(1) if match else ''
            flag = get_flag(ip_country.get(ip, ''))
            processed.append(f"{line}#{i:0{digits_needed}d}{flag}")

    else:
            processed = [f"{line}" for line in sorted_lines]

    with open('all.txt', 'w') as f:
        f.write('\n'.join(processed))

    print(f"Added {added} new lines. Total: {len(sorted_lines)}")

    if update_old:
        existing_data = set()
        if os.path.exists('old.json'):
            with open('old.json', 'r') as f:
                existing_data = set(json.load(f))
        combined_data = existing_data.union(sorted_lines)
        with open('old.json', 'w') as f:
            json.dump(list(combined_data), f, indent=2)
        print(f"Updated old.json with {len(combined_data)} total lines")

if __name__ == "__main__":
    main()
