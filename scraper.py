import requests
from bs4 import BeautifulSoup
import schedule
import time

def scrape_news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = soup.find_all('h3')
    with open("headlines.txt", "a", encoding='utf-8') as file:
        file.write(f"\n--- Headlines on {time.ctime()} ---\n")
        for h in headlines[:5]:  # top 5
            file.write(h.get_text(strip=True) + '\n')
    print("Headlines saved.")

schedule.every(1).minutes.do(scrape_news)  # Change to `.hours` if needed

print("Scraper started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)