import random

class personnage:
    #tous les membres de cette classe sont initialisés avec les attributs spécifiques "nom", "points de vie", "points d'attaque", 
    def __init__(self, nom, classe, points_de_vie, points_dattaque_principaux, points_dattaque_secondaires, points_de_guerison):
        self.nom = nom
        self.classe = classe
        self.points_de_vie = points_de_vie
        self.points_dattaque_principaux = points_dattaque_principaux
        self.points_dattaque_secondaires = points_dattaque_secondaires
        self.points_de_guerison = points_de_guerison

    #chaque membre de cette classe possède une fonction qui lui permet d'attaquer un autre membre de cette classe
    def attaquer(self, personnage):
        x = personnage.points_de_vie
        print("\n", self.nom, "a attaqué", personnage.nom, "...")
        if self.classe == "Troll" and personnage.classe == "Chasseur":
            personnage.points_de_vie -= random.randint(1, self.points_dattaque_principaux-2)
        else:
            personnage.points_de_vie -= random.randint(1, self.points_dattaque_principaux)
        if personnage.points_de_vie < 0:
            print("\n", self.nom, "a fait", x-personnage.points_de_vie, "degats!", personnage.nom, "a 0 points de vie restant...")
        else:
            print("\n", self.nom, "a fait", x-personnage.points_de_vie, "degats!", personnage.nom, "a", personnage.points_de_vie, "points de vie restant...")
    
    def attaquerChasseurSansFleches(self, personnage):
        print("\n", self.nom, "a attaqué", personnage.nom, "...")
        personnage.points_de_vie -= 1
        print("\n", self.nom, "a fait 1 degat!", personnage.nom, "a", personnage.points_de_vie, "points de vie restant...")


    #chaque membre de cette classe possède une fonction qui lui permet d'attaquer tout ses adversaires
    def attaquerLeGroupe(self, cible, equipe):
        for mem in equipe:
            x = mem.points_de_vie
            if mem == cible:
                print("\n", self.nom, "a attaqué", cible.nom, "...")
                mem.points_de_vie -= random.randint(1, self.points_dattaque_principaux)
            else:
                print("\n", self.nom, "a attaqué", mem.nom, "...")
                mem.points_de_vie -= random.randint(1, self.points_dattaque_secondaires)
            if mem.points_de_vie < 0:
                print("\n", self.nom, "a fait", x-mem.points_de_vie, "degats!", mem.nom, "a 0 points de vie restant...")
            else:
                print("\n", self.nom, "a fait", x-mem.points_de_vie, "degats!", mem.nom, "a", mem.points_de_vie, "points de vie restant...")

    #chaque membre de cette classe possède une fonction qui lui permet de guérir un autre membre de cette classe
    def guerir(self, personnage):
        x = personnage.points_de_vie
        print("\n", self.nom, "a guéri", personnage.nom, "...")
        personnage.points_de_vie += self.points_de_guerison
        print("\n", self.nom, "a soigné", personnage.nom, "de", personnage.points_de_vie-x, "points de vie!", personnage.nom, "a", personnage.points_de_vie, "points de vie restant...")

    #Cette classe possède une fonction particulière qui vérifie si les points de vie du membre sont égaux ou inférieurs à zéro
    def isDead(self):
        return self.points_de_vie <= 0;
