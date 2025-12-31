import requests
from bs4 import BeautifulSoup

# Config
LARAVEL_API = "http://127.0.0.1:8000/api/articles"
# We target page 5 to get older articles
TARGET_URL = "https://beyondchats.com/blogs/page/5/" 

def seed_database():
    print(f"Scraping {TARGET_URL}...")
    try:
        response = requests.get(TARGET_URL)
        if response.status_code != 200:
            print("Failed to fetch page.")
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Select article cards
        article_links = soup.select('.post-card-content-link')[:5] 
        
        # Fallback selector if the above fails
        if not article_links:
            article_links = soup.select('a.post-card-image-link')[:5]

        for link_tag in article_links:
            href = link_tag['href']
            article_url = "https://beyondchats.com" + href if href.startswith('/') else href
            
            print(f"Fetching: {article_url}")
            try:
                art_resp = requests.get(article_url)
                art_soup = BeautifulSoup(art_resp.content, 'html.parser')

                title_tag = art_soup.select_one('h1')
                title = title_tag.get_text(strip=True) if title_tag else "Untitled"

                content_div = art_soup.select_one('.gh-content') or art_soup.select_one('.entry-content')
                content = content_div.get_text(strip=True) if content_div else "Content not found"

                payload = {
                    "title": title,
                    "original_content": content,
                    "source_url": article_url
                }

                api_post = requests.post(LARAVEL_API, json=payload)
                if api_post.status_code == 201:
                    print(f"Saved: {title}")
                else:
                    print(f"Error saving {title}: {api_post.text}")
            except Exception as e:
                print(f"Error fetching detail: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    seed_database()