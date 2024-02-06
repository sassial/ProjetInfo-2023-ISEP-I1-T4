import arcade
import arcade.gui
import Constants as c
import dill
from JeuPrincipal import GameView
from InitPerso import init_perso
from BoutonStyle import bouton_style_defaut


class MenuDemarrage(arcade.View): # The Start Menu class is a view and not a window

    def on_show_view(self):
        # Creates a UI Manager to help us draw the GUI Elements
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        
        # Sets the Start Menu's background color and image
        arcade.set_background_color(arcade.color.DARK_SLATE_BLUE)
        self.background_image = arcade.load_texture("ArcadePractice/images/Backgrounds/Other/TitleBackground.png")

        # Sets the background music of the Start Menu
        self.song   = arcade.load_sound("ArcadePractice/sound/music/start.mp3")
        self.player = arcade.play_sound(self.song)

        # Creates the title and subtitle on the Start Menu
        titre     = arcade.gui.UILabel(text="Trolls et Dragons",    font_size=48, font_name="calibri", text_color=arcade.color.BLACK, bold=True, align="center")
        soustitre = arcade.gui.UILabel(text="Créé par Ripple Inc.", font_size=12, font_name="calibri", text_color=arcade.color.BLACK, bold=True, align="center")

        # Creates multiple buttons that are identical in appearance but labeled differently
        textes_boutons = ["Nouveau Jeu", "Quitter"]
        bouton         = [(arcade.gui.UIFlatButton(text=text, width=c.LARGEUR_BOUTON, style=bouton_style_defaut))for text in textes_boutons]

        # Creates a BoxGroup to contain all the UI Elements
        self.boite = arcade.gui.UIBoxLayout()

        # Adds the title, subtitle, and all the buttons to the BoxGroup
        self.boite.add(titre)
        self.boite.add(soustitre)
        [self.boite.add(b) for b in bouton]

        # Assigns each Start Menu button a function based on its label
        bouton[0].on_click = self.on_click_nj
        bouton[1].on_click = self.on_click_quitter

        # Assigns a position to the BoxGroup right in the middle of the screen
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.boite))

    # Draws all the in-game objects
    def on_draw(self):
        self.clear() # Clears any pre-existing elements
        arcade.start_render()
        arcade.draw_texture_rectangle(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2, c.SCREEN_WIDTH, c.SCREEN_HEIGHT, self.background_image)
        self.manager.draw() # The UI Manager draws all the UI Elements
    
    # Function assigned to the New Game button
    def on_click_nj(self, event):
        self.manager.clear() # Clears all UI elements including the title, subtitle, and buttons
        arcade.stop_sound(self.player) # Stops the background music
        heros, villains = init_perso()
        game_view = GameView(self, heros, villains) # Initializes the Game's view
        game_view.setup() # Sets the Game View up
        self.window.show_view(game_view) # Shows the Game's view in the window
    
    # Function assigned to the Quit Game button
    def on_click_quitter(self, event):
        arcade.exit() # Exits the Game