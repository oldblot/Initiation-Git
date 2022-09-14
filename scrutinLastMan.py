import csv
from encodings import utf_8
def scrutin3():
    with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
        tableau = csv.reader(csvfile, delimiter=",")
        tab = list(tableau)

   
            
scrutin3()


