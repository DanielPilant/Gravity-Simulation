from numpy import sin
import pygame
import sys

from core.buttons.general_button import Button
from core.functions.generate_random_objects import generate_random_objects
from entities.square import Square
from physics.collision import is_colliding, resolve_collision
from physics.world import EarthGravity, MoonGravity, SunGravity
from entities.objects import squares_in_game

pygame.init()                               

# Constants and setup
FPS = 144
WIDTH, HEIGHT = 1000, 900                    
screen = pygame.display.set_mode((WIDTH, HEIGHT))   
pygame.display.set_caption("Square Demo")   

def set_gravity(planet):
    global gravity
    if planet == "sun":
        gravity = SunGravity()
    elif planet == "earth":
        gravity = EarthGravity()
    elif planet == "moon":
        gravity = MoonGravity()
        
def set_friction(friction_type_choice):
    global friction_type
    if friction_type_choice == "stone":
        friction_type = "stone"
    elif friction_type_choice == "oil":
        friction_type = "oil"
    elif friction_type_choice == "ice":
        friction_type = "ice"

# Game variables
clock = pygame.time.Clock()
dt = 1/FPS 
e = 0.7 # coefficient of restitution
offset_x = 0
offset_y = 0
running = True
mouse_pre_vx = 0
mouse_pre_vy = 0
throw_strength = 0.5  # scale if needed
gravity = EarthGravity() # default to Earth gravity
friction_type = "stone" # default to stone friction
generate_sqr_button = Button(
    x=WIDTH - 320,
    y=10,
    w=300,
    h=60,
    text="Add Square",
    callback=generate_random_objects
)

select_planet_earth = Button(
    x=10,
    y=10,
    w=200,
    h=40,
    text="Earth Gravity",
    callback=lambda: set_gravity("earth")
)

select_planet_sun = Button(
    x=10,
    y=60,
    w=200,
    h=40,
    text="Sun Gravity",
    callback=lambda: set_gravity("sun")
)

select_planet_moon = Button(
    x=10,
    y=110,
    w=200,
    h=40,
    text="Moon Gravity",
    callback=lambda: set_gravity("moon")
)

select_friction_stone = Button(
    x=220,
    y=10,
    w=200,
    h=40,
    text="Stone Friction",  
    callback=lambda: set_friction("stone")
)

select_friction_oil = Button(
    x=220,
    y=60,
    w=200,
    h=40,
    text="Oil Friction",
    callback=lambda: set_friction("oil")
)

select_friction_ice = Button(
    x=220,
    y=110,
    w=200,
    h=40,
    text="Ice Friction",
    callback=lambda: set_friction("ice")
)

# Main game loop
while running:
    
    screen.fill((30, 30, 30))
    clock.tick(FPS)
                    
    mx, my = pygame.mouse.get_pos()
    mouse_vx = (mx - mouse_pre_vx) / dt
    mouse_vy = (my - mouse_pre_vy) / dt

    mouse_pre_vx = mx  
    mouse_pre_vy = my
    
      
    # Draw button
    generate_sqr_button.draw(screen)
    
    
    # Handle events
    for event in pygame.event.get():
        generate_sqr_button.handle_event(event) 
        select_planet_earth.handle_event(event)
        select_planet_sun.handle_event(event)
        select_planet_moon.handle_event(event)   
        select_friction_stone.handle_event(event)
        select_friction_oil.handle_event(event)
        select_friction_ice.handle_event(event)
                
        if event.type == pygame.QUIT:       
            running = False 
            
        # drag squares with mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            for square in squares_in_game:
                if square.x <= mx <= square.x + square.size and \
                   square.y <= my <= square.y + square.size:
                    square.dragging = True
                    square.vy = 0.0  # reset vertical velocity when picked up
                    square.vx = 0.0  # reset horizontal velocity when picked up
                    break
                
        if event.type == pygame.MOUSEBUTTONUP:
            for square in squares_in_game:
                if square.dragging:
                    square.dragging = False
                    square.vx = mouse_vx * throw_strength
                    square.vy = mouse_vy * throw_strength

    # Update squares
    for square in squares_in_game:
        
        if square.dragging:
            square.x = mx - square.size / 2
            square.y = my - square.size / 2
        else:
            square.vy += gravity.acceleration * dt
            square.x += square.vx * dt
            square.y += square.vy * dt
            print(square.vy)

            if square.y + square.size >= HEIGHT:
                square.y = HEIGHT - square.size

                square.vy = -square.vy * e
               
                if(square.vx != 0):
                    friction_acc = 0
                    if friction_type == "stone":
                        friction_acc = gravity.stone()
                    elif friction_type == "oil":
                        friction_acc = gravity.oil()
                    elif friction_type == "ice":
                        friction_acc = gravity.ice()
                    if square.vx > 0:
                        square.vx -= friction_acc * dt
                        if square.vx < 0:
                            square.vx = 0
                    else:
                        square.vx += friction_acc * dt
                        if square.vx > 0:
                            square.vx = 0
                
            elif square.y < 0:
                square.y = 0
                square.vy = -square.vy * e
            
            if square.x + square.size >= WIDTH:
                square.x = WIDTH - square.size
                square.vx = -square.vx * e
                
            elif square.x < 0:
                square.x = 0
                square.vx = -square.vx * e
    
    for i in range(len(squares_in_game)):
        for j in range(i + 1, len(squares_in_game)):
            a = squares_in_game[i]
            b = squares_in_game[j]
            if is_colliding(a, b):
                resolve_collision(a, b, e)
             
    # Draw squares
    for square in squares_in_game:
        square.draw(screen)
      
    select_planet_earth.draw(screen)
    select_planet_sun.draw(screen)
    select_planet_moon.draw(screen)
    
    select_friction_stone.draw(screen)
    select_friction_oil.draw(screen)
    select_friction_ice.draw(screen)

    pygame.display.flip()                  

pygame.quit()                               
