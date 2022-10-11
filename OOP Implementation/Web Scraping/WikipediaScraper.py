
# Basic web scraper using Beautiful Soup

import requests
import time
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Web_scraping"

# Class Object in this case is requests
# Method is .get(url)
response = requests.get(url)

# BeautifulSoup Object is a html parser.
soup = BeautifulSoup(response.content, "html.parser")
results = soup.find_all('p')

# Writes text to file.
f = open("output.txt", "w")
f.write(results[0].text)
f.close()


# Pauses program so the website doesn't overload or block our connection.
time.sleep(1)