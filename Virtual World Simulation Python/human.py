from animal import Animal
import pygame
import os


class Human(Animal):

    def __init__(self, world, x, y):
        super().__init__(world, x, y)
        self.initiative = 4
        self.strength = 5
        #self.is_human_ability_active = False
        #self.cooldown = 0

        self.IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images/", "humanPNG.png")),
                                             (self.world.organism_width, self.world.organism_height))

    def check_ability_condition(self):

        if self.world.is_human_ability_active and self.world.cooldown < 5:
            self.world.cooldown += 1
        else:
            if self.world.cooldown > 0:
                self.world.cooldown -= 1

        if self.world.cooldown == 5:
            self.world.is_human_ability_active = False

    def collision(self, collider):
        if self.world.is_human_ability_active:
            if collider is None:
                self.world.board[self.position.x][self.position.y] = self
                return
            elif not collider.is_animal or self.strength > collider.strength:
                self.kill(collider)
            else:
                empty_field = self.get_empty_field(self.position)
                if empty_field:
                    self.world.board[self.position.x][self.position.y] = collider
                    self.position = empty_field
                    self.world.board[empty_field.x][empty_field.y] = self
                else:
                    self.kill(collider)
        else:
            super().collision(collider)

    def action(self):
        self.check_ability_condition()
        self.age += 1
        self.undo_position()
        self.make_move()

    def change_direction(self, direction):
        self.direction = direction

    def draw(self, position_x, position_y):
        self.world.screen.blit(self.IMAGE, (self.position.y * self.world.organism_width, self.position.x * self.world.organism_height))

    def get_to_string(self):
        return "Czlowiek"