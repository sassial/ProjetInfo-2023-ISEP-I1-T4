import arcade
import arcade.gui
import Constants as c
from BoutonStyle import bouton_style_defaut
from ReturnToMainMenu import RetournerMenu
from PauseMenu import MenuPause


class GameView(arcade.View):
    def __init__(self, menu_demarrage, heros, villains):
        super().__init__() # Initializes the view
        self.menu_demarrage = menu_demarrage # Assigns the Game View to a class variable
        self.heros = heros.copy()
        self.villains = villains.copy()

        # Creates a UI Manager to help us draw the GUI Elements
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Creates multiple backgrounds for different combat scenarios
        arcade.set_background_color(arcade.color.CASTLETON_GREEN)
        self.background_image = [[arcade.load_texture(f"ArcadePractice/images/Backgrounds/BackgroundRuins/PNG/background{i}.png")     for i in range(1, 5)],
                                 [arcade.load_texture(f"ArcadePractice/images/Backgrounds/BackgroundMountains/PNG/background{i}.png") for i in range(1, 4)],
                                 [arcade.load_texture(f"ArcadePractice/images/Backgrounds/BackgroundHills/_PNG/background{i}.png")    for i in range(1, 5)],
                                 [arcade.load_texture(f"ArcadePractice/images/Backgrounds/BackgroundRuins/PNG/background{i}.png")     for i in range(1, 5)],
                                 [arcade.load_texture(f"ArcadePractice/images/Backgrounds/BackgroundHills/_PNG/background{i}.png")    for i in range(1, 5)]]

        self.song = arcade.load_sound("ArcadePractice/sound/music/battle.mp3")
        self.player = arcade.play_sound(self.song, looping=True)

        self.cover_transparency = 255
        self.healing = False
        self.victory = False
        self.bossfight = False
        self.total_victory = False
        
        self.boutons = [(arcade.gui.UIFlatButton(text="Bataille",           width=c.LARGEUR_BOUTON, style=bouton_style_defaut)),
                        (arcade.gui.UIFlatButton(text="Guerir",             width=c.LARGEUR_BOUTON, style=bouton_style_defaut)),
                        (arcade.gui.UIFlatButton(text="Effacer Villains",   width=c.LARGEUR_BOUTON, style=bouton_style_defaut)),
                        (arcade.gui.UIFlatButton(text="Effacer Heros",      width=c.LARGEUR_BOUTON, style=bouton_style_defaut)),
                        (arcade.gui.UIFlatButton(text="Pause",              width=c.LARGEUR_BOUTON, style=bouton_style_defaut))]
        
        self.boutons[0].on_click = self.on_click_bataille
        self.boutons[1].on_click = self.on_click_guerir
        self.boutons[2].on_click = self.on_click_effv
        self.boutons[3].on_click = self.on_click_effh
        self.boutons[4].on_click = self.on_click_pause

        self.boite = [arcade.gui.UIBoxLayout(),
                      arcade.gui.UIBoxLayout(),
                      arcade.gui.UIBoxLayout()]
        
        self.boite[0].add(self.boutons[0])
        self.boite[0].add(self.boutons[1])
        self.boite[1].add(self.boutons[2])
        self.boite[1].add(self.boutons[3])
        self.boite[2].add(self.boutons[4])
        
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="left",  anchor_y="top",    child=self.boite[0]))
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="right", anchor_y="top",    child=self.boite[1]))
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="right", anchor_y="bottom", child=self.boite[2]))

    def setup(self):
        self.main_hero = 0
        self.main_villain = 0

        self.fleche = 5 

        self.reorder_heros()

        self.timer = 0
        self.interval = 0.1

    def on_draw(self):
        self.clear()
        arcade.start_render()

        # Draws the background
        for image in self.background_image[len(self.villains)-1]:
            arcade.draw_texture_rectangle(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, image)
        
        if not self.healing:
            if len(self.villains)>0:
                for v in self.villains[0]:
                    v.sprite.draw()
                    if v.points_de_vie > 0:
                        self.draw_health_bar(v)
        
        for h1, h2 in self.heros.items():
            h2.sprite.draw()
            if h2.points_de_vie > 0:
                self.draw_health_bar(h2)

        # Draws the UI Elements
        self.manager.draw()

        # Draws a fading Start Menu background for aesthetic purposes
        if self.cover_transparency>0:
            arcade.draw_texture_rectangle(c.SCREEN_WIDTH//2, c.SCREEN_HEIGHT//2, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, arcade.load_texture("ArcadePractice/images/Backgrounds/Other/TitleBackground.png"), 0, self.cover_transparency)

    def on_update(self, delta_time):
        keys_to_remove = []
        self.timer += delta_time

        if self.cover_transparency > 0:
            if self.cover_transparency > 225:
                self.cover_transparency -= 1
            else:
                self.cover_transparency -= 5
        
        if len(self.heros)<=0:
            self.window.show_view(RetournerMenu(self, self.menu_demarrage))
        
        if len(self.villains)>0 and len(self.villains[0])==0:
            self.victory = True
            self.on_click_pause("Victory")
            self.victory = False
            del self.villains[0]
            if len(self.villains)==0:
                self.total_victory = True
                self.window.show_view(RetournerMenu(self, self.menu_demarrage))
            else:
                self.reorder_villains()
                for h in self.heros.values():
                    h.points_dattaque_principaux += 1
                    if h.classe == "Mage":
                        h.points_dattaque_secondaires += 1
                    h.points_de_vie = h.points_de_vie_max
                self.fleche = 5
                
        for h1, h2 in self.heros.items():
            h2.timer += delta_time

            if h2.animation == 2:
                if h2.classe != "Guerisseur":
                    h2.sprite.center_y = c.SPRITE_DEFAULT_ELEVATION + (h2.sprite.height//2)
                else:
                    h2.sprite.center_y = c.SPRITE_DEFAULT_ELEVATION + (h2.sprite.height//2.7)
                
                if h2.orientation == 0:
                    h2.sprite.center_x += c.MOVEMENT_SPEED
                    if h2.sprite.center_x >= c.position[1][0] - c.x:
                        h2.sprite.center_x = c.position[1][0] - c.x - 1
                        h2.attaquer()
                else:
                    h2.sprite.center_x -= c.MOVEMENT_SPEED
                    if h2.sprite.center_x <= c.position[0][3]:
                        h2.detendre()
                        h2.tourner()
            else:
                h2.sprite.bottom = c.SPRITE_DEFAULT_ELEVATION

            if h2.timer > h2.interval:
                h2.frame = (h2.frame + 1)%(len(h2.textures[h2.orientation][h2.animation]))
                h2.sprite.texture = h2.textures[h2.orientation][h2.animation][h2.frame]
                h2.sprite.set_hit_box(h2.sprite.texture.hit_box_points)
                if (h2.frame == len(h2.textures[h2.orientation][h2.animation])-1) and (h2.animation != 2):
                    if h2.animation==1:
                        if h2.classe == "Mage":
                            h2.attaquer_le_groupe(self.villains[0][self.main_villain], self.villains[0])
                            for v in self.villains[0]:
                                v.blesser()
                        elif h2.classe == "Chasseur":
                            if self.fleche > 0:
                                h2.attaquer_une_perso(self.villains[0][self.main_villain])
                                self.villains[0][self.main_villain].blesser()
                                self.fleche -= 1
                            else:
                                pass
                        else:
                            h2.attaquer_une_perso(self.villains[0][self.main_villain])
                            self.villains[0][self.main_villain].blesser()
                        h2.detendre()
                    elif h2.animation==3:
                        if h2.points_de_vie <= 0:
                            h2.mourir()
                        else:
                            h2.tourner()
                            h2.courir()
                    elif h2.animation==4:
                        keys_to_remove.append(h1)
                    else:
                        h2.detendre()
                h2.timer -= h2.interval

            h2.sprite.update()
        
        for k in keys_to_remove:
            del self.heros[k]

        if len(self.villains)>0:
            for v in self.villains[0]:
                v.timer += delta_time
                v.sprite.bottom = c.SPRITE_DEFAULT_ELEVATION

                if v.timer > v.interval:
                    v.frame = (v.frame + 1)%(len(v.textures[v.orientation][v.animation]))
                    v.sprite.texture = v.textures[v.orientation][v.animation][v.frame]
                    v.sprite.set_hit_box(v.sprite.texture.hit_box_points)
                    if (v.frame == len(v.textures[v.orientation][v.animation])-1) and (v.animation != 2):
                        if v.animation == 1:
                            if v.classe == "Dragon":
                                v.attaquer_le_groupe(self.heros[self.main_hero], self.heros.values())
                                [h.blesser() for h in self.heros.values()]
                            else:
                                if self.heros[self.main_hero].classe == "Chasseur" and self.fleche == 0:
                                    v.attaquer_chasseur_sans_fleches(self.heros[self.main_hero])
                                else:
                                    v.attaquer_une_perso(self.heros[self.main_hero])
                                self.heros[self.main_hero].blesser()
                            v.detendre()
                        elif v.animation == 3:
                            if v.points_de_vie <= 0:
                                v.mourir()
                            else:
                                if v == self.villains[0][self.main_villain]:
                                    v.attaquer()
                                else:
                                    v.detendre()
                        elif v.animation == 4:
                            self.villains[0].remove(v)
                            self.main_villain = 0
                            self.reorder_villains()
                            self.heros[self.main_hero].orientation = 1
                            self.heros[self.main_hero].courir()
                        else:
                            v.detendre()
                    v.timer -= v.interval

                v.sprite.update()

    def on_mouse_press(self, x, y, button, modifiers):
        if button==arcade.MOUSE_BUTTON_LEFT:
            # Any hero that is clicked on becomes the main hero and moves to the front of their party
            for h1, h2 in self.heros.items():
                if h2.sprite.collides_with_point((x, y)):
                    self.main_hero = h1
                    self.reorder_heros()
                    break
            
            # Any villain that is clicked on becomes the main villain and moves to the front of the wave
            for v in self.villains[0]:
                if v.sprite.collides_with_point((x, y)):
                    self.main_villain = self.villains[0].index(v)
                    self.reorder_villains()
                    break

    def reorder_heros(self):
        i = 0
        for h1, h2 in self.heros.items():
            if not self.healing:
                if h2 == self.heros[self.main_hero]:
                    self.heros[self.main_hero].sprite.set_position(c.position[0][3], c.SPRITE_DEFAULT_ELEVATION + (self.heros[self.main_hero].sprite.texture.height))
                    self.heros[self.main_hero].sprite.set_hit_box(self.heros[self.main_hero].sprite.texture.hit_box_points)
                else:
                    h2.sprite.set_position(c.position[0][2-i], c.SPRITE_DEFAULT_ELEVATION + (h2.sprite.texture.height))
                    h2.sprite.set_hit_box(h2.sprite.texture.hit_box_points)
                    i += 1
            else:
                if h2.classe == "Guerisseur":
                    h2.sprite.set_position(c.position[0][3], c.SPRITE_DEFAULT_ELEVATION + (self.heros[self.main_hero].sprite.texture.height))
                    h2.sprite.set_hit_box(self.heros[self.main_hero].sprite.texture.hit_box_points)
                elif h2 == self.heros[self.main_hero]:
                    self.heros[self.main_hero].orientation = 1
                    self.heros[self.main_hero].sprite.set_position(c.position[1][0], c.SPRITE_DEFAULT_ELEVATION + (self.heros[self.main_hero].sprite.texture.height))
                    self.heros[self.main_hero].sprite.set_hit_box(self.heros[self.main_hero].sprite.texture.hit_box_points)
                else:
                    h2.sprite.set_position(c.position[1][i+1], c.SPRITE_DEFAULT_ELEVATION + (h2.sprite.texture.height))
                    h2.sprite.set_hit_box(h2.sprite.texture.hit_box_points)
                    i += 1
    
    def reorder_villains(self):
        i = 0
        for v in self.villains[0]:
            if v == self.villains[0][self.main_villain]:
                self.villains[0][self.main_villain].sprite.set_position(c.position[1][0], c.SPRITE_DEFAULT_ELEVATION + (self.villains[0][self.main_villain].sprite.texture.height))
                self.villains[0][self.main_villain].sprite.set_hit_box(self.villains[0][self.main_villain].sprite.texture.hit_box_points)
            else:
                v.sprite.set_position(c.position[1][i+1], c.SPRITE_DEFAULT_ELEVATION + (v.sprite.texture.height))
                v.sprite.set_hit_box(v.sprite.texture.hit_box_points)
                i += 1
        
    def on_click_bataille(self, event):
        if not self.healing:
            if (self.fleche>0) or (self.heros[self.main_hero].classe != "Chasseur"):
                self.heros[self.main_hero].courir()
        else:
            self.healing = not self.healing
            for h in self.heros.values():
                if h.classe != "Guerisseur":
                    h.orientation = (h.orientation+1)%2
            self.main_hero = 1
            self.reorder_heros()

    def on_click_guerir(self, event):
        if not self.healing:
            self.healing = not self.healing
            for h in self.heros.values():
                if h.classe != "Guerisseur":
                    h.orientation = (h.orientation+1)%2
            self.main_hero = 1
            self.reorder_heros()
        else:
            for h in self.heros.values():
                if h.classe == "Guerisseur":
                    h.animation = 5
                    h.guerir(self.heros[self.main_hero])
    
    def on_click_effv(self, event):
        for v in self.villains[0]:
            v.points_de_vie = 0
            v.animation = 3

    def on_click_effh(self, event):
        for h in self.heros.values():
            h.points_de_vie = 0
            h.animation = 3
    
    def on_click_pause(self, event):
        self.window.show_view(MenuPause(self))
        
    def draw_health_bar(self, perso):
        # Give each Troll Bandit a unique health bar color to differentiate them
        color_dict = {"Troll Bandit 0": arcade.color.VIVID_SKY_BLUE,
                      "Troll Bandit 1": arcade.color.TURQUOISE_BLUE,
                      "Troll Bandit 2": arcade.color.BABY_BLUE,
                      "Troll Bandit 3": arcade.color.AIR_SUPERIORITY_BLUE,
                      "Troll Bandit 4": arcade.color.BALL_BLUE}
        color = color_dict.get(perso.nom, arcade.color.GREEN) # Set GREEN as default health bar color for non Troll Bandit characters

        if perso.animation == 0 or perso.animation == 3: # Only display health bar when character is idle or hurt
            # Variables used for generating the health bar
            bar_half_width = perso.sprite.texture.width//3
            bar_height = 10
            sprite_height = perso.sprite.center_y + perso.sprite.texture.height//2
            
            # Calculate width of health bar fill based on current health
            health_width   = (2*bar_half_width) * (perso.points_de_vie / perso.points_de_vie_max)

            # Calculate coordinates for health bar
            left          = perso.sprite.center_x - bar_half_width
            right_filled  = left + health_width
            right_outline = left + 2*bar_half_width
            bottom        = sprite_height + 5
            top           = bottom + bar_height

            # Calculate coordinates and values for health values
            value_width = right_outline-left
            value_text = str(perso.points_de_vie)+"/"+str(perso.points_de_vie_max)
            value_center = left+value_width//2
            value_color = arcade.color.BLACK

            # Calculate coordinates and values for arrow quanitity
            fleche_text = str(self.fleche)+" fleche(s) restant"

            # Draw health bar and health values
            arcade.draw_lrtb_rectangle_filled(left,  right_filled,  top, bottom, color)
            arcade.draw_lrtb_rectangle_outline(left, right_outline, top, bottom, arcade.color.WHITE, 1)
            arcade.draw_text(text=value_text, start_x=value_center, start_y=bottom, color=value_color, font_size=bar_height-2, width=value_width, bold=True, anchor_x="center")
            if perso.classe == "Chasseur":
                arcade.draw_text(text=fleche_text, start_x=value_center, start_y=top, color=arcade.color.WHITE, font_size=12, bold=True, anchor_x="center", anchor_y="bottom")