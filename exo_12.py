#!usr/bin/python3

def exo12():
    saisie = int(input("Entrez un nombre : "))

    fact = 1
    for i in range(1, saisie+1):
        fact = fact * i

    print("La factorielle de %d vaut %d" %(saisie, fact))

exo12()