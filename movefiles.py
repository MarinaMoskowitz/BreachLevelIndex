
import os


def move_all():
    years = ["2017", "2016","2015","2014", "2013","2012"]
    for year in years:
        move(year)


def move(year):
    os.rename("data/new/data" + year + ".csv", "data/old/data" + year + ".csv")
