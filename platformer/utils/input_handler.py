import sys

import pygame
from pygame.locals import *

from entities.player import Player
from utils.config import config


def handle_player_input(player: Player):
    """
    Process keyboard input for player movement and actions.
    Returns False if the game should quit, True otherwise.
    """
    # Handle continuous key presses (like movement)
    keys = pygame.key.get_pressed()

    # Handle movement
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move_left()
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move_right()
    else:
        player.stop()

    # Handle one-time key presses (like jumping)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if (
                event.key == pygame.K_SPACE
                or event.key == pygame.K_UP
                or event.key == pygame.K_w
            ):
                player.jump()

            if config["DEBUG"] and event.key == pygame.K_r:
                player.reset_position()
            if config["DEBUG"] and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    return True
