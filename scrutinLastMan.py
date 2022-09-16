from code import interact
import csv
def scrutin3():
    with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
        tableau = csv.reader(csvfile, delimiter=",")
        tab = list(tableau)

    for j in range(len(tab)):
        score = [tab[j][0]]
        print(score)
    for i in range(len(tab)):
        if "1" in tab[i]:
            print(tab[i])
       
          
scrutin3()


