from plant import Plant


class WolfBerries(Plant):

    COLOR = (255, 0, 191)

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 0
        self.strength = 99
        self.multiplication_chance = 5
        self.has_collision_power = True

    def special_collision_method(self, collider):
        self.kill(collider)

    def get_to_string(self):
        return "Wilcze jagody"

