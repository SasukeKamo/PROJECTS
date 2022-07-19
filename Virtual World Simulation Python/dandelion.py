from plant import Plant

class Dandelion(Plant):

    COLOR = (238, 242, 13)

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 0
        self.strength = 0
        self.multiplication_chance = 10
        self.has_collision_power = False
        self.has_action_power = True

    def special_action_method(self, collider):
        self.multiplication(self)
        self.multiplication(self)
        self.multiplication(self)

    def get_to_string(self):
        return "Mlecz"