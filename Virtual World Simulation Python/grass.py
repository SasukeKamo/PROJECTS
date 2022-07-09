from plant import Plant
import pygame

class Grass(Plant):

    COLOR = (51, 204, 0)  # GREEN

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 0
        self.strength = 0

    def get_to_string(self):
        return "Trawa"