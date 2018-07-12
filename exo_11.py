#!usr/bin/python3

def exo11():
    montantHT = int(input("Entrez le montant de l'article : "))
    quantite = int(input("Entrez le nombre d'articles : "))

    montantTTC = (montantHT + (montantHT * 0.2)) * quantite

    print("Montant HT : %d" % montantHT)
    print("Quantite : %d" % quantite)
    print("Montant TTC : %d" % montantTTC)

exo11()