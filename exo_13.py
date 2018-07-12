#!usr/bin/python3

def exo13():
    nombre = int(input("Donnez un nombre entier : "))
    binaire = []
    while nombre:
        reste = nombre % 2
        nombre = nombre//2
        binaire.append(reste)
    print(binaire)

exo13()