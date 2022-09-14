import csv
from encodings import utf_8
def scrutin2():
    with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
        tableau = csv.reader(csvfile, delimiter=",")
        tab = list(tableau)

#Premier tour
        for iden1 in range(len(tab[1])):
            if tab[1][iden1]=="1":
                print("le premier selectioné est" ,tab[0][iden1-1],"avec", tab[1][0], "votes")
        for iden2 in range(len(tab[2])):
            if tab[2][iden2]=="1":
                print("le deuxième selectioné est", tab[0][iden2-1],"avec",tab[2][0], "votes")

#Deuxieme tour

        duelsgagnésc1 = 0
        duelsgagnésc2 = 0
        i = 1
        for j in range(3,7):
            if tab[j][i] > tab[j][i+1]:
                duelsgagnésc2 += 1
            else: duelsgagnésc1 += 1
        if duelsgagnésc1 > duelsgagnésc2 :
            print("le grand vainqueur est", tab[0][0])
        else : 
            print("le grand vainqueur est", tab[0][1])

scrutin2()
