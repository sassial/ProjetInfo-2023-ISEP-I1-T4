import arcade
import arcade.gui
import Constants as c
import dill
from BoutonStyle import bouton_style_defaut


class RetournerMenu(arcade.View): # The Start Menu class is a view and not a window
    def __init__(self, game_view, menu_demarrage): # Receives the Game View and Start Menu as an input parameter upon initialization
        super().__init__() # Initializes the view
        self.game_view = game_view # Assigns the Game View to a class variable
        self.menu_demarrage = menu_demarrage

    def on_show_view(self):
        # Creates a UI Manager to help us draw the GUI Elements
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Sets the background music of the Return to Main Menu
        arcade.set_background_color(arcade.color.DARK_SLATE_BLUE)
        if not self.game_view.total_victory:
            self.background_image = arcade.load_texture("ArcadePractice\images\Backgrounds\Other\DeathScreen.jpg")
        else:
            self.background_image = arcade.load_texture("ArcadePractice\images\Backgrounds\Other\IntroScreen.jpg")

        # Pauses the Game View's background music and plays the victory music if during a victory
        self.death_song = arcade.load_sound("ArcadePractice/sound/music/death.mp3")
        self.total_victory_song = arcade.load_sound("ArcadePractice/sound/music/gamecomplete.mp3")
        self.game_view.player.pause()
        if not self.game_view.total_victory:
            self.player = arcade.play_sound(self.death_song)
        else:
            self.player = arcade.play_sound(self.total_victory_song)

        # Creates the Pause Menu's title
        if not self.game_view.total_victory:
            titre     = arcade.gui.UILabel(text="Vous êtes tous morts...", font_size=48, font_name="calibri", bold=True, align="center")
            soustitre = arcade.gui.UILabel(text="Retourner au menu principal pour charger la dernière partie sauvegardée.",
                                           font_size=12, font_name="calibri", bold=True, align="center")
        else:
            titre     = arcade.gui.UILabel(text="Victoire Totale !", font_size=48, font_name="calibri", bold=True, align="center")
            soustitre = arcade.gui.UILabel(text="Vous avez gagné le jeu",
                                           font_size=12, font_name="calibri", text_color=arcade.color.BLACK, bold=True, align="center")

        # Creates multiple buttons that are identical in appearance but labeled differently
        textes_boutons = ["Retour au Menu Principal", "Quitter"]
        bouton         = [(arcade.gui.UIFlatButton(text=text, width=c.LARGEUR_BOUTON, style=bouton_style_defaut))for text in textes_boutons]

        # Creates a BoxGroup to contain all the UI Elements
        self.boite = arcade.gui.UIBoxLayout()

        # Adds the title and all the buttons to the BoxGroup
        self.boite.add(titre)
        self.boite.add(soustitre)
        [self.boite.add(b) for b in bouton]

        # Assigns each Pause Menu button a function based on its label
        bouton[0].on_click = self.on_click_ramp
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
    def on_click_ramp(self, event):
        self.clear() # Clears any pre-existing elements
        self.manager.clear() # Clears all UI elements including the title and buttons
        self.player.pause() # Stops the background music
        self.window.show_view(self.menu_demarrage)

    # Function assigned to the Quit Game button
    def on_click_quitter(self, event):
        arcade.exit() # Exits the Game