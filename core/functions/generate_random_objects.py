import random
from entities.objects import squares_in_game, squares
import pygame
import sys

counter = 0

def generate_random_objects():
    global counter
    counter += 1
    if counter < len(squares):
        squares_in_game.extend([
            squares[counter] 
        ])
        