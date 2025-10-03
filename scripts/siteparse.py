import requests
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import re

def fetch_page(page_num):
    """Fetch a single page and extract VLESS links"""
    url = f"https://joss.krikkrik.tech/?page={page_num}&configType=tls"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Find all VLESS links using regex
        pattern = r"onclick=\"showOptions\('VLess', 'vless://([^']+)', 'vless://[^']+'\)\""
        matches = re.findall(pattern, response.text)
        
        return page_num, matches, True
    except Exception as e:
        return page_num, [], False

def main():
    max_workers = 10  # Adjust based on your needs
    all_links = []
    page = 1
    consecutive_empty = 0
    max_consecutive_empty = 3  # Stop after 3 empty pages
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        while consecutive_empty < max_consecutive_empty:
            # Submit multiple pages at once
            futures = []
            for _ in range(max_workers):
                futures.append(executor.submit(fetch_page, page))
                page += 1
            
            # Process results
            for future in as_completed(futures):
                page_num, links, success = future.result()
                
                if success:
                    if links:
                        print(f"Page {page_num}: Found {len(links)} links")
                        all_links.extend([f"vless://{link}" for link in links])
                        consecutive_empty = 0
                    else:
                        print(f"Page {page_num}: No links found")
                        consecutive_empty += 1
                else:
                    print(f"Page {page_num}: Failed to fetch")
                    consecutive_empty += 1
                
                if consecutive_empty >= max_consecutive_empty:
                    break
    
    # Save all links to file
    with open("all.txt", "w") as f:
        for link in all_links:
            f.write(link + "\n")
    
    print(f"\nTotal links found: {len(all_links)}")
    print("Links saved to all.txt")

if __name__ == "__main__":
    main()