from organism import Organism
from direction import Direction


class Animal(Organism):
    def __init__(self, world, x, y):
        super().__init__(world, x, y)

    def collision(self, collider):
        if collider is None:
            self.world.board[self.position.x][self.position.y] = self
            return
        if type(collider) == type(self):
            self.go_back()
            self.world.board[self.position.x][self.position.y] = self
        else:
            self.fight(collider)

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
        if self.strength > collider.strength:
            self.kill(collider)
        elif self.strength < collider.strength:
            print("test")
            collider.kill(self)

    def get_to_string(self):
        pass

    def kill(self, organism):
        organism.is_dead = True
        self.world.board[organism.position.x][organism.position.y] = self
        self.world.organisms.remove(organism)
        self.world.event_listener.add_comment(f"{self.get_to_string()} zabija {organism.get_to_string()} na pozycji({self.position.x}, {self.position.y})")







