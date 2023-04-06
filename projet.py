from initPerso import heros, vilains
from menus import menuPrincipal, menuSauvegarde
from combat import bataille

class Game:
    def __init__(self):
        self.vilains = vilains
        self.heros = heros

    def run(self):
        self.menu()
        # Les héros doivent combattre tout les vagues d'ennemis pour terminer le jeu.
        for i in range(len(self.vilains)):
            self.batailleVagues()
            self.sauvegarde()

    def menu(self):
        self.heros, self.vilains = menuPrincipal(self.heros, self.vilains)

    def batailleVagues(self):
        bataille(self.heros, self.vilains)

    def sauvegarde(self):
        menuSauvegarde(self.heros, self.vilains)

Game().run()