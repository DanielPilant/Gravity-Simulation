from numpy import sin
import pygame
import sys

from entities.square import Square
from physics.world import EarthGravity, MoonGravity, sunGravity
from entities.objects import (
    square1,
    square2,
    square3,
    square4,
    square5,
    square6,
)

pygame.init()                               

# Constants and setup
FPS = 144
WIDTH, HEIGHT = 1000, 900                    
screen = pygame.display.set_mode((WIDTH, HEIGHT))   
pygame.display.set_caption("Square Demo")   

# Game variables
squares = [square1, square2, square3, square4, square5, square6]

g = "earth"  # choose gravity: "earth", "moon", or "sun"
if g == "sun":
    gravity = sunGravity()
elif g == "earth":
    gravity = EarthGravity()
else:
    gravity = MoonGravity()  # default to Moon gravity
clock = pygame.time.Clock()
dt = 1/FPS 
e = 0.7 # coefficient of restitution
offset_x = 0
offset_y = 0
running = True
mouse_pre_vx = 0
mouse_pre_vy = 0
throw_strength = 0.5  # scale if needed

# Main game loop
while running:
    
    screen.fill((30, 30, 30))
    clock.tick(FPS)
                    
    mx, my = pygame.mouse.get_pos()
    mouse_vx = (mx - mouse_pre_vx) / dt
    mouse_vy = (my - mouse_pre_vy) / dt

    mouse_pre_vx = mx  
    mouse_pre_vy = my
    
    # Handle events
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:       
            running = False 
            
        # drag squares with mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            for square in squares:
                if square.x <= mx <= square.x + square.size and \
                   square.y <= my <= square.y + square.size:
                    square.dragging = True
                    square.vy = 0.0  # reset vertical velocity when picked up
                    square.vx = 0.0  # reset horizontal velocity when picked up
                    break
                
        if event.type == pygame.MOUSEBUTTONUP:
            for square in squares:
                if square.dragging:
                    square.dragging = False
                    square.vx = mouse_vx * throw_strength
                    square.vy = mouse_vy * throw_strength
    
                    

    
    # Update squares
    for square in squares:
        if square.dragging:
            square.x = mx - square.size / 2
            square.y = my - square.size / 2
        else:
            square.vy += gravity.acceleration() * dt
            square.x += square.vx * dt
            square.y += square.vy * dt
            
            if square.y + square.size >= HEIGHT:
                square.y = HEIGHT - square.size
                if abs(square.vy) > 5:
                    square.vy = -square.vy * e
                else:
                    square.vy = 0
                    if(square.vx != 0):
                        friction_acc = gravity.stone()
                        if square.vx > 0:
                            square.vx -= friction_acc * dt
                            if square.vx < 0:
                                square.vx = 0
                        else:
                            square.vx += friction_acc * dt
                            if square.vx > 0:
                                square.vx = 0
                    print("friction applied, vx:", square.vx)
                
            elif square.y < 0:
                square.y = 0
                square.vy = -square.vy * e
            
            if square.x + square.size >= WIDTH:
                square.x = WIDTH - square.size
                square.vx = -square.vx * e
                
            elif square.x < 0:
                square.x = 0
                square.vx = -square.vx * e
    
    # Draw squares
    for square in squares:
        square.draw(screen)
        
    

    pygame.display.flip()                  

pygame.quit()                               
