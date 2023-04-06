import pickle
from personne import personnage
from initPerso import heros, vilains
from menus import affichage, menuSauvegarde


class Game:
    fleche = 0

    def __init__(self):
        # Les méchants sont initialisés dans une liste de listes, chaque liste agissant comme une vague d'ennemis
        self.vilains = vilains

        # Les héros sont initialisés dans un dictionnaire.
        self.heros = heros

    def run(self):
        self.menu()
        # Les héros doivent combattre tout les vagues d'ennemis pour terminer le jeu.
        for i in range(len(self.vilains)):
            self.battle()
            self.sauvegarde()

    def menu(self):
     # Afficher les choix.
        print("\n#1: Nouveau Jeu", end="")
        print("\n#2: Charger un Jeu", end="")
        print("\n#3: Quitter", end="")

        # Demander à l'utilisateur de faire un choix
        while True:
            choix = int(input("\n=> "))
            if choix == 1:
                break
            elif choix == 2:
                with open('savefile.pickle', 'rb') as f:
                    self.heros = pickle.load(f)
                    self.vilains = pickle.load(f)
                print("\nPartie chargée!\n")
                break
            elif choix == 3:
                exit()
            else:
                print("Saisie non valide, veuillez réessayer.")

    def battle(self):
        fleche = 5

        # Tant qu'il reste des héros ou des méchants...
        while (len(self.heros) > 0) and (len(self.vilains[0]) > 0):

            # Afficher l'état de tous les caractères.
            self.printCondition()

            # Pour chaque héros de l'équipe...
            for h1, h2 in self.heros.items():
                if h2.classe == "Guerisseur":
                    h = self.soignerHeros(h2)
                    h2.guerir(self.heros[h])

                # Le héros choisit le méchant.
                v = self.combattreMechant(h2)

                # Le héros attaque le méchant.
                if h2.classe == "Mage":
                    h2.attaquerLeGroupe(v, self.vilains[0])
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
                    self.vilains[0].remove(v)
                    break

                # Le méchant attaque le héros.
                if v.classe == "Dragon" or v.classe == "Petit Dragon":
                    v.attaquerLeGroupe(h2, self.heros.values())
                else:
                    if h2.classe == "Chasseur" and fleche == 0:
                        v.attaquerChasseurSansFleches(h2)
                    else:
                        v.attaquer(h2)

                # Si le héros est mort, il est retiré de l'équipe.
                if h2.isDead():
                    print("\n", h2.nom, "est mort...")
                    self.heros.pop(h1)
                    break

        # S'il n'y a plus d'ennemis dans la vague, les héros gagnent la bataille.
        if len(self.vilains[0]) == 0:
            print("\nLes héros ont gagné la bataille !!!")
            del self.vilains[0]

        # Sinon, ce sont les ennemis qui gagnent.
        else:
            print("\nLes méchants ont gagné...")

    def combattreMechant(self, hero):
        # Afficher les choix.
        for i, v in enumerate(self.vilains[0]):
            print("\n#", i + 1, ":", v.nom, end="")

        # Demander à l'utilisateur de faire un choix
        while True:
            choix = input("\n=> " + hero.nom + " combat #")
            try:
                index = int(choix) - 1
                if 0 <= index < len(self.vilains[0]):
                    return self.vilains[0][index]
            except ValueError:
                pass
            print("Saisie non valide, veuillez réessayer.")

    def soignerHeros(self, hero):
        # Afficher les choix.
        for i, h in enumerate(self.heros):
            print("\n#", i + 1, ":", self.heros[h].nom, end="")

        # Demander à l'utilisateur de faire un choix
        while True:
            choix = input("\n=> " + hero.nom + " soigne #")
            try:
                index = int(choix) - 1
                if 0 <= index < len(self.heros):
                    return list(self.heros.keys())[index]
            except ValueError:
                pass
            print("Saisie non valide, veuillez réessayer.")

    def sauvegarde(self):
        menuSauvegarde(self.heros, self.vilains)

    def printCondition(self):
        affichage(self.heros, self.vilains)

Game().run()