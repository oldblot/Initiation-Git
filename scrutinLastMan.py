import csv
from encodings import utf_8
#def scrutin1():
with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
    tableau = csv.reader(csvfile, delimiter=",")
    tab = list(tableau)
    print (tab)

