#!usr/bin/python3

maListe = []
print(type(maListe))

maListe = [1,2,3]
print(maListe)

maListe = []
maListe.append(1)
print(maListe)

maListe.append("salut")
print(maListe)

maListe = ["1er", "deuxième", "troisième"]
print(maListe[1])
print(maListe[2])

maListe[1] = "changement"
print(maListe)

#Supprimé avec l'index
del maListe[1]
print(maListe)

#Supprimé avec la valeur
maListe.remove("troisième")
print(maListe)