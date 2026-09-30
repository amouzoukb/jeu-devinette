# 1. Choisir un nombre secret entre 1 et 100 : Module ramdom
# Repéter tant que le nombre n'est pas trouvé : Boucle while
# Demander une proposition au jouyeur : input()+conversion
# Comparer la proposition au secret : if/elif/else
# Afficher un indice ou felicitations : print()
print("=== Jeu de devinette ===")
print("Devine le nombre secret entre 1 et 100 !")
print("Tu as 10 essais maximum. Bonne chance !")
print()


import random
nombre_secret = random.randint(1, 100)
# print(nombre_secret) # un nombre différent à chaque exécution

trouve = False
max_essais = 10
essais = 0
def verifier_proposition(secret, proposition):
    if proposition == secret :
        return "trouve"
    elif proposition < secret :
        return "trop_petit"
    else :
        return "trop_grand"

while not trouve and essais < max_essais :
    proposition = int(input("Propose un nombre entre 1 et 100 : "))
    essais = essais + 1
    resultat = verifier_proposition(nombre_secret, proposition)
    if resultat == "trouve" :
        print("Bravo ! Tu as trouvé le nombre secret en " + str(essais) + " essais !")
    elif resultat == "trop_petit" :
        print("Trop petit !")
    else :
        print("Trop grand !")

if not trouve :
    print("Perdu ! Le nombre etait " + str(nombre_secret) + " !")







