from bs4 import BeautifulSoup
import requests
import csv
import os

def scrape(year):
    r = requests.get("http://breachlevelindex.com/data-breach-database.php?range=" + year)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')
    data = dict()
    table = soup.find('tbody')

    pulled_data = list()

    for row in table.find_all('tr'):
        pulled_data.append(make_row_dict(row.find_all('td')))

    return pulled_data

def make_row_dict(cols):
    headers = [
        'Rank',
        'Organisation',
        'Records Breached',
        'Date',
        'Type',
        'Source of Breach',
        'Location',
        'Industry',
        'Risk Source',
        'Link'
    ]
    values = []
    for i in range(0, len(cols)):
        values.append(clean(cols[i]))
    row_dict = dict(zip(headers,values))
    return row_dict

def clean(col):
    atag = col.find('a')
    if atag:
        return atag.get('href')
    else:
        return col.text

def write_to_csv(data, filename):
    dir = os.path.dirname(os.path.abspath(__file__)) + "/"
    with open(dir + 'data/new/' + filename + '.csv', 'w') as csvfile:
        fieldnames = list((data[0]).keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def scrape_to_csv(year):
    write_to_csv(scrape(year), "data" + year)


def scrape_all():
    years = ["2018", "2017","2016","2015","2014", "2013"]
    for year in years:
        scrape_to_csv(year)