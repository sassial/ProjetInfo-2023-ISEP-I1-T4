import random
import Constants as c


"""
The character class is a bit complex as it has to account for every character's name, class, stats, sprite, textures, and animation information.
"""


class personnage:
    def __init__(self, nom, classe,
                 points_de_vie_max, points_dattaque_principaux,
                 points_dattaque_secondaires, points_de_guerison,
                 textures, sprite, orientation, position):
        # Character Name and Class
        self.nom    = nom
        self.classe = classe

        # Character Stats
        self.points_de_vie_max           = points_de_vie_max
        self.points_de_vie               = points_de_vie_max
        self.points_dattaque_principaux  = points_dattaque_principaux
        self.points_dattaque_secondaires = points_dattaque_secondaires
        self.points_de_guerison          = points_de_guerison

        # Character Sprite, Textures, and Animation information
        self.textures = textures
        self.sprite   = sprite

        # Determines the frame of action of the character based on the direction it's facing
        self.orientation = orientation
        self.animation   = 0
        self.frame       = 0

        # Character timer
        self.timer = 0
        self.interval = 0.1

        # Character Sprite Information
        self.sprite.texture  = self.textures[self.orientation][self.animation][self.frame] # The Character's texture is based on its orientation, action, and frame of the action.
        self.sprite.center_x = position
        self.sprite.center_y = c.SPRITE_DEFAULT_ELEVATION + (self.sprite.texture.height)
        if self.classe == "Guerrier" or self.classe == "Chasseur":
            self.sprite.scale = c.SPRITE_DEFAULT_SCALING  - 0.5
        else:
            self.sprite.scale = c.SPRITE_DEFAULT_SCALING
        
    def detendre(self):
        self.animation = 0
        self.frame = 0

    def attaquer(self):
        self.animation = 1
        self.frame = 0

    def courir(self):
        self.animation = 2
        self.frame = 0

    def blesser(self):
        self.animation = 3
        self.frame = 0

    def mourir(self):
        self.animation = 4
        self.frame = 0

    def meditation(self):
        self.animation = 5
        self.frame = 0

    def tourner(self):
        self.orientation = not self.orientation

    def attaquer_une_perso(self, perso):
        if self.classe == "Troll" and perso.classe == "Chasseur":
            perso.points_de_vie -= random.randint(1, self.points_dattaque_principaux-2)
        else:
            perso.points_de_vie -= random.randint(1, self.points_dattaque_principaux)

    def attaquer_chasseur_sans_fleches(self, perso):
        perso.points_de_vie -= 1

    def attaquer_le_groupe(self, cible, equipe):
        for mem in equipe:
            if mem == cible:
                mem.points_de_vie -= random.randint(1, self.points_dattaque_principaux)
            else:
                mem.points_de_vie -= random.randint(1, self.points_dattaque_secondaires)

    def guerir(self, perso):
        perso.points_de_vie += random.randint(1, self.points_de_guerison)