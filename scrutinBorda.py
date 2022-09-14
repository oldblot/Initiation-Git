import csv
from encodings import utf_8
def scrutin4():
    with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
        tableau = csv.reader(csvfile, delimiter=",")
        tab = list(tableau)
    
    for i in range(len(tab[1])):
        if tab[1][i] == "1":
            tab[1][i] = 5
        if tab[1][i] == "2":
            tab[1][i] = 4
        if tab[1][i] == "3":
            tab[1][i] = 3
        if tab[1][i] == "4":
            tab[1][i] = 2
        if tab[1][i] == "5":
            tab[1][i] = 1
    print(tab[1])
    for i in range(len(tab[2])):
        if tab[2][i] == "1":
            tab[2][i] = 5
        if tab[2][i] == "2":
            tab[2][i] = 4
        if tab[2][i] == "3":
            tab[2][i] = 3
        if tab[2][i] == "4":
            tab[2][i] = 2
        if tab[2][i] == "5":
            tab[2][i] = 1
    print(tab[2])




 
scrutin4()