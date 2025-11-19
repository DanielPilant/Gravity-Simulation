import pygame

from entities.square import Square
from physics.world import EarthGravity
from entities.objects import square1, square2

pygame.init()                               

FPS = 60
WIDTH, HEIGHT = 800, 900                    
screen = pygame.display.set_mode((WIDTH, HEIGHT))   
pygame.display.set_caption("Square Demo")   

squares = [square1, square2]
e_gravity = EarthGravity()
clock = pygame.time.Clock()

dt = 1/FPS 
e = 0.7 # coefficient of restitution
offset_x = 0
offset_y = 0

running = True
while running:
        
    screen.fill((30, 30, 30))
    clock.tick(FPS)
    
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:       
            running = False 
            
        # drag squares with mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for square in squares:
                if square.x <= mx <= square.x + square.size and \
                   square.y <= my <= square.y + square.size:
                    square.dragging = True
                    square.vy = 0.0
        if event.type == pygame.MOUSEBUTTONUP:
            for square in squares:
                square.dragging = False
 
        for square in squares:
            if not square.dragging:
                square.vy += e_gravity.acceleration()*dt
                square.y += square.vy*dt
                print("vy:", square.vy, "y:", square.y)
                if square.y + square.size >= HEIGHT:
                    square.y = HEIGHT - square.size
                    square.vy = -square.vy * e
        
    for square in squares:
        square.draw(screen)

    pygame.display.flip()                  

pygame.quit()                               
