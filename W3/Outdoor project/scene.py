# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from turtle import width
from draw2d import \
    draw_horizontal_gradient, draw_vertical_gradient, start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_moon(canvas, 400, 100)


    repeat_clouds = 0
    for i in range(10):
        if repeat_clouds < 10:
            draw_clouds(canvas, 150, 5)
            repeat_clouds += 1



    repeat_clouds = 0
    for i in range(3):
        if repeat_clouds < 3:
            draw_clouds(canvas, 350, 40)
            repeat_clouds += 1


    draw_ground(canvas, scene_width, scene_height)

    repeat = 0
    x0 = -20
    for i in range(scene_width):
        if repeat < scene_width:
            draw_bushes(canvas, x0)
            repeat += 1
            x0 += 30


    repeat = 0
    x0 = -20
    for i in range(scene_width):
        if repeat < scene_width:
            draw_bushes(canvas, x0)
            repeat += 1
            x0 += 30

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_grid(canvas, width, height, interval, color="blue"):
    # Draw a vertical line at every x interval.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    # Draw a horizontal line at every y interval.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)

# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas, scene_width, scene_height):
    color1 = [252, 106, 56]
    color2 = [50, 51, 77]
    draw_vertical_gradient(canvas, 0, 0, color1, scene_width, scene_height, color2)

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 4, width=0, fill="#6B2F07")

    # Pine tree background.
    tree_center_x = 150
    tree_bottom = 100
    tree_height = 180
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Pine tree 2.
    tree_center_x = 130
    tree_bottom = 100
    tree_height = 180
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)


    # Pine tree 3.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Pine tree 4.
    tree_center_x = 90
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    # Pine tree foreground.
    tree_center_x = 210
    tree_bottom = 60
    tree_height = 250
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

def draw_pine_tree(canvas, center_x, bottom, height):
    """Draw a single pine tree.
    Parameters
        canvas: The canvas where this function
            will draw a pine tree.
        center_x, bottom: The x and y location in pixels where
            this function will draw the bottom of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")

def draw_moon(canvas, moon_center, moon_diameter):
    draw_oval(canvas, moon_center, moon_center-50, moon_center+moon_diameter, moon_center+moon_diameter-50, outline="white", fill="white")

def draw_bushes(canvas, x0):
    diameter = 40
    y1 = random.randint(0, 100)
    draw_oval(canvas, x0, -20, x0+diameter, y1+diameter, outline="green", fill="darkgreen")

def draw_clouds(canvas, level, diameter):
    x0 = random.randint(100, 800)
    x1 = random.randint(x0+10, x0+300)

    y1 = random.randint(level+10, level+50)
    draw_oval(canvas, x0, level, x1+diameter, y1+diameter, outline="lightgrey", fill="lightgrey")

# Call the main function so that
# this program will start executing.
main()