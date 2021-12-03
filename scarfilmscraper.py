import re
import requests
from bs4 import BeautifulSoup

URL = 'https://scarfilm.org/rekomenduju-k-prosmotru/'

html_text = requests.get(URL).text
soup = BeautifulSoup(html_text, 'html.parser')
contentTable = soup.find('div', { "class" : "post-body-inner"})

titles = contentTable.find_all("strong")

for i in titles:
    print(i.get_text())




