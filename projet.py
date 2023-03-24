from personne import personnage
from initVague import initVagueTrolls

class Game:
    fleche = 0
    
    def __init__(self):
        #Les méchants sont initialisés dans une liste de listes, chaque liste agissant comme une vague d'ennemis
        self.vilains = [[], [], [], []]
        for i in range(3):
            self.vilains[i] = initVagueTrolls(self.vilains[i], i+3, (i*(i+1))//2 + 2*i )

        self.vilains[3].append(personnage("Smaug le Dragon", "Dragon", 15, 6, 2, 0))

        #Les héros sont initialisés dans un dictionnaire.
        self.heros = {}

        self.heros["Guerrier"] = personnage("Ares le Guerrier", "Guerrier", 10, 5, 0, 0)
        self.heros["Chasseur"] = personnage("Artemis le Chasseur", "Chasseur", 10, 3, 0, 0)
        self.heros["Guerisseur"] = personnage("Apollo le Guerisseur", "Guerisseur", 10, 1, 0, 2)
        self.heros["Mage"] = personnage("Athena le Mage", "Mage", 10, 4, 2, 0)

    def run(self):
        #Les héros doivent combattre 4 vagues d'ennemis pour terminer le jeu.
        for i in range(4):
            self.battle()

    def battle(self):
        fleche = 5

        #Tant qu'il reste des héros ou des méchants...
        while (len(self.heros) > 0) and (len(self.vilains[0]) >0):

            #Afficher l'état de tous les caractères.
            self.printCondition()
            
            #Pour chaque héros de l'équipe...
            for h1, h2 in self.heros.items():
                if h2.classe == "Guerisseur":
                    h = self.choisirHeros(h2)
                    h2.guerir(self.heros[h])

                #Le héros choisit le méchant.
                v = self.choisirMechant(h2)
                
                #Le héros attaque le méchant.
                if h2.classe == "Mage":
                    h2.attaquerLeGroupe(v, self.vilains[0])
                elif h2.classe == "Chasseur":
                    if fleche > 0:
                        h2.attaquer(v)
                        fleche -= 1
                        print("\n Il ne lui reste que", fleche, "flèches")
                else:
                    h2.attaquer(v)
                
                #Si le méchant est mort, il est retiré de l'équipe.
                if v.isDead():
                    print("\n", v.nom, "est mort...")
                    self.vilains[0].remove(v)
                    break
                
                #Le méchant attaque le héros.
                if v.classe == "Dragon":
                    v.attaquerLeGroupe(h2, self.heros.values())
                else:
                    if h2.classe == "Chasseur" and fleche == 0:
                        v.attaquerChasseurSansFleches(h2)
                    else:
                        v.attaquer(h2)

                #Si le héros est mort, il est retiré de l'équipe.
                if h2.isDead():
                    print("\n", h2.nom, "est mort...")
                    self.heros.pop(h1)
                    break
        
        #S'il n'y a plus d'ennemis dans la vague, les héros gagnent la bataille.
        if len(self.vilains[0]) == 0:
            print("\nLes héros ont gagné la bataille !!!")
            del self.vilains[0]
        
        #Sinon, ce sont les ennemis qui gagnent.
        else:
            print("\nLes méchants ont gagné...")
    
    def choisirMechant(self, hero):
        #Afficher les choix.
        for i, v in enumerate(self.vilains[0]):
            print("\n#",i+1,":",v.nom, end="")
        
        #Demander à l'utilisateur de faire un choix
        while True:
            choix = input("\n=> " + hero.nom + " combat #")
            try:
                index = int(choix)-1
                if index >= 0 and index < len(self.vilains[0]):
                    return self.vilains[0][index]
            except ValueError:
                pass
            print("Saisie non valide, veuillez réessayer.")

    def choisirHeros(self, hero):
        #Afficher les choix.
        for i, h in enumerate(self.heros):
            print("\n#",i+1,":", self.heros[h].nom, end="")

        #Demander à l'utilisateur de faire un choix
        while True:
            choix = input("\n=> " + hero.nom + " soigne #")
            try:
                index = int(choix)-1
                if index >= 0 and index < len(self.heros):
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
        for a in self.vilains[0]:
            print(f"{a.nom : <25}{a.classe : ^20}{a.points_de_vie : ^10}{a.points_dattaque_principaux : ^20}{a.points_dattaque_secondaires : ^20}{a.points_de_guerison : >10}")

Game().run()