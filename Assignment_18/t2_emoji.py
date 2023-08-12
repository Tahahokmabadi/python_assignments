import arcade

SW = 600
SH = 600

arcade.open_window(SW, SH, " Emoji")
arcade.set_background_color(arcade.color.AZURE_MIST)

arcade.start_render()

# draw empty face
arcade.draw_circle_filled(300, 300, 252, arcade.color.ORANGE)
arcade.draw_circle_filled(300, 300, 250, arcade.color.AMBER)

# draw hat
# arcade.draw_circle_filled(300, 575, 200, arcade.color.BLACK)

# draw mouth
arcade.draw_circle_filled(300, 300, 150, arcade.color.BLACK)
arcade.draw_circle_filled(300, 300, 140, arcade.color.WHITE)
# arcade.draw_circle_filled(300, 300, 142, arcade.color.AMBER)
arcade.draw_lrtb_rectangle_filled(150, 450, 450, 300, arcade.color.AMBER)
arcade.draw_lrtb_rectangle_filled(150, 450, 300, 290, arcade.color.BLACK)

# draw eyes
def draw_eye(x, y):
    arcade.draw_circle_filled(x, y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y, 42, arcade.color.BLUE_YONDER)
    arcade.draw_circle_filled(x, y, 25, arcade.color.BLACK_LEATHER_JACKET)
    arcade.draw_circle_filled(x - 15, y + 20, 10, arcade.color.WHITE)

draw_eye(390, 400)
draw_eye(210, 400)


arcade.finish_render()
arcade.run()