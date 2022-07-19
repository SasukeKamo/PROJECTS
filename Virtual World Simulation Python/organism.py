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
        self.is_animal = False
        self.has_collision_power = False
        self.has_action_power = False
        self.multiplication_chance = 20

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
        self.age += 1

    def collision(self, collider):
        pass

    def get_age(self):
        return self.age

    def get_empty_field(self, position):
        empty_fields = []
        if position.x > 0:
            if self.world.board[position.x - 1][position.y] is None:
                empty_fields.append(Point(position.x - 1, position.y))
        if position.x < self.world.get_height() - 1:
            if self.world.board[position.x + 1][position.y] is None:
                empty_fields.append(Point(position.x + 1, position.y))
        if position.y > 0:
            if self.world.board[position.x][position.y - 1] is None:
                empty_fields.append(Point(position.x, position.y - 1))
        if position.y < self.world.get_width() - 1:
            if self.world.board[position.x][position.y + 1] is None:
                empty_fields.append(Point(position.x, position.y + 1))
        if empty_fields:
            return random.choice(empty_fields)
        return None

    def get_initiative(self):
        return self._initiative

    def kill(self, organism):
        if organism == self.world.get_human():
            self.world.is_human_alive = False
        organism.is_dead = True
        self.world.board[organism.position.x][organism.position.y] = self
        self.world.organisms.remove(organism)
        self.world.event_listener.add_comment(f"{self.get_to_string()} zabija {organism.get_to_string()}[{self.position.x}][{self.position.y}]")

    def special_collision_method(self, collider):
        pass

    def special_action_method(self):
        pass

    def multiplication(self, collider):
        if random.randint(1, 100) < self.multiplication_chance:
            empty_field = self.get_empty_field(collider.position)
            if empty_field is not None:
                new_organism = self.world.create_organism(self.get_to_string(), empty_field.x, empty_field.y)
                self.world.board[new_organism.position.x][new_organism.position.y] = new_organism
                self.world.organisms.append(new_organism)
                self.world.event_listener.add_comment(f'Urodzil sie {self.get_to_string()}[{self.position.x}][{self.position.y}]')

    def get_neighbours(self):
        neighbour_organisms = []
        if self.position.x > 0:
            neighbour_organisms.append(self.world.board[self.position.x - 1][self.position.y])
        if self.position.x < self.world.get_height() - 1:
            neighbour_organisms.append(self.world.board[self.position.x + 1][self.position.y])
        if self.position.y > 0:
            neighbour_organisms.append(self.world.board[self.position.x][self.position.y - 1])
        if self.position.y < self.world.get_width() - 1:
            neighbour_organisms.append(self.world.board[self.position.x][self.position.y + 1])
        return neighbour_organisms

    def get_to_string(self):
        pass

