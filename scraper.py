import requests
from bs4 import BeautifulSoup
import json

def scrape_hesa_news():
    try:
        url = "https://www.hesa.ac.uk/news"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        updates = []
        articles = soup.find_all('article', class_='node--type-news')

        if not articles:
            print("No articles found. The page structure might have changed.")
            return updates

        for article in articles:
            title_element = article.find('h2')
            link_element = article.find('a', href=True)
            date_element = article.find('time')

            if title_element and link_element and date_element:
                title = title_element.get_text(strip=True)
                link = link_element['href']
                date = date_element.get_text(strip=True)
                updates.append({
                    'title': title,
                    'link': link,
                    'date': date
                })
            else:
                print("Missing elements in an article block.")

        return updates

    except Exception as e:
        print(f"An error occurred during scraping: {e}")
        raise

def save_updates(updates):
    with open('updates.json', 'w') as f:
        json.dump(updates, f, indent=4)

if __name__ == '__main__':
    updates = scrape_hesa_news()
    if updates:
        save_updates(updates)
    else:
        print("No updates found to save.")
