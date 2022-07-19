from plant import Plant




class Guarana(Plant):

    COLOR = (255, 0, 0)

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 0
        self.strength = 0
        self.has_collision_power = True

    def special_collision_method(self, collider):
        collider.strength += 3
        collider.kill(self)

    def get_to_string(self):
        return "Guarana"
