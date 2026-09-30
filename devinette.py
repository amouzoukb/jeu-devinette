# 1. Choisir un nombre secret entre 1 et 100 : Module ramdom
# Repéter tant que le nombre n'est pas trouvé : Boucle while
# Demander une proposition au jouyeur : input()+conversion
# Comparer la proposition au secret : if/elif/else
# Afficher un indice ou felicitations : print()

import random 
nombre_secret = random.randint(1, 20)
trouve = False
essais = 0
while not trouve :
    proposition = int(input("Tape le nombre : "))
    essais = essais + 1
    if proposition == nombre_secret :
        print("Bravo, tu as trouvé en " + str(essais) + " essais")
        trouve =  True
    elif proposition < nombre_secret :
        print("Trop petit !")
    else :
        print("Trop grand !")