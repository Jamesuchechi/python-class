import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Main_Page"

print("Fetching the main page of Wikipedia...")

try:
    response = requests.get(url)
    response.raise_for_status()
      # Raise an error for bad responses
    soup = BeautifulSoup(response.text, "html.parser")
    
    news_section = soup.find("div", id="mp-itn")

    headlines = news_section.find_all("h1, h2, h3, h4, h5, h6")

    print("Latest news headlines: ", headlines)
    for i, headline in enumerate(headlines, 1):
        print(f"Headline {i}: {headline.get_text().strip()}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")  