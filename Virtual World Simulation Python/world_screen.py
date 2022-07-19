import event_listener
from world import World
from grass import Grass
from sheep import Sheep
from wolf import Wolf
from antelope import Antelope
from guarana import Guarana
from turtle import Turtle
from dandelion import Dandelion
from borscht import Borscht
from fox import Fox
from cyber_sheep import CyberSheep
from wolf_berries import WolfBerries
from dandelion import Dandelion
from turtle import Turtle
import pygame
import sys
from direction import Direction
from button import Button
from event_listener import EventListener
from input_rect import InputRect


class WorldScreen(World):
    SCREEN_WIDTH, SCREEN_HEIGHT = 720, 720
    BOARD_WIDTH, BOARD_HEIGHT = 500, 500
    DESCRIPTION_WIDTH, DESCRIPTION_HEIGHT = 720, 220
    EVENT_WIDTH, EVENT_HEIGHT = 220, 500
    EMPTY_FIELD_COLOR = (255, 221, 169)


    def __init__(self, width, height, screen):
        super().__init__(width, height, self)
        self.organism_width = int(self.BOARD_WIDTH / self.get_width())
        self.organism_height = int(self.BOARD_HEIGHT / self.get_height())
        self.screen = screen
        self.load_button = None
        self.save_button = None
        self.events_button = None
        self.save_label = None
        self.event_listener = EventListener(self.screen, self.EVENT_WIDTH, self.EVENT_HEIGHT)

    def draw_world(self):
        self.draw_board()
        self.draw_descriptions()
        self.draw_events()
        self.draw_buttons()

    def draw_buttons(self):
        self.save_button = Button((self.BOARD_WIDTH + 37, 25, 150, 50), (0, 0, 0), " Zapisz i wyjdz", 27)
        # self.events_button = Button((self.BOARD_WIDTH + 50, 100, 120, 50), (0, 0, 0), "Zdarzenia", 25)
        self.save_button.draw_button(self.screen)
        # self.events_button.draw_button(self.screen)


    def draw_descriptions(self):
        organism_description = {
            'Antylopa': Antelope.COLOR,
            'Cyber-owca': CyberSheep.COLOR,
            'Lis': Fox.COLOR,
            'Owca': Sheep.COLOR,
            'Wilk': Wolf.COLOR,
            'Zolw': Turtle.COLOR,
            'Barszcz': Borscht.COLOR,
            'Guarana': Guarana.COLOR,
            'Mlecz': Dandelion.COLOR,
            'Trawa': Grass.COLOR,
            'Wilcze jagody': WolfBerries.COLOR,
            'Ziemia': (255, 221, 169),
        }

        position_x, position_y = 5, 550
        for description in list(organism_description.keys())[:6]:
            pygame.draw.rect(self.screen, organism_description[description], (
                pygame.Rect(position_x, position_y, 110, 25)))
            text = pygame.font.Font(None, 20).render(description, True, (0, 0, 0))
            self.screen.blit(text, (position_x, position_y + 5))
            position_x, position_y = position_x + 120, position_y
        position_x, position_y = 5, 650
        for description in list(organism_description.keys())[6:]:
            pygame.draw.rect(self.screen, organism_description[description], (
                pygame.Rect(position_x, position_y, 110, 25)))
            text = pygame.font.Font(None, 20).render(description, True, (0, 0, 0))
            self.screen.blit(text, (position_x, position_y + 5))
            position_x, position_y = position_x + 120, position_y

    def draw_events(self):
        pass

    def draw_board(self):
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                if self.board[i][j] is not None:
                    self.board[i][j].draw(i, j)
                else:
                    self.draw_empty_field(i, j)

    def show_error_label(self):
        red_color = (255, 0, 0)
        text_surface = self.save_label.LABEL_FONT.render("Wprowadz prawidlowe dane!", True, (255, 0, 0))
        self.screen.blit(text_surface, (self.save_label.input_rect.x - 100, self.save_label.input_rect.y - 50))

    def draw_empty_field(self, x, y):
        pygame.draw.rect(self.screen, self.EMPTY_FIELD_COLOR, (
            pygame.Rect(y * self.organism_width, x * self.organism_height, self.organism_width - 2,
                        self.organism_height - 2)))

    def is_valid_save_input(self):
        return True

    def show_save_label(self):
        self.save_label = InputRect(40, (self.BOARD_WIDTH / 2 + 50, 300, 500, 40), "test.txt")
        self.save_label.is_active = True

    def update_input_hover(self):
        if self.save_label.is_active:
            self.save_label.color = self.save_label.color_active
        else:
            self.save_label.color = self.save_label.color_passive

    def draw_input_labels(self):
        self.save_label.draw_title_label(self.screen, "Podaj nazwe pliku i zatwierdz przyciskiem 'ENTER'",
                                         (0, 0, 0), pygame.font.Font(None, 30),  (self.save_label.input_rect.x - 200, self.save_label.input_rect.y - 50))

    def get_events(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.save_button.surface.collidepoint(event.pos):
                        print('Save World')
                        self.show_save_label()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.is_human_alive:
                        self.get_human().change_direction(Direction.UP)
                        self.evaluate()
                    elif event.key == pygame.K_DOWN and self.is_human_alive:
                        self.get_human().change_direction(Direction.DOWN)
                        self.evaluate()
                    elif event.key == pygame.K_LEFT and self.is_human_alive:
                        self.get_human().change_direction(Direction.LEFT)
                        self.evaluate()
                    elif event.key == pygame.K_RIGHT and self.is_human_alive:
                        self.get_human().change_direction(Direction.RIGHT)
                        self.evaluate()
                    elif event.key == pygame.K_RIGHT and self.is_human_alive:
                        self.get_human().change_direction(Direction.RIGHT)
                        self.evaluate()
                    elif event.key == pygame.K_m and self.is_human_alive:
                        self.print_organisms()
                        self.print_board()
                    elif event.key == pygame.K_n:
                        self.event_listener.show_next_events()
                    elif event.key == pygame.K_p:
                        self.event_listener.show_previous_events()
                    elif event.key == pygame.K_SPACE:
                        if self.is_human_alive:
                            self.get_human().direction = None
                        self.evaluate()
                    elif event.key == pygame.K_x and self.get_human():
                        if self.cooldown == 0 and self.is_human_ability_active == False:
                            self.event_listener.add_comment("Umiejetnosc aktywowana")
                            self.is_human_ability_active = True
                        elif self.is_human_ability_active == True:
                            self.event_listener.add_comment("Umiejetnosc jest juz aktywna")
                        elif self.cooldown != 0 and self.is_human_ability_active == False:
                            self.event_listener.add_comment("Nie mozna jeszcze aktywowac umiejetnosci")
                    elif self.save_label and self.save_label.is_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.save_label.user_text = self.save_label.user_text[:-1]
                        elif event.key == pygame.K_RETURN:
                            self.save_world(self.save_label.user_text)
                            print(f'Zatwierdzam i potwierdzam, zapisany plik to {self.save_label.user_text}')
                            pygame.quit()
                            sys.exit()
                        else:
                            self.save_label.user_text += event.unicode


            self.screen.fill((209, 209, 209))
            self.draw_world()
            self.event_listener.draw_window()
            self.draw_descriptions()
            if self.save_label:
                self.screen.fill((127, 127, 127))
                self.draw_input_labels()
                self.save_label.draw(self.screen)
                self.update_input_hover()
            if not self.is_valid_save_input():
                # self.show_error_label()
                pass
            pygame.display.flip()
            clock.tick(60)
