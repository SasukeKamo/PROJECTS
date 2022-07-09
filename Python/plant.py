from organism import Organism


class Plant(Organism):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)

    def action(self):
        pass

    def collision(self, collider):
        pass
