import pygame
pygame.init()


class Button:

    WHITE_COLOR = (255, 255, 255)

    def __init__(self, button_size, color, title, font_size):
        self.color = color
        self.title = title
        self.surface = pygame.Rect(button_size)
        self.BUTTON_FONT = pygame.font.Font(None, font_size)

    def draw_button(self, screen):
        pygame.draw.rect(screen, self.color, self.surface)
        self.draw_button_text(screen)

    def draw_button_text(self, screen):
        text = self.BUTTON_FONT.render(self.title, True, self.WHITE_COLOR)
        screen.blit(text, (self.surface.x + 5, self.surface.y + 14))
