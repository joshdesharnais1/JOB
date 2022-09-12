import requests
from bs4 import BeautifulSoup
url = 'https://www.scrapethissite.com/pages/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
for tag in soup.find_all('h3', class_ = 'page-title'):
    print("{1}".format(tag.name, tag.text))
    
for tag in soup.find_all('p', class_ = 'lead session-desc'):
    print("{1}".format(tag.name, tag.text))







