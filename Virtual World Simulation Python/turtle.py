from animal import Animal
import random


class Turtle(Animal):

    COLOR = (16, 75, 2)

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 1
        self.strength = 2
        self.has_collision_power = True
        self.has_action_power = True

    def special_action_method(self):
        chance_to_move = random.randint(1, 4)
        self.undo_position()
        if chance_to_move == 4:
            self.direction = self.get_random_direction()
            self.make_move()

    def special_collision_method(self, collider):
        if collider.strength < 5:
            self.world.board[collider.position.x][collider.position.y] = collider
            self.run_away()
            if self.position.x == collider.position.x and self.position.y == collider.position.y:
                collider.fight(self)
                return
            self.world.board[self.position.x][self.position.y] = self
        else:
            if(collider.is_animal):
                collider.fight(self)

    def get_to_string(self):
        return "Zolw"