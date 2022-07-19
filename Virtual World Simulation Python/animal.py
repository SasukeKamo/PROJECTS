from organism import Organism
from direction import Direction


class Animal(Organism):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.is_animal = True

    def collision(self, collider):
        human = self.world.get_human()
        if collider is None:
            self.world.board[self.position.x][self.position.y] = self
            return
        elif type(collider) == type(self):
            self.go_back()
            self.world.board[self.position.x][self.position.y] = self
            self.multiplication(collider)
        elif collider == human and human.world.is_human_ability_active:
            human.collision(self)
            return
        elif self.has_collision_power:
            self.special_collision_method(collider)
        elif collider.has_collision_power:
            collider.special_collision_method(self)
        else:
            self.fight(collider)

    def run_away(self):
        empty_field = self.get_empty_field(self.position)
        if empty_field.x < self.position.x:
            self.position.x -= 1
        elif empty_field.x > self.position.x:
            self.position.x += 1
        elif empty_field.y < self.position.y:
            self.position.y -= 1
        elif empty_field.y > self.position.y:
            self.position.y += 1

    def action(self):
        super().action()
        if self.has_action_power:
            self.special_action_method()
        else:
            self.undo_position()
            self.direction = self.get_random_direction()
            self.make_move()

    def get_collider(self):
        return self.world.board[self.position.x][self.position.y]

    def go_back(self):
        if self.direction == Direction.UP:
            self.position.x += 1
        elif self.direction == Direction.DOWN:
            self.position.x -= 1
        elif self.direction == Direction.LEFT:
            self.position.y += 1
        elif self.direction == Direction.RIGHT:
            self.position.y -= 1

    def fight(self, collider):
        if self.strength >= collider.strength:
            self.kill(collider)
        elif self.strength < collider.strength:
            print(f'{collider.strength}')
            collider.kill(self)

    def get_to_string(self):
        pass






