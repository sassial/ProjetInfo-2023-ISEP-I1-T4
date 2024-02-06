import arcade
import arcade.gui


"""
The default button style has parameters that are fairly self explanatory based on their name.
"""
bouton_style_defaut = {
            "font_name":    ("calibri", "arial"),
            "font_size":    15,
            "font_color":   arcade.color.WHITE,
            "border_width": 2,
            "border_color": arcade.color.WHITE,
            "bg_color":     arcade.color.BLACK,

            # Used when the button is pressed
            "bg_color_pressed":     arcade.color.WHITE,
            "border_color_pressed": arcade.color.BLACK,  # Also used when hovering over the button
            "font_color_pressed":   arcade.color.BLACK,
        }