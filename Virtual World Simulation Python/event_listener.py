import pygame
from human import Human
from world import World


class EventListener:

    COMMENT_FONT = pygame.font.Font(None, 12)
    FOOTER_FONT = pygame.font.Font(None, 15)
    def __init__(self, surface, width, height):
        self.surface = surface
        self.width = width
        self.height = height
        self.stop = 30
        self.start = 0
        self.events = []
        self.page = 0

    def add_comment(self, comment):
        self.events.append(comment)

    def clear_events(self):
        self.events.clear()
        self.start = 0
        self.stop = 30
        self.page = 0

    def draw_window(self):
        self.draw_events()

    def show_next_events(self):
        if self.start + 30 > len(self.events):
            return
        if len(self.events) > 30:
            self.page += 1
            self.start += 30
            self.stop += 30

    def show_previous_events(self):
        if self.start - 30 < 0:
            return
        if self.page > 0:
            self.page -= 1
            self.start -= 30
            self.stop -= 30

    def draw_events(self):
        position_x, position_y = 550, 100
        for index in range(self.start, self.stop):
            if index == len(self.events):
                break
            text_surface = self.COMMENT_FONT.render(self.events[index], True, (0, 0, 0))
            self.surface.blit(text_surface, (position_x, position_y))
            position_y += 13
        if self.events:
            self.display_footer()

    def display_footer(self):
        footer_text = ""
        if self.page == 0 and len(self.events) > 30:
            footer_text = "Nastepna strona (n)"
            text_surface = self.FOOTER_FONT.render(footer_text, True, (0, 0, 0))
            self.surface.blit(text_surface, (550, 500))

        if self.page == int(len(self.events) / 30) and self.page > 0:
            footer_text = "Poprzednia strona (p)"
            text_surface = self.FOOTER_FONT.render(footer_text, True, (0, 0, 0))
            self.surface.blit(text_surface, (540, 500))

        if self.page > 0 and self.page < int(len(self.events) / 30):
            footer_text_1 = "Nastepna strona (n)"
            footer_text_2 = "Poprzednia strona (p)"
            text_surface = self.FOOTER_FONT.render(footer_text_1, True, (0, 0, 0))
            self.surface.blit(text_surface, (550, 500))
            text_surface = self.FOOTER_FONT.render(footer_text_2, True, (0, 0, 0))
            self.surface.blit(text_surface, (540, 520))

