def combat(hero, vliste):
    # Afficher les choix.
    for i, v in enumerate(vliste[0]):
        print("\n#", i + 1, ":", v.nom, end="")

    # Demander à l'utilisateur de faire un choix
    while True:
        choix = input("\n=> " + hero.nom + " combat #")
        try:
            index = int(choix) - 1
            if 0 <= index < len(vliste[0]):
                return vliste[0][index]
        except ValueError:
            pass
        print("Saisie non valide, veuillez réessayer.")

def soignage(hero, hdict):
    # Afficher les choix.
    for i, h in enumerate(hdict):
        print("\n#", i + 1, ":", hdict[h].nom, end="")

    # Demander à l'utilisateur de faire un choix
    while True:
        choix = input("\n=> " + hero.nom + " soigne #")
        try:
            index = int(choix) - 1
            if 0 <= index < len(hdict):
                return list(hdict.keys())[index]
        except ValueError:
            pass
        print("Saisie non valide, veuillez réessayer.")