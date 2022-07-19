from animal import Animal

class Wolf(Animal):

    COLOR = (79, 79, 125)

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 5
        self.strength = 9

    def get_to_string(self):
        return "Wilk"