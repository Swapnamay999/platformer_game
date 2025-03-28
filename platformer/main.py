import pygame
from pygame.locals import *
import os
from entities.player import Player
from utils.input_handler import handle_player_input
from levels.level import Level

class PlatformerGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Platformer Game")
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        # Create the level
        self.current_level = Level(800, 600)
        
        # Create the player
        self.player = Player(self.current_level.player_spawn_x, self.current_level.player_spawn_y)

    def run(self):
        running = True
        while running:
            # Update input and player
            if not handle_player_input(self.player):
                running = False
                
            self.player.update(self.current_level.platforms, 800, 600)
            
            # Draw
            self.screen.fill((0, 0, 0))
            self.current_level.draw(self.screen)
            self.player.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(self.fps)
        
        pygame.quit()

if __name__ == "__main__":
    game = PlatformerGame()
    game.run()
