from plant import Plant


def get_to_string():
    return "Guarana"


class Guarana(Plant):

    COLOR = (255, 0, 0)

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 0
        self.strength = 0

    def collision(self, collider):
        collider.strength += 3
