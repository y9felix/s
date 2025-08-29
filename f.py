import requests
import re

def get_flag_emoji(country_code):
    """Convert country code to flag emoji"""
    if len(country_code) != 2:
        return "🏴"
    
    # Convert each letter to regional indicator symbol
    flag_emoji = ''.join(chr(ord(char) + 127397) for char in country_code.upper())
    return flag_emoji

def scrape_configs():
    base_url = "https://web.xhamster.biz.id/?page={}"
    all_configs = []
    
    for page in range(1, 221):
        try:
            response = requests.get(base_url.format(page))
            response.raise_for_status()
            
            # Find all vless:// links
            vless_links = re.findall(r"copy\('(vless://[^']+)'\)", response.text)
            
            for link in vless_links:
                # Strip everything after last #
                clean_link = link.split('#')[0]
                all_configs.append(clean_link)
                
        except requests.RequestException as e:
            print(f"Error scraping page {page}: {e}")
            continue
    
    # Sort by line length
    all_configs.sort(key=len)
    
    # Add numbered flags
    numbered_configs = []
    for i, config in enumerate(all_configs, 1):
        # Extract country code from Free-CF-Proxy pattern
        country_match = re.search(r'Free-CF-Proxy-([A-Z]{2})', config)
        if country_match:
            country_code = country_match.group(1)
            flag = get_flag_emoji(country_code)
        else:
            flag = "🏴"
        
        numbered_configs.append(f"{config}#{i:05d}{flag}")
    
    # Write to file
    with open('all.txt', 'w') as f:
        f.write('\n'.join(numbered_configs))
    
    print(f"Scraped {len(numbered_configs)} configurations to all.txt")

if __name__ == "__main__":
    scrape_configs()