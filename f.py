import requests
import re

def get_flag_emoji(country_code):
    if len(country_code) != 2:
        return "🏴"
    flag_emoji = ''.join(chr(ord(char) + 127397) for char in country_code.upper())
    return flag_emoji

def scrape_configs():
    base_url = "https://web.xhamster.biz.id/?page={}"
    all_configs = []
    
    for page in range(1, 221):
        try:
            response = requests.get(base_url.format(page))
            response.raise_for_status()
            vless_links = re.findall(r"copy\('(vless://[^']+)'\)", response.text)
            
            for link in vless_links:
                clean_link = link.split('#')[0]
                all_configs.append(clean_link)
                
        except requests.RequestException as e:
            print(f"Error scraping page {page}: {e}")
            continue
            
    all_configs.sort(key=len)
    numbered_configs = []
    
    for i, config in enumerate(all_configs, 1):
        country_match = re.search(r'Free-CF-Proxy-([A-Z]{2})', config)
        if country_match:
            country_code = country_match.group(1)
            flag = get_flag_emoji(country_code)
        else:
            flag = "🏴"
        numbered_configs.append(f"{config}#{i:05d}{flag}")
    
    with open('all.txt', 'w') as f:
        f.write('\n'.join(numbered_configs))
    
    print(f"Scraped {len(numbered_configs)} configurations to all.txt")

if __name__ == "__main__":
    scrape_configs()
