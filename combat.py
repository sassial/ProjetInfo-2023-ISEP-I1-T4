from menus import affichage
from actionsPerso import combat, soignage

def bataille(hdict, vliste):
        fleche = 5

        # Tant qu'il reste des héros ou des méchants...
        while (len(hdict) > 0) and (len(vliste[0]) > 0):

            # Afficher l'état de tous les caractères.
            affichage(hdict, vliste)

            # Pour chaque héros de l'équipe...
            for h1, h2 in hdict.items():

                # Si le héros est le guerisseur, il soigne d'abord un héros
                if h2.classe == "Guerisseur":
                    h = soignage(h2, hdict)
                    h2.guerir(hdict[h])

                # Le héros choisit le méchant.
                v = combat(h2, vliste)

                # Le héros attaque le méchant.
                if h2.classe == "Mage":
                    h2.attaquerLeGroupe(v, vliste[0])
                elif h2.classe == "Chasseur":
                    if fleche > 0:
                        h2.attaquer(v)
                        fleche -= 1
                        print("\n Il ne lui reste que", fleche, "flèches")
                else:
                    h2.attaquer(v)

                # Si le méchant est mort, il est retiré de l'équipe.
                if v.isDead():
                    print("\n", v.nom, "est mort...")
                    vliste[0].remove(v)
                    break

                # Le méchant attaque le héros.
                if v.classe == "Dragon" or v.classe == "Petit Dragon":
                    v.attaquerLeGroupe(h2, hdict.values())
                else:
                    if h2.classe == "Chasseur" and fleche == 0:
                        v.attaquerChasseurSansFleches(h2)
                    else:
                        v.attaquer(h2)

                # Si le héros est mort, il est retiré de l'équipe.
                if h2.isDead():
                    print("\n", h2.nom, "est mort...")
                    hdict.pop(h1)
                    break

        # S'il n'y a plus d'ennemis dans la vague, les héros gagnent la bataille.
        if len(vliste[0]) == 0:
            print("\nLes héros ont gagné la bataille !!!")
            del vliste[0]

        # Sinon, ce sont les ennemis qui gagnent.
        else:
            print("\nLes méchants ont gagné...")