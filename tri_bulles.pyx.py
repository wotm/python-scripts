import random

maListe = [4,8,415,1,25,75,6]
print(maListe)

flag = False
limit = len(maListe)

while not flag:
    flag = True
    for i in range(0, limit-1):
        if maListe[i] > maListe[i+1]:
            maListe[i], maListe[i+1] = maListe[i+1], maListe[i]
            flag = False
    limit = limit - 1

print(maListe)