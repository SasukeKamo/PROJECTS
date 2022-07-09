from plant import Plant


def get_to_string():
    return "Wilcze jagody"


class WolfBerries(Plant):

    COLOR = (255, 0, 191)

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 0
        self.strength = 99

    def collision(self, collider):
        if collider.is_animal:
            collider.is_dead = True

