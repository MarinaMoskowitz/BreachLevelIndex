
"""
Small script to query the csv datafiles
"""
import csv
import pprint
import sys

def main(company,
         year=None):
    """
    Query data for a company, optionally in a specific year
    :param company:
    :param year:
    :return: List of record matches
    """
    if year:
        file_to_open = "data/data" + year
    else:
        file_to_open = "data/combined"

    matches = []

    with open(file_to_open + ".csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if company in row['Organisation']:
                matches.append(row)
                pprint.pprint(row)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(sys.argv[1]))
    else:
        print("Please provide victim search name")

