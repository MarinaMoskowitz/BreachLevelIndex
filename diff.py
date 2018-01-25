#Perform diff between files in new and old.
# Return the rows that are new
#
import csv

def diff(year):
    """
    Returns the rows that are in the new year file
    :param year:
    :return:
    """
    f1 = open("data/old/data" + year + ".csv")
    oldFile1 = csv.reader(f1)
    oldList1 = list(oldFile1)

    f2 = open("data/new/data" + year + ".csv")
    newFile2 = csv.reader(f2)
    newList2 = list(newFile2)
    f1.close()
    f2.close()

    newRows = [row for row in newList2 if row not in oldList1]
    print(newRows)



