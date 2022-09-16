import csv
from encodings import utf_8
def valeurs():
    with open("tableauvote.csv", newline='',encoding='utf-8') as csvfile:
        tableau = csv.reader(csvfile, delimiter=",")
        tab = list(tableau)
    
    points = [[0]*len(tab[0]) for _ in range(len(tab)) ]
    for i in range(1, len(tab)):
        points[i][0] = int(tab[i][0])
        for j in range(1,len(tab[i])):
            points[i][j] = (5 if tab[i][j]== "1" else 
                4 if tab[i][j] == "2" else 
                3 if tab[i][j]== "3" else 
                2 if tab[i][j] == "4" else 
                1 if tab[i][j]=="5" else tab[i][j])
    return points
    
def votes(points): 
    total = [0]*len(points[0])
    for icol in range(1,len(points[0])):
        for ilign in range(1,len(points)):
            total[icol] += points[ilign][0]*points[ilign][icol]
    
    return total

def maxscore(total):
    max = total[0]
    indmax = 0
    for ind in range(1,len(total)):
        if total[ind]> max:
            max = total[ind]
            indmax = ind
    return max,indmax

def vainqueur(ind, tab):
    for v in range(len(tab)):
        if v == ind:
            return tab[0][v]





tableau = valeurs()
resultats = votes(tableau)
score = maxscore(resultats)
print(vainqueur(score, tab))


            


