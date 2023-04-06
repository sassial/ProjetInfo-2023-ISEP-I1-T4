import pickle

def affichage(hdict, vliste):
    print(f"{'Nom' : <25}{'Classe' : ^20}{'Vie' : ^10}{'Attaque Principal' : ^20}{'Attaque Secondaire' : ^20}{'Guerison' : >10}")
    
    print() 
    for a in hdict.values():
        print(f"{a.nom : <25}{a.classe : ^20}{a.points_de_vie : ^10}{a.points_dattaque_principaux : ^20}{a.points_dattaque_secondaires : ^20}{a.points_de_guerison : >10}")
    
    print()
    for a in vliste[0]:
        print(f"{a.nom : <25}{a.classe : ^20}{a.points_de_vie : ^10}{a.points_dattaque_principaux : ^20}{a.points_dattaque_secondaires : ^20}{a.points_de_guerison : >10}")


def menuSauvegarde(hdict, vliste):
    while True:
            # Afficher les choix.
            print("\n#1: Continuer", end="")
            print("\n#2: Sauvegarder", end="")
            print("\n#3: Quitter", end="")

            # Demander à l'utilisateur de faire un choix
            choix = int(input("\n=> "))
            if choix == 1:
                break
            elif choix == 2:
                with open('savefile.pickle', 'wb') as f:
                    pickle.dump(hdict, f, protocol=pickle.HIGHEST_PROTOCOL)
                    pickle.dump(vliste, f, protocol=pickle.HIGHEST_PROTOCOL)
                print("\nPartie sauvegardée!\n")
            elif choix == 3:
                exit()
            else:
                print("Saisie non valide, veuillez réessayer.")