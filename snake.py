from microbit import *

# Directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Screen size
screen_size = 5

# Snake light intensity
SN_LIGHT = 9
# Apple light intensity
APP_LIGHT = 5


def draw_snake(snake):
    """
    Draw the snake on the screen
    """
    for i in range(screen_size):
        for j in range(screen_size):
            display.set_pixel(j, i, SN_LIGHT)

def new_direction(dir):
    """
    Choose the new direction
    """
    # TODO : Change the direction if button A or B is pressed



snake = [(2, 2)]
snake_len = 1
dir = UP
apple = None

while snake_len:

    # TODO: Change the direction

    # TODO: Find the new head of the snake

    # TODO: Add the new head to the snake

    # TODO: If new head touch the apple, increase the length

    # TODO: Choose a new coordinates for the apple

    display.clear()
    # TODO: Display the apple
    # TODO: Display the snake
    sleep(500)
