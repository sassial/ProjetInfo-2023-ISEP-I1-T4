import arcade
import arcade.gui
import Constants as c
import dill
from BoutonStyle import bouton_style_defaut


class MenuPause(arcade.View): # The Start Menu class is a view and not a window
    def __init__(self, game_view): # Receives the Game View as an input parameter upon initialization
        super().__init__() # Initializes the view
        self.game_view = game_view # Assigns the Game View to a class variable

    def on_show_view(self):
        # Creates a UI Manager to help us draw the GUI Elements
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Pauses the Game View's background music and plays the victory music if during a victory
        self.song   = arcade.load_sound("ArcadePractice/sound/music/victory.mp3")
        self.game_view.player.pause()
        if not self.game_view.victory:
            self.player = arcade.play_sound(self.song, volume=0)
        else:
            self.game_view.player.seek(0)
            self.player = arcade.play_sound(self.song)
        
        # Creates the Pause Menu's title
        if not self.game_view.victory:
            titre     = arcade.gui.UILabel(text="Pause", font_size=48, font_name="calibri", bold=True, align="center")
            soustitre = arcade.gui.UILabel(text="",      font_size=12, font_name="calibri", text_color=arcade.color.BLACK, bold=True, align="center")
        else:
            titre     = arcade.gui.UILabel(text="Victoire !", font_size=48, font_name="calibri", bold=True, align="center")
            soustitre = arcade.gui.UILabel(text="Les héros ont progressé en niveau et ont augmenté leur attaque", font_size=12, font_name="calibri", text_color=arcade.color.BLACK, bold=True, align="center")
        
        # Creates multiple buttons that are identical in appearance but labeled differently
        textes_boutons = ["Continuer le Jeu", "Quitter"]
        bouton         = [(arcade.gui.UIFlatButton(text=text, width=c.LARGEUR_BOUTON, style=bouton_style_defaut))for text in textes_boutons]

        # Creates a BoxGroup to contain all the UI Elements
        self.boite = arcade.gui.UIBoxLayout()

        # Adds the title and all the buttons to the BoxGroup
        self.boite.add(titre)
        self.boite.add(soustitre)
        [self.boite.add(b) for b in bouton]

        # Assigns each Pause Menu button a function based on its label
        bouton[0].on_click = self.on_click_cj
        bouton[1].on_click = self.on_click_quitter

        # Assigns a position to the BoxGroup right in the middle of the screen
        self.manager.add(arcade.gui.UIAnchorWidget(anchor_x="center_x", anchor_y="center_y", child=self.boite))

    # Draws all the in-game objects
    def on_draw(self):
        self.manager.draw() # The UI Manager draws all the UI Elements
        
    # Function assigned to the New Game button
    def on_click_cj(self, event):
        self.clear() # Clears any pre-existing elements
        self.manager.clear() # Clears all UI elements including the title and buttons
        self.player.pause() # Stops the victory music
        self.game_view.player.play() # Resumes the Game View's background music
        self.window.show_view(self.game_view) # Switches back to the Game View
    
    # Function assigned to the Quit Game button
    def on_click_quitter(self, event):
        arcade.exit() # Exits the Game