from microbit import *
from random import randint

# Directions
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Taille de l'ecran
screen_size = 5

# Intensite lumineuse pour le serpent
SN_LIGHT = 9
# Intensite lumineuse pour la pomme
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
    # TODO: Change la direction en fonction des boutons A, B et de la 
    # direction donnee

    # Si on appuie sur le bouton A, on tourne a gauche.
    # Si on appuie sur le bouton B, on tourne a droite.
    return UP


def new_head(snake, dir):
    """
    Return the tuple (x, y) of the new head
    """
    # TODO: Choisi une nouvelle direction en fonction de la direction donnee
    # et de la tete
    return (0, 0)


# La tete du serpent est le premier element de la liste
# La queue est le dernier element
snake = [(2, 2)]
snake_len = 1
dir = UP
apple = None

# Tant que le serpent ne rempli pas toutes les cases
while snake_len < 25:

    # TODO: Si la pomme n'existe pas (None), choisi une place aleatoire pour
    # la pomme

    # TODO: Change la direction

    # TODO: Trouve la nouvelle tete du serpent

    # TODO: Ajoute la nouvelle tete au serpent (insere la tete en position 0)

    # TODO: Si la nouvelle tete est sur la pomme, agrandi la taille du serpent
    # Et retire la pomme de la grille (None)


    display.clear()
    # TODO: Affiche la pomme
    # TODO: Affiche le serpent
    sleep(500)


# TODO: Affiche un message de victoire/defaire en fonction du score (25 = gagne)
