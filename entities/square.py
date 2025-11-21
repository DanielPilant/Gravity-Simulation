import pygame

class Square:
    def __init__(self, x, y, size, color, mass):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.mass = mass
        self.vy = 0.0  # vertical velocity
        self.vx = 0.0  # horizontal velocity
        self.dragging = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
            (self.x, self.y, self.size, self.size))
