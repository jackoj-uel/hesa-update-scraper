import requests
from bs4 import BeautifulSoup
import json

# Scrape HESA News Data
def scrape_hesa_news():
    url = "https://www.hesa.ac.uk/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    updates = []
    articles = soup.find_all('article', class_='news')

    for article in articles:
        title = article.find('h2').text.strip()
        link = article.find('a')['href']
        date = article.find('time').text
        updates.append({
            'title': title,
            'link': link,
            'date': date
        })

    return updates

# Save the scraped data to a JSON file
def save_updates(updates):
    with open('updates.json', 'w') as f:
        json.dump(updates, f, indent=4)

if __name__ == '__main__':
    updates = scrape_hesa_news()
    save_updates(updates)
