import pygame
from pygame.locals import *

def handle_player_input(player):
    """
    Process keyboard input for player movement and actions.
    Returns False if the game should quit, True otherwise.
    """
    # Handle continuous key presses (like movement)
    keys = pygame.key.get_pressed()
    
    # Reset horizontal velocity
    player.velocity_x = 0
    
    # Move left with A or LEFT arrow
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move_left()
    
    # Move right with D or RIGHT arrow
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move_right()
        
    # Jump with SPACE, UP or W
    if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
        player.jump()
    
    return True