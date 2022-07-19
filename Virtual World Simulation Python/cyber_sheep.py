from animal import Animal
from direction import Direction

class CyberSheep(Animal):

    COLOR = (0, 255, 247)

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 4
        self.strength = 11
        self.has_action_power = True
        self.has_collision_power = True

    def get_closest_borscht(self):
        closest_borscht = None
        max_abs = 100
        for borscht in self.world.get_all_borscht():
            distance = abs(self.position.x - borscht.position.x) + abs(self.position.y - borscht.position.y)
            if distance < max_abs:
                max_abs = distance
                closest_borscht = borscht
        return closest_borscht

    def action(self):
        self.age += 1
        self.undo_position()
        if not self.world.get_all_borscht():
            self.direction = self.get_random_direction()
        else:
            self.extra_action_behavior()
        self.make_move()

    def special_collision_method(self, collider):
        if self.world.is_organism_type(collider, "Barszcz Sosnowskiego"):
            self.kill(collider)
        else:
            self.fight(collider)

    def extra_action_behavior(self):
        nearest_borsch = self.get_closest_borscht()
        if self.position.x > nearest_borsch.position.x:
            self.direction = Direction.UP
        elif self.position.x < nearest_borsch.position.x:
            self.direction = Direction.DOWN
        elif self.position.y > nearest_borsch.position.y:
            self.direction = Direction.LEFT
        elif self.position.y < nearest_borsch.position.y:
            self.direction = Direction.RIGHT

    def get_to_string(self):
        return "Cyber Owca"

