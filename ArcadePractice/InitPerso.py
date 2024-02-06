import arcade
import Constants as c
from ClassPerso import personnage


"""
The following code is practically identical for every character, both heroes and villains.

The images which will be used for each character's animations are stored in a list in a list in a list.
This list will be indexed based on the direction the character is facing (orientations), what action it's performing (animation), and which frame of the animation it is in (frame).
To account for orientation, we have to load the textures twice using a for loop, once for each direction the character is facing.

The character's sprite is initialized as a basic sprite of the arcade class.

The character class is finally initialized with each character's name, class, stats, animation information, sprite, and textures for the animation.

At the very end of the code, the initialized characters are stored in a dictionary or list in a list based on whether they're a hero or villain.
"""

def init_perso():
    knight_textures    = [[[arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Knight/png/fire_knight/01_idle/idle_{i}.png",                         x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 9) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Knight/png/fire_knight/08_sp_atk/sp_atk_{i}.png",                     x=50, y=32, width=200, height=96,  flipped_horizontally=flipped) for i in range(1, 19)],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Knight/png/fire_knight/02_run/run_{i}.png",                           x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 9) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Knight/png/fire_knight/10_take_hit/take_hit_{i}.png",                 x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 7) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Knight/png/fire_knight/11_death/death_{i}.png",                       x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 14)]] for flipped in (False, True)]
    knight_sprite      = arcade.Sprite()
    knight             = personnage("Knight le Guerrier", "Guerrier",
                                    10, 5, 0, 0,
                                    knight_textures,
                                    knight_sprite,
                                    c.DEFAULT_HERO_ORIENTATION,
                                    c.position[0][0])

    priestess_textures = [[[arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Priestess/png/01_idle/idle_{i}.png",                                  x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 9) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Priestess/png/10_sp_atk/sp_atk_{i}.png",                              x=50, y=32, width=200, height=96,  flipped_horizontally=flipped) for i in range(1, 33)],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Priestess/png/03_surf/surf_{i}.png",                                  x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 9) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Priestess/png/13_take_hit/take_hit_{i}.png",                          x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 8) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Priestess/png/14_death/death_{i}.png",                                x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 16)]] for flipped in (False, True)]
    priestess_sprite   = arcade.Sprite()
    priestess          = personnage("Priestess le Mage", "Mage",
                                    10, 4, 2, 0,
                                    priestess_textures,
                                    priestess_sprite,
                                    c.DEFAULT_HERO_ORIENTATION,
                                    c.position[0][1])

    ranger_textures    = [[[arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Ranger/animations/PNG/idle/idle_{i}.png",                             x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 13)],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Ranger/animations/PNG/sp_atk/sp_atk_{i}.png",                         x=50, y=32, width=200, height=96,  flipped_horizontally=flipped) for i in range(1, 18)],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Ranger/animations/PNG/run/run_{i}.png",                               x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 11)],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Ranger/animations/PNG/take_hit/take_hit_{i}.png",                     x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 7) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Ranger/animations/PNG/death/death_{i}.png",                           x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 20)]] for flipped in (False, True)]
    ranger_sprite      = arcade.Sprite()
    ranger             = personnage("Ranger le Chasseur", "Chasseur",
                                    10, 3, 0, 0,
                                    ranger_textures,
                                    ranger_sprite,
                                    c.DEFAULT_HERO_ORIENTATION,
                                    c.position[0][2])

    monk_textures      = [[[arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Monk/png/idle/idle_{i}.png",                                          x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 7) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Monk/png/sp_atk/sp_atk_{i}.png",                                      x=50, y=32, width=200, height=96,  flipped_horizontally=flipped) for i in range(1, 26)],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Monk/png/run/run_{i}.png",                                            x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 9) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Monk/png/take_hit/take_hit_{i}.png",                                  x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 7) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Monk/png/death/death_{i}.png",                                        x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 19)],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Heros/Monk/png/meditate/meditate_{i}.png",                                  x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 17)]] for flipped in (False, True)]
    monk_sprite        = arcade.Sprite()
    monk               = personnage("Monk le Guerisseur", "Guerisseur",
                                    10, 1, 0, 2,
                                    monk_textures,
                                    monk_sprite,
                                    c.DEFAULT_HERO_ORIENTATION,
                                    c.position[0][3])

    heros    = {0: knight,
                1: priestess,
                2: ranger,
                3: monk}
    villains = [[],
                [],
                [],
                [],
                []]

    giant_textures     = [[[arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Giant/PNG files/idle/idle_{i}.png",                                 x=12, y=28, width=180, height=100, flipped_horizontally=flipped) for i in range(1, 7) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Giant/PNG files/1_atk/1_atk_{i}.png",                               x=12, y=28, width=180, height=100, flipped_horizontally=flipped) for i in range(1, 15)],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Giant/PNG files/walk/walk_{i}.png",                                 x=12, y=28, width=180, height=100, flipped_horizontally=flipped) for i in range(1, 11)],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Giant/PNG files/take_hit/take_hit_{i}.png",                         x=12, y=28, width=180, height=100, flipped_horizontally=flipped) for i in range(1, 8) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Giant/PNG files/death/death_{i}.png",                               x=12, y=28, width=180, height=100, flipped_horizontally=flipped) for i in range(1, 17)]] for flipped in (False, True)]
    giant_sprite       = arcade.Sprite()
    giant              = personnage("Giant le Frost Guardian", "Giant",
                                    20, 5, 0, 0,
                                    giant_textures,
                                    giant_sprite,
                                    c.DEFAULT_HERO_ORIENTATION,
                                    c.position[1][0])
    villains[3].append(giant)

    demon_textures     = [[[arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Demon/individual sprites/01_demon_idle/demon_idle_{i}.png",         x=24, y=32, width=230, height=128, flipped_horizontally=flipped) for i in range(1, 7) ],
                        [arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Demon/individual sprites/03_demon_cleave/demon_cleave_{i}.png",     x=24, y=32, width=230, height=128, flipped_horizontally=flipped) for i in range(1, 16)],
                        [arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Demon/individual sprites/02_demon_walk/demon_walk_{i}.png",         x=24, y=32, width=230, height=128, flipped_horizontally=flipped) for i in range(1, 13)],
                        [arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Demon/individual sprites/04_demon_take_hit/demon_take_hit_{i}.png", x=24, y=32, width=230, height=128, flipped_horizontally=flipped) for i in range(1, 6) ],
                        [arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Demon/individual sprites/05_demon_death/demon_death_{i}.png",       x=24, y=32, width=230, height=128, flipped_horizontally=flipped) for i in range(1, 23)]] for flipped in (False, True)]
    demon_sprite       = arcade.Sprite()
    demon              = personnage("Dragon le Demon", "Dragon",
                                    15, 6, 2, 0,
                                    demon_textures,
                                    demon_sprite,
                                    c.DEFAULT_HERO_ORIENTATION,
                                    c.position[1][0])
    villains[4].append(demon)

    bandit_textures    = [[[arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Bandit/PNG/idle/idle_{i}.png",                                      x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 9) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Bandit/PNG/2_atk/2_atk_{i}.png",                                    x=50, y=32, width=200, height=96,  flipped_horizontally=flipped) for i in range(1, 19)],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Bandit/PNG/run/run_{i}.png",                                        x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 9) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Bandit/PNG/take_hit/take_hit_{i}.png",                              x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 7) ],
                           [arcade.load_texture(f"ArcadePractice/images/Characters/Enemies/Bandit/PNG/death/death_{i}.png",                                    x=64, y=64, width=160, height=64,  flipped_horizontally=flipped) for i in range(1, 20)]] for flipped in (False, True)]
    for j in range(3):
        for i in range(j+3):
            bandit_sprite = arcade.Sprite()
            bandit        = personnage("Troll Bandit "+str(i), "Troll",
                                    5, 4, 0, 0,
                                    bandit_textures,
                                    bandit_sprite,
                                    c.DEFAULT_VILLAIN_ORIENTATION,
                                    c.position[1][i])
            villains[j].append(bandit)
    
    return(heros, villains)