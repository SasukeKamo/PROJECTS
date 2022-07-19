from organism import Organism
import random


class Plant(Organism):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)

    def action(self):
        self.multiplication(self)

    def collision(self, collider):
        if random.randint(1, 100) < self.multiplication_chance:
            neighbour_field = self.get_empty_field(self.position)
            if neighbour_field:
                self.world.create_organism(self.get_to_string(), neighbour_field.x, neighbour_field.y)
                self.world.event_listener.add_comment(f'Urodzil sie {self.get_to_string()}[{self.position.x}][{self.position.y}]')
