
# A slightly more advanced web scraper
# Still uses the same libraries but formats and selects specific data.

import requests
import time
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
job_elements = soup.find_all("div", class_="card-content")

for job_element in job_elements:
    title = job_element.find("h2", class_="title")
    company = job_element.find("h3", class_="company")
    location = job_element.find("p", class_="location")
    apply_link = job_element.find_all("a", class_="card-footer-item")[1]["href"]

    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print(apply_link.strip())
    print(" ")


SAMPLE_OUTPUT = """

        Ship broker
        Fuentes, Walls and Castro
        Michelleville, AP
        https://realpython.github.io/fake-jobs/jobs/ship-broker-99.html

        """



time.sleep(1)