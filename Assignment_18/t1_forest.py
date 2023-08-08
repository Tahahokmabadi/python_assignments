# Forest With Moonlight

#import arcade
import arcade
from random import randrange

#screen size contrast
SW = 600
SH = 600

arcade.open_window(SW, SH, "Forest With Moonlight")
arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
arcade.start_render()

# Draw Ground
arcade.draw_lrtb_rectangle_filled(0, SW, SH / 5 * 1.5, 0, arcade.color.DARK_GREEN)

# Draw Moon
arcade.draw_circle_filled(290, SH - 70, 60, arcade.color.MOONSTONE_BLUE)
arcade.draw_circle_filled(325, SH - 60, 50, arcade.color.DARK_MIDNIGHT_BLUE)

# Draw Cloud
# def draw_cloud():
#     arcade.draw_rectangle_filled(160, SH - 90)
#     arcade.draw_circle()

# draw_cloud()

# Draw Circular Trees
def draw_circular_tree(x, y):
    arcade.draw_rectangle_filled(x, y, 15, 75,arcade.color.BROWN)
    arcade.draw_rectangle_outline(x, y, 15, 75,arcade.color.BLACK)
    arcade.draw_circle_filled(x, y + 20, 35, arcade.color.GREEN)
    arcade.draw_circle_outline(x, y+ 20, 35,arcade.color.BLACK)
# Draw Triangular Trees
def draw_triangular_tree(x, y):
    arcade.draw_rectangle_filled(x, y, 15, 75,arcade.color.CATAWBA)
    arcade.draw_rectangle_outline(x, y, 15, 75,arcade.color.BLACK)
    arcade.draw_triangle_filled(x - 30, y - 5, x + 30 ,y - 5, x, y + 50, arcade.color.DARK_OLIVE_GREEN)
    arcade.draw_triangle_outline(x - 30, y - 5, x + 30 ,y - 5, x, y + 50, arcade.color.BLACK)

for i in range(25 , SW - 25 , 70):
    max_y = 190
    # draw_circular_tree(randrange(i - 30, i + 30), randrange(max_y))
    draw_triangular_tree(randrange(i - 25, i + 25), randrange(max_y))
#Finish program
arcade.finish_render()
arcade.run()
