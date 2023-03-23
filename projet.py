from personnage import personnage

class Game:
    def __init__(self):
        #Les vagues sont initialisées séparément des méchants car les héros ne combattent qu'une vague à la fois.
        self.vilains = []

        self.vague1 = []
        self.vague2 = []
        self.vague3 = []
        self.vague4 = []

        self.vague1.append(personnage("Troll 1", "Troll", 5, 4, 0, 0))
        self.vague1.append(personnage("Troll 2", "Troll", 5, 4, 0, 0))
        self.vague1.append(personnage("Troll 3", "Troll", 5, 4, 0, 0))

        self.vague2 = self.vague1.copy()
        self.vague2.append(personnage("Troll 4", "Troll", 5, 4, 0, 0))

        self.vague3 = self.vague2.copy()
        self.vague3.append(personnage("Troll 5", "Troll", 5, 4, 0, 0))

        self.vague4.append(personnage("Smaug le Dragon", "Dragon", 15, 6, 2, 0))

        #Les héros sont initialisés dans un dictionnaire plutôt que dans une liste comme les méchants.
        self.heros = {}

        self.heros["Guerrier"] = personnage("Ares le Guerrier", "Guerrier", 10, 5, 0, 0)
        self.heros["Chasseur"] = personnage("Artemis le Chasseur", "Chasseur", 10, 3, 0, 0)
        self.heros["Guerisseur"] = personnage("Apollo le Guerisseur", "Guerisseur", 10, 1, 0, 2)
        self.heros["Mage"] = personnage("Athena le Mage", "Mage", 10, 4, 2, 0)

    def run(self):
        #Chaque fois que les héros terminent le combat, une nouvelle vague de monstres vient s'ajouter aux méchants.
        self.vilains = self.vilains + self.vague1
        self.battle()
        self.vilains = self.vilains + self.vague2
        self.battle()
        self.vilains = self.vilains + self.vague3
        self.battle()
        self.vilains = self.vilains + self.vague4
        self.battle()

    def battle(self):
        while (len(self.heros) > 0) and (len(self.vilains) >0): #Tant qu'il reste des héros ou des méchants...
            self.printCondition() #Afficher l'état de tous les caractères
            for h1, h2 in self.heros.items(): #Pour chaque héros de l'équipe...
                if h2.classe == "Guerisseur":
                    h = self.choisirHeros(h2)
                    h2.guerir(self.heros[h])
                v = self.choisirMechant(h2) #Le héros choisit le méchant
                if h2.classe == "Mage":
                    h2.attaquerLeGroupe(v, self.vilains)
                else:
                    h2.attaquer(v) #Le héros attaque le méchant
                if v.isDead(): #Si le méchant est mort, il est retiré de l'équipe.
                    print("\n", v.nom, "est mort...")
                    self.vilains.remove(v)
                    break
                if v.classe == "Dragon":
                    v.attaquerLeGroupe(h2, self.heros.values()) #Le méchant attaque le héros
                else:
                    v.attaquer(h2) #Le méchant attaque le héros
                if h2.isDead(): #Si le héros est mort, il est retiré de l'équipe.
                    print("\n", h2.nom, "est mort...")
                    self.heros.pop(h1)
                    break
        if len(self.vilains) == 0:
            print("\nLes héros ont gagné la bataille !!!")
        else:
            print("\nLes méchants ont gagné...")

    def choisirMechant(self, hero):
        for i, v in enumerate(self.vilains):
            print("\n#",i+1,":",v.nom, end="")
        while True:
            choix = input("\n=> " + hero.nom + " combat #")
            try:
                index = int(choix)-1
                if index >= 0 and index < len(self.vilains)+1:
                    return self.vilains[index]
            except ValueError:
                pass
            print("Saisie non valide, veuillez réessayer.")

    def choisirHeros(self, hero):
        for i, h in enumerate(self.heros):
            print("\n#",i+1,":", self.heros[h].nom, end="")
        while True:
            choix = input("\n=> " + hero.nom + " soigne #")
            try:
                index = int(choix)-1
                if index >= 0 and index < len(self.heros)+1:
                    return list(self.heros.keys())[index]
            except ValueError:
                pass
            print("Saisie non valide, veuillez réessayer.")

    def printCondition(self):
        print(f"{'Nom' : <25}{'Classe' : ^20}{'Vie' : ^10}{'Attaque Principal' : ^20}{'Attaque Secondaire' : ^20}{'Guerison' : >10}")
        print()
        for a in self.heros.values():
            print(f"{a.nom : <25}{a.classe : ^20}{a.points_de_vie : ^10}{a.points_dattaque_principaux : ^20}{a.points_dattaque_secondaires : ^20}{a.points_de_guerison : >10}")
        print()
        for a in self.vilains:
            print(f"{a.nom : <25}{a.classe : ^20}{a.points_de_vie : ^10}{a.points_dattaque_principaux : ^20}{a.points_dattaque_secondaires : ^20}{a.points_de_guerison : >10}")

Game().run()