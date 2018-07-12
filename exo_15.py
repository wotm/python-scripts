#!usr/bin/python3

def exo15():
    a = 0
    b = 1
    c = 0

    nombre = int(input("Entrez un nombre entier : "))
    for i in range(0, nombre):
        print(a, b)
        c = a + b
        a = b
        b = c

exo15()