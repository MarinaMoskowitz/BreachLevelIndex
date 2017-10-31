from bs4 import BeautifulSoup

import requests


r  = requests.get("http://breachlevelindex.com/data-breach-database.php?range=2017")

data = r.text

soup = BeautifulSoup(data)

data = dict()

table = soup.find_all('tbody')
print(type(table))
table.
#for row in table.find_all('tr'):
#    print(row)
#    print('\n\n\n\n\n\n\n\n\n')