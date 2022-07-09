from animal import Animal
import pygame
import os


class Human(Animal):

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 4
        self.strength = 5
        self.is_ability_active = False
        self.cooldown = 0

        self.IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images/", "humanPNG.png")),
                                             (self.world.organism_width, self.world.organism_height))

    def action(self):
        self.undo_position()
        self.make_move()

    def change_direction(self, direction):
        self.direction = direction

    def draw(self, position_x, position_y):
        self.world.screen.blit(self.IMAGE, (self.position.y * self.world.organism_width, self.position.x * self.world.organism_height))

    def __repr__(self):
        return 'Human'

    def get_to_string(self):
        return "Czlowiek"