from animal import Animal



class Fox(Animal):

    COLOR = (255, 153, 0)

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 7
        self.strength = 3
        self.has_action_power = True

    def special_action_method(self):
        neighbours = self.get_neighbours()
        self.undo_position()
        counter = 0
        for neighbour in neighbours:
            if neighbour != None:
                if neighbour.strength > self.strength:
                    counter += 1
        if counter == 0:
            self.direction = self.get_random_direction()
            self.make_move()

    def get_to_string(self):
        return "Lis"