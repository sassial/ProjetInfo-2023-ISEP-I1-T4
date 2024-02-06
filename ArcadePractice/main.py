import arcade
import arcade.gui
import Constants as c
from StartMenu import MenuDemarrage

def main():
    window = arcade.Window(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
    window.center_window()
    window.show_view(MenuDemarrage())
    arcade.run()

if __name__ == "__main__":
    main()