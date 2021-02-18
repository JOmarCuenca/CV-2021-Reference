import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=New-York'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')
# job_elems = results.find_all('div', class_='card-content')
job_elems = results.find_all("div",class_="flex-row")

for job in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job.find('h2', class_='title')
    company_elem = job.find('div', class_='company')
    location_elem = job.find('div', class_='location')
    link = title_elem.find("a")
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print(link.attrs["href"])
    print()

# python_jobs = results.find_all('h2', string='Python Developer')
# jobs = results.find_all('h2',string=lambda text: "python" in text.lower())
# for job in jobs:
#     print(job.prettify())
#     title_elem = job.find('h2', class_='title')
#     company_elem = job.find('div', class_='company')
#     location_elem = job.find('div', class_='location')
#     if None in (title_elem, company_elem, location_elem):
#         continue
#     print(title_elem.text.strip())
#     print(company_elem.text.strip())
#     print(location_elem.text.strip())
#     print()