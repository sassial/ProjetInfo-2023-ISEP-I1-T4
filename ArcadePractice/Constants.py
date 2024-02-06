"""
The constants are fairly self explanatory based on their name.
"""


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Projet Informatique"
LARGEUR_BOUTON = 200
MOVEMENT_SPEED = 4

DEFAULT_HERO_ORIENTATION = 0
DEFAULT_VILLAIN_ORIENTATION = 1

SPRITE_DEFAULT_SCALING = 2.5
SPRITE_DEFAULT_ELEVATION = SCREEN_HEIGHT//8
SPRITE_SCALING_PLAYER = 3


"""
In order to efficiently position the sprites of each character, the screen is divided horizontally by 11,
creating 10 possible positions for each character to be in.

Since there are only 9 characters on the screen at a time, that's more than enough for each character to have its own position,
with a gap between the heroes and villains.
"""
x = SCREEN_WIDTH //11
position = [[x, 2*x, 3*x, 4*x],
            [6*x, 7*x, 8*x, 9*x, 10*x]]