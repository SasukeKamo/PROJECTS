from animal import Animal



class Sheep(Animal):

    COLOR = (254, 225, 253)

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 4
        self.strength = 4

    def __repr__(self):
        return 'Sheep'


    def get_to_string(self):
        return "Owca"

