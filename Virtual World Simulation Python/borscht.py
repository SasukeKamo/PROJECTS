from plant import Plant
from cyber_sheep import CyberSheep

class Borscht(Plant):

    COLOR = (153, 0, 153)

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 0
        self.strength = 0
        self.multiplication_chance = 10
        self.has_collision_power = True
        self.has_action_power = True

    def action(self):
        super().action()
        self.special_action_method()

    def kill(self, organism):
        if organism == self.world.get_human():
            self.world.is_human_alive = False
        organism.is_dead = True
        self.world.board[organism.position.x][organism.position.y] = None
        self.world.organisms.remove(organism)
        self.world.event_listener.add_comment(f"{self.get_to_string()} zabija {organism.get_to_string()}[{self.position.x}][{self.position.y}]")


    def special_action_method(self):
        neighbours = self.get_neighbours()
        for neighbour in neighbours:
            if neighbour is not None and type(neighbour) is not type(self) and not isinstance(neighbour, CyberSheep) and not self.world.is_human_ability_active:
                self.kill(neighbour)

    def special_collision_method(self, collider):
        if self.is_dead or collider.is_dead:
            return
        if not isinstance(collider, CyberSheep):
            self.kill(collider)


    def get_to_string(self):
        return "Barszcz Sosnowskiego"
