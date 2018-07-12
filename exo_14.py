#!usr/bin/python3

def exo14():
    somme = 0
    for i in range(1, 1000):
        if i % 3 == 0 and i % 5 == 0:
            somme += i
    print(somme)

exo14()