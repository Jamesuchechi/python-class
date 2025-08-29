import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Main_Page"

try:
    response = requests.get(url)
    response.raise_for_status()
      # Raise an error for bad responses
    soup = BeautifulSoup(response.text, "html.parser")
    
    news_selection = soup.find("div", id="mp-itn")

    headings = soup.find_all("l1") if news_selection else []
    headline_data = [headings.get_text().strip() for headings in headings]

    with open("wikipedia_news_headlines.csv", "w", newline="", encoding= 'utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Headline"])
        writer.writerows([[headline] for headline in headline_data])
        print("Headlines have been written to wikipedia_news_headlines.csv")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")




