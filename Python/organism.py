import random

from point import Point
import pygame
from direction import Direction


class Organism:

    def __init__(self, world, x, y):
        self.position = Point(x, y)
        self.world = world
        self.age = self.world.round_number
        self.strength = None
        self.initiative = None
        self.direction = None
        self.is_dead = False

    def draw(self, position_x, position_y):
        pygame.draw.rect(self.world.screen, self.COLOR, (
            pygame.Rect(self.position.y * self.world.organism_width, self.position.x * self.world.organism_height, self.world.organism_width - 2,
                        self.world.organism_height - 2)))

    def make_move(self):
        if self.direction == Direction.UP and 0 < self.position.x:
            self.position.x -= 1
        elif self.direction == Direction.DOWN and self.position.x < self.world.get_height() - 1:
            self.position.x += 1
        elif self.direction == Direction.LEFT and 0 < self.position.y:
            self.position.y -= 1
        elif self.direction == Direction.RIGHT and self.position.y < self.world.get_width() - 1:
            self.position.y += 1

    def get_collider(self):
        return self.world.board[self.position.x][self.position.y]

    def get_x(self):
        return self.position.x

    def get_y(self):
        return self.position.y

    def get_strength(self):
        return self.strength

    # clears current position before move
    def undo_position(self):
        self.world.board[self.position.x][self.position.y] = None

    def get_random_direction(self):
        return random.choice([Direction.DOWN, Direction.UP, Direction.LEFT, Direction.RIGHT])

    def action(self):
        self.undo_position()
        self.direction = self.get_random_direction()
        self.make_move()

    def collision(self, collider):
        pass

    def get_age(self):
        return self.age

    def get_initiative(self):
        return self._initiative
