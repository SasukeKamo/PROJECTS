import random
from grass import Grass
from human import Human
from sheep import Sheep
from wolf import Wolf
from guarana import Guarana
from wolf_berries import WolfBerries

class World:

    def __init__(self, width, height, world_screen):
        self._width = width
        self._height = height
        self.board = [[None for x in range(self.get_width())] for y in range(self.get_height())]
        self.organisms = list()
        self.round_number = 0
        self.world_screen = world_screen
        self.is_human_alive = True

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
                    if i == 0 and j == 0:
                        new_organism = self.get_random_organism()(self, i, j)
                        self.organisms.append(new_organism)
                        self.board[i][j] = new_organism

    def get_random_organism(self):
        organisms = [Sheep]
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
        for org in self.organisms:
            if not org.is_dead:
                org.action()
                org.collision(org.get_collider())

    def save_world(self, file_path):

        with open(file=file_path, mode="w") as f:
            f.write(f"{self.get_width()};")
            f.write(f"{self.get_height()};")
            f.write(f"{self.round_number};")
            f.write(f"{self.is_human_alive}")
            for org in self.organisms:
                f.write(f"\n{org};")
                f.write(f"{org.get_x()};")
                f.write(f"{org.get_y()};")
                f.write(f"{org.get_age()};")
                f.write(f"{org.get_strength()}")

    def sort_organisms(self):
        self.organisms = sorted(self.organisms, key=lambda x: (x.initiative, x.age), reverse=True)

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height