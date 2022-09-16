import csv
def scrutin2():
    with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
        tableau = csv.reader(csvfile, delimiter=",")
        tab = list(tableau)

#Premier tour
    selection1 = 0
    selection2 = 0
    for iden1 in range(len(tab[1])):
        if tab[1][iden1]=="1":
            selection1 = tab[0][iden1]
    for iden2 in range(len(tab[2])):
        if tab[2][iden2]=="1":
            selection2 = tab[0][iden2]

#Deuxieme tour
    duelsgagnésc1 = 0
    duelsgagnésc2 = 0
    i = 1
    vainqueur = 0
    for j in range(3,7):
        if tab[j][i] > tab[j][i+1]:
            duelsgagnésc2 += 1
        else: duelsgagnésc1 += 1
        if duelsgagnésc1 > duelsgagnésc2 :
            vainqueur = tab[0][1]
        else : 
            vainqueur =  tab[0][2]

    return [selection1, selection2, vainqueur]

print(scrutin2())


