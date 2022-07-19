import pygame
import sys
import os
from input_rect import InputRect
from button import Button
from world_screen import WorldScreen


class Menu:
    MENU_FONT = pygame.font.Font(None, 32)
    BACKGROUND = pygame.image.load(os.path.join('images/', 'background.png'))
    WIDTH, HEIGHT = 720, 720

    def __init__(self):
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption('Wirtualny Swiat')
        self.width_input = None
        self.height_input = None
        self.load_button = None
        self.button = None
        self.load_label = None
        self.load_file = "test.txt"

    def draw_menu(self):
        self.width_input = InputRect(32, (self.WIDTH / 2 - 70, 200, 300, 32), "20")
        self.height_input = InputRect(32, (self.WIDTH / 2 - 70, 300, 300, 32), "20")
        self.button = Button((self.WIDTH / 2 - 97, 380, 150, 50), (0, 0, 0), "NOWA GRA", 36)
        self.load_button = Button((self.WIDTH / 2 - 97, 450, 150, 50), (0, 0, 0), "  WCZYTAJ", 36)
        self.get_events()

    def draw_size_input_labels(self):
        self.height_input.draw_title_label(self.screen, "Podaj wysokosc planszy:", (0, 0, 0),
                                           pygame.font.Font(None, 25),
                                           (self.height_input.input_rect.x - 50, self.height_input.input_rect.y - 30))
        self.width_input.draw_title_label(self.screen, "Podaj szerokosc planszy:", (0, 0, 0),
                                          pygame.font.Font(None, 25),
                                          (self.width_input.input_rect.x - 50, self.width_input.input_rect.y - 30))

    def draw_file_input_labels(self):
        self.load_label.draw_title_label(self.screen, "Podaj nazwe pliku i zatwierdz przyciskiem 'ENTER'",
                                         (0, 0, 0), pygame.font.Font(None, 30),  (self.load_label.input_rect.x - 200, self.load_label.input_rect.y - 50))


    def update_world_size_input_hover(self):
        if self.width_input.is_active:
            self.width_input.color = self.width_input.color_active
        else:
            self.width_input.color = self.width_input.color_passive
        if self.height_input.is_active:
            self.height_input.color = self.height_input.color_active
        else:
            self.height_input.color = self.height_input.color_passive

    def update_file_input_hover(self):
        self.load_file = self.load_label.user_text
        if self.load_label.is_active:
            self.load_label.color = self.load_label.color_active
        else:
            self.load_label.color = self.load_label.color_passive

    def start_simulation(self):
        self.screen.fill((127, 127, 127))
        world = WorldScreen(int(self.width_input.user_text), int(self.height_input.user_text), self.screen)
        world.add_organisms()
        world.get_events()

    def load_simulation(self):
        self.screen.fill((127, 127, 127))
        with open(self.load_file, mode="r") as file:
            simulation_info = file.readline()
            simulation_info = simulation_info.split(";")
            simulation_info = simulation_info[:6]
            print(simulation_info)
            world = WorldScreen(int(simulation_info[0]), int(simulation_info[1]), self.screen)
            world.round_number = int(simulation_info[2])
            world.is_human_alive = bool(int(simulation_info[3]))
            world.is_human_ability_active = bool(int(simulation_info[4]))
            world.cooldown = int(simulation_info[5])
            print(world.is_human_alive)

            for line in file:
                line = line.split(";")
                line = line[:5]
                world.load_organism(line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4]))

        world.get_events()

    def show_error_label(self):
        red_color = (255, 0, 0)
        text_surface = self.MENU_FONT.render("Wprowadz prawidlowe dane!", True, (255, 0, 0))
        self.screen.blit(text_surface, (self.button.surface.x - 100, self.button.surface.y - 50))

    def is_valid_world_size_input(self):
        try:
            int(self.width_input.user_text)
            int(self.height_input.user_text)
            if not 2 <= int(self.width_input.user_text) <= 30 or not 2 <= int(self.height_input.user_text) <= 30:
                return False
            else:
                return True
        except:
            return False
        
    def is_valid_load_file_input(self):
        if os.path.exists(self.load_file):
            return True
        return False
    
    def show_load_label(self):
        self.load_label = InputRect(40, (500 / 2 + 50, 300, 500, 40), "test.txt")
        self.load_label.is_active = True

    def get_events(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.width_input.input_rect.collidepoint(event.pos):
                        self.width_input.is_active = True
                    else:
                        self.width_input.is_active = False

                    if self.height_input.input_rect.collidepoint(event.pos):
                        self.height_input.is_active = True
                    else:
                        self.height_input.is_active = False

                    if self.load_button.surface.collidepoint(event.pos):
                        self.show_load_label()

                    if self.button.surface.collidepoint(event.pos):
                        if self.is_valid_world_size_input():
                            self.start_simulation()

                if event.type == pygame.KEYDOWN:
                    if self.height_input.is_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.height_input.user_text = self.height_input.user_text[:-1]
                        else:
                            self.height_input.user_text += event.unicode
                    elif self.width_input.is_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.width_input.user_text = self.width_input.user_text[:-1]
                        else:
                            self.width_input.user_text += event.unicode
                    elif self.load_label.is_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.load_label.user_text = self.load_label.user_text[:-1]
                        elif event.key == pygame.K_RETURN:
                            if self.is_valid_load_file_input():
                                print("ladujemy swiat")
                                self.load_simulation()

                        else:
                            self.load_label.user_text += event.unicode

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.BACKGROUND, (0, 0))
            self.draw_size_input_labels()
            self.button.draw_button(self.screen)
            self.load_button.draw_button(self.screen)
            if not self.is_valid_world_size_input():
                self.show_error_label()

            self.update_world_size_input_hover()

            self.height_input.draw(self.screen)
            self.width_input.draw(self.screen)

            if self.load_label:
                self.screen.fill((127, 127, 127))
                self.draw_file_input_labels()
                self.load_label.draw(self.screen)
                self.update_file_input_hover()
            if self.load_label and not self.is_valid_load_file_input():

                self.show_error_label()
            pygame.display.flip()
            clock.tick(60)





