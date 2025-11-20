import pygame
import sys

from core.colors import WHITE, BLUE, DARK_BLUE, BLACK
from core.fonts import FONT


class Button:
    def __init__(self, x, y, w, h, text, callback):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.callback = callback 
        self.hovered = False
    
    def draw(self, surface):
        color = DARK_BLUE if self.hovered else BLUE
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        text_surf = FONT.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.callback() 