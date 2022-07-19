import random
from grass import Grass
from human import Human
from sheep import Sheep
from wolf import Wolf
from guarana import Guarana
from wolf_berries import WolfBerries
from antelope import Antelope
from dandelion import Dandelion
from borscht import Borscht
from fox import Fox
from cyber_sheep import CyberSheep
from turtle import Turtle
import copy

class World:

    def __init__(self, width, height, world_screen):
        self._width = width
        self._height = height
        self.board = [[None for x in range(self.get_width())] for y in range(self.get_height())]
        self.organisms = list()
        self.round_number = 0
        self.world_screen = world_screen
        self.is_human_alive = True
        self.is_human_ability_active = False
        self.cooldown = 0 #duration and cooldown in one

    def add_human(self, human_position):
        x, y = human_position
        new_organism = Human(self, x, y)
        self.organisms.append(new_organism)
        self.board[x][y] = new_organism

    def get_human(self):
        for org in self.organisms:
            if isinstance(org, Human):
                return org
        return None

    def add_organisms(self):
        human_position = (random.randint(0, self.get_height() - 1), random.randint(0, self.get_width() - 1))
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                if (i, j) == human_position:
                    self.add_human(human_position)
                else:
                    if random.randint(1, 100) < 40:

                        new_organism = self.get_random_organism()(self, i, j)
                        self.organisms.append(new_organism)
                        self.board[i][j] = new_organism
                    # if i == 1 and j == 1:
                    #     new_organism = self.get_random_organism()(self, i, j)
                    #     self.organisms.append(new_organism)
                    #     self.board[i][j] = new_organism
                    #
                    # if i == 0 and j == 0:
                    #     new_organism = self.get_random_organism()(self, i, j)
                    #     self.organisms.append(new_organism)
                    #     self.board[i][j] = new_organism

    def get_random_organism(self):
        organisms = [
            Borscht, CyberSheep, Grass, Guarana, Wolf, WolfBerries, Turtle, Antelope, Dandelion, Fox,
            CyberSheep
        ]
        return random.choice(organisms)

    def print_organisms(self):
        print(self.organisms)
        print(len(self.organisms))
        # for organism in self.organisms:
        #     print(organism)
        #     print(f'Organism {organism}, initiative = {organism.initiative}, age = {organism.age}')

    def print_board(self):
        for i in range(self._height):
            for j in range(self._width):
                print(self.board[i][j], end=" ")
            print()

    # next round
    def evaluate(self):
        self.event_listener.clear_events()
        self.event_listener.add_comment(f"Runda: {self.round_number}")
        self.sort_organisms()
        self.round_number += 1
        for org in copy.copy(self.organisms):
            if not org.is_dead:
                org.action()
                if not org.is_animal:
                    org.collision(None)
                else:
                    org.collision(org.get_collider())

    def save_world(self, file_path):

        with open(file=file_path, mode="w") as f:
            f.write(f"{self.get_width()};")
            f.write(f"{self.get_height()};")
            f.write(f"{self.round_number};")
            f.write(f'{"1;" if self.is_human_alive else "0;"}')
            f.write(f'{"1;" if self.is_human_ability_active else "0;"}')
            f.write(f"{self.cooldown};")
            for org in self.organisms:
                f.write(f"\n{org.get_to_string()};")
                f.write(f"{org.get_x()};")
                f.write(f"{org.get_y()};")
                f.write(f"{org.get_age()};")
                f.write(f"{org.get_strength()};")

    def sort_organisms(self):
        self.organisms = sorted(self.organisms, key=lambda x: (x.initiative, x.age), reverse=True)

    def get_width(self):
        return self._width

    def create_organism(self, type, x, y):
        new_organism = None
        if type == "Czlowiek":
            new_organism = Human(self, x, y)
        elif type == "Mlecz":
            new_organism = Dandelion(self, x, y)
        elif type == "Antylopa":
            new_organism = Antelope(self, x, y)
        elif type == "Owca":
            new_organism = Sheep(self, x, y)
        elif type == "Wilk":
            new_organism = Wolf(self, x, y)
        elif type == "Wilcze jagody":
            new_organism = WolfBerries(self, x, y)
        elif type == "Trawa":
            new_organism = Grass(self, x, y)
        elif type == "Guarana":
            new_organism = Guarana(self, x, y)
        elif type == "Zolw":
            new_organism = Turtle(self, x, y)
        elif type == "Cyber Owca":
            new_organism = CyberSheep(self, x, y)
        elif type == "Barszcz Sosnowskiego":
            new_organism = Borscht(self, x, y)
        elif type == "Lis":
            new_organism = Fox(self, x, y)

        return new_organism

    def load_organism(self, type, x, y, age, strength):
        new_organism = self.create_organism(type, x, y)
        if new_organism:
            self.board[x][y] = new_organism
            self.organisms.append(new_organism)
            new_organism.age = age
            new_organism.strength = strength

    def is_organism_type(self, organism, type):
        if type == "Czlowiek":
            return isinstance(organism, Human)
        elif type == "Mlecz":
            return isinstance(organism, Dandelion)
        elif type == "Antylopa":
            return isinstance(organism, Antelope)
        elif type == "Owca":
            return isinstance(organism, Sheep)
        elif type == "Wilk":
            return isinstance(organism, Wolf)
        elif type == "Wilcze jagody":
            return isinstance(organism, WolfBerries)
        elif type == "Trawa":
            return isinstance(organism, Grass)
        elif type == "Guarana":
            return isinstance(organism, Guarana)
        elif type == "Zolw":
            return isinstance(organism, Turtle)
        elif type == "Cyber Owca":
            return isinstance(organism, CyberSheep)
        elif type == "Barszcz Sosnowskiego":
            return isinstance(organism, Borscht)
        elif type == "Lis":
            return isinstance(organism, Fox)

    def get_all_borscht(self):
        all_borscht = []
        for organism in self.organisms:
            if isinstance(organism, Borscht):
                all_borscht.append(organism)
        return all_borscht

    def get_height(self):
        return self._height