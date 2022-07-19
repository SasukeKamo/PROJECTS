from animal import Animal
from point import Point
from direction import Direction
import random


class Antelope(Animal):
    COLOR = (153, 77, 0)

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 4
        self.strength = 4
        self.has_action_power = True
        self.has_collision_power = True

    def make_big_move(self):
        if self.direction == Direction.UP and 1 < self.position.x:
            self.position.x -= 2
        elif self.direction == Direction.DOWN and self.position.x < self.world.get_height() - 2:
            self.position.x += 2
        elif self.direction == Direction.LEFT and 1 < self.position.y:
            self.position.y -= 2
        elif self.direction == Direction.RIGHT and self.position.y < self.world.get_width() - 2:
            self.position.y += 2

    def special_action_method(self):
        self.undo_position()
        self.direction = self.get_random_direction()
        self.make_big_move()

    def has_free_neighbour_field(self):
        if self.world.board[self.position.x][self.position.y + 1] is None\
                or self.world.board[self.position.x][
            self.position.y - 1] is None or self.world.board[self.position.x - 1][self.position.y] is None or \
                self.world.board[self.position.x + 1][self.position.y] is None:
            return True
        return False

    def go_back(self):
        super().go_back()
        super().go_back()

    def get_free_neighbour_field(self):
        free_field = []
        if self.position.x > 0:
            if self.world.board[self.position.x - 1][self.position.y] is None:
                free_field.append(Point(self.position.x - 1, self.position.y))
        if self.position.x < self.world.get_height() - 1:
            if self.world.board[self.position.x + 1][self.position.y] is None:
                free_field.append(Point(self.position.x + 1, self.position.y))
        if self.position.y > 0:
            if self.world.board[self.position.x][self.position.y - 1] is None:
                free_field.append(Point(self.position.x, self.position.y - 1))
        if self.position.y < self.world.get_width() - 1:
            if self.world.board[self.position.x][self.position.y + 1] is None:
                free_field.append(Point(self.position.x, self.position.y + 1))
        chance = random.randint(0, len(free_field))
        return random.choice(free_field)

    def special_collision_method(self, collider):
        free_field = self.get_empty_field(self.position)
        if free_field:
            print("mam wolne pole")
            chance = random.randint(1, 2)
            if chance == 1:
                print("walcze")
                self.fight(collider)
            else:
                print("uciekam")
                print(free_field.x, free_field.y)
                self.world.board[self.position.x][self.position.y] = collider
                self.position = free_field
                self.world.board[free_field.x][free_field.y] = self
                self.world.event_listener.add_comment(f"{self.get_to_string()} ucieka od {collider.get_to_string()}")
        else:
            self.fight(collider)

    def get_to_string(self):
        return "Antylopa"
