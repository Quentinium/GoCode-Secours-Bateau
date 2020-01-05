from math import *

def ask_boats_nbr():
    boats = int(input("Nombre de bateaux (1-100):"))
    if isinstance(boats, int) and boats > 0 and boats <= 100:
        return boats
    else:
        main()

def ask_passagers_nbr():
    passagers = int(input("Nombre de passagers par bateaux (0-50):"))
    if isinstance(passagers, int) and passagers >= 0 and passagers <= 50:
        return passagers
    else:
        main()

def main():
    print("Le centre d'opération vous demande de confirmer les informations suivantes")
    boats = ask_boats_nbr()
    passagers = ask_passagers_nbr()
    passagers_total = passagers * boats
    result = ceil(passagers / 10) * boats
    print("========== Informations ==========")
    print("Nombre de trajets nécessaires: " + str(result))
    print("Nombre de passagers total: " + str(passagers_total))
    print("__")
    print("Plan de navigation par navire: ")
    print("__")
    for i in range(1, ceil(passagers / 10) + 1) :
        passagers -= 10
        if passagers > 0:
            print("[Trajet "+str(i)+"] " + str(passagers) + " restants")
        else:
            print("[Trajet "+str(i)+"] Le bateau est vidé")
            print("==================================")
main()
