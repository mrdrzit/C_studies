import requests as re
import numpy as np
from bs4 import BeautifulSoup as bs

base_urls = ['https://pegaso.changeip.org/DOCS-TECH/Programming/Python/',
             'https://pegaso.changeip.org/DOCS-TECH/Programming/The%20Art%20of%20Computer%20Programming/',
             'https://pegaso.changeip.org/DOCS-TECH/Programming/Secure%20Programming/',
             'https://pegaso.changeip.org/DOCS-TECH/Programming/Regular%20Expressions/',
             'https://pegaso.changeip.org/DOCS-TECH/Programming/JavaScript/',
             'https://pegaso.changeip.org/DOCS-TECH/Programming/JavaScript/',
             'https://pegaso.changeip.org/DOCS-TECH/Programming/Art%20of%20Computer%20Programming/',
             'https://pegaso.changeip.org/DOCS-TECH/Programming/Advanced/',
             'https://pegaso.changeip.org/DOCS-TECH/AI/',
             'https://pegaso.changeip.org/DOCS-TECH/Hacking/Reversing%20and%20Exploiting/Reversing/',
             'https://pegaso.changeip.org/DOCS-TECH/Hacking/USB/',
             'https://pegaso.changeip.org/DOCS-TECH/Information%20Theory/',
             ]

hrefs = [[0]*150 for i in range(0, len(base_urls))]
names = [[0]*150 for i in range(0, len(base_urls))]


with re.session() as req:
  print("I'll do stuff, hang tight")
  for url in range(0, len(base_urls)):
    place = 0
    html = req.get(base_urls[url])
    soup = bs(html.text, 'html.parser').find_all('a')
    for refs in range(0, len(soup)):
      if soup[refs].attrs['href'].endswith('pdf'):
        hrefs[url][place] = base_urls[url] + soup[refs].attrs['href']
        names[url][place] = soup[refs].text
        place += 1

for values in range(0, len(hrefs)):
  hrefs[values] = np.trim_zeros(hrefs[values])
  names[values] = np.trim_zeros(names[values])

print("Let's download some stuff")

with re.session() as req:
  for links in range(0, len(base_urls)):
    for files in range(0, len(hrefs[links])):
      try:
        download = req.get(hrefs[links][files])
      except re.exceptions.ConnectionError:
        print("couldn't connect to server")
      if download.status_code == 200:
        with open(names[links][files], 'wb') as f:
          print(f"Downloading: {names[links][files]}")
          f.write(download.content)
      else:
        print(f"Download Failed For File {names[links][files]}")