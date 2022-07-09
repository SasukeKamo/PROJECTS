import pygame
pygame.init()

class InputRect:
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    WHITE_COLOR = (255, 255, 255)
    LABEL_FONT = pygame.font.Font(None, 25)

    def __init__(self, font_size, rect_size, default_text):
        self.input_font = pygame.font.Font(None, font_size)
        self.input_rect = pygame.Rect(rect_size)
        self.user_text = default_text
        self.is_active = False
        self.color = self.color_passive

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.input_rect)
        text_surface = self.input_font.render(self.user_text, True, (255, 255, 255))
        screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        self.input_rect.w = max(100, text_surface.get_width() + 10)

    def draw_title_label(self, screen, title, color, font, position):
        text = font.render(title, True, color)
        screen.blit(text,position)

