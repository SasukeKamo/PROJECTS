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
        self.load_button = None
        self.screen = pygame.display.set_mode([self.WIDTH, self.HEIGHT])
        pygame.display.set_caption('Wirtualny Swiat')
        self.width_input = None
        self.height_input = None
        self.button = None
        self.is_valid_input = True

    def draw_menu(self):
        self.width_input = InputRect(32, (self.WIDTH / 2 - 70, 200, 300, 32), "20")
        self.height_input = InputRect(32, (self.WIDTH / 2 - 70, 300, 300, 32), "20")
        self.button = Button((self.WIDTH / 2 - 97, 380, 150, 50), (0, 0, 0), "NOWA GRA", 36)
        self.load_button = Button((self.WIDTH / 2 - 97, 450, 150, 50), (0, 0, 0), "  WCZYTAJ", 36)
        self.get_events()

    def draw_input_labels(self):
        self.height_input.draw_title_label(self.screen, "Podaj wysokosc planszy:", (0, 0, 0), pygame.font.Font(None, 25),
                                           (self.height_input.input_rect.x - 50, self.height_input.input_rect.y - 30))
        self.width_input.draw_title_label(self.screen, "Podaj szerokosc planszy:", (0, 0, 0), pygame.font.Font(None, 25),
                                          (self.width_input.input_rect.x - 50, self.width_input.input_rect.y - 30))

    def update_input_hover(self):
        if self.width_input.is_active:
            self.width_input.color = self.width_input.color_active
        else:
            self.width_input.color = self.width_input.color_passive

        if self.height_input.is_active:
            self.height_input.color = self.height_input.color_active
        else:
            self.height_input.color = self.height_input.color_passive

    def start_simulation(self):
        self.screen.fill((127, 127, 127))
        world = WorldScreen(int(self.width_input.user_text), int(self.height_input.user_text), self.screen)
        world.add_organisms()
        world.get_events()

    def show_error_label(self):
        red_color = (255, 0, 0)
        text_surface = self.MENU_FONT.render("Wprowadz prawidlowe dane!", True, (255, 0, 0))
        self.screen.blit(text_surface, (self.button.surface.x - 100, self.button.surface.y - 50))

    def validate_input(self):
        try:
            int(self.width_input.user_text)
            int(self.height_input.user_text)
            if not 2 <= int(self.width_input.user_text) <= 30 or not 2 <= int(self.height_input.user_text) <= 30:
                self.is_valid_input = False
            else:
                self.is_valid_input = True

        except:
            self.is_valid_input = False


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

                    if self.button.surface.collidepoint(event.pos):
                        self.validate_input()
                        if self.is_valid_input:
                            self.start_simulation()

                if event.type == pygame.KEYDOWN:
                    if self.height_input.is_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.height_input.user_text = self.height_input.user_text[:-1]
                        else:
                            self.height_input.user_text += event.unicode
                    if self.width_input.is_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.width_input.user_text = self.width_input.user_text[:-1]
                        else:
                            self.width_input.user_text += event.unicode

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.BACKGROUND, (0, 0))
            self.draw_input_labels()
            self.button.draw_button(self.screen)
            self.load_button.draw_button(self.screen)
            if not self.is_valid_input:
                self.show_error_label()

            self.update_input_hover()

            self.height_input.draw(self.screen)
            self.width_input.draw(self.screen)

            pygame.display.flip()
            clock.tick(60)





