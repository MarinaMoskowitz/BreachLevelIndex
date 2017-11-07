
"""
Small script to query the csv datafiles
"""
import csv
import sys
import pprint
import os

def main(company,
         year=None):
    """
    Query data for a company, optionally in a specific year
    :param company:
    :param year:
    :return: List of record matches
    """

    dir = os.path.dirname(os.path.abspath(__file__)) + "/"

    if year:
        file_to_open = "data/data" + year
    else:
        file_to_open = "data/combined"

    matches = []

    with open(dir + file_to_open + ".csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if company.lower() in row['Organisation'].lower():
                matches.append(row)
    return matches

if __name__ == '__main__':
    if len(sys.argv) > 1:
        pprint.pprint(main(sys.argv[1]))
    else:
        print("Please provide victim search name")

