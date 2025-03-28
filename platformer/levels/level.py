from enum import Enum

import pygame

from .platform import Platform
from game.camera import Camera


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (128, 0, 128)


class Level:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.platforms = []
        self.player_spawn_x = 50  # Starting near the left
        self.player_spawn_y = screen_height - 20  # A bit above the ground
        self.level_width = screen_width * 3  # Make level 3x wider than screen
        self.camera = Camera(screen_width, screen_height, self.level_width)

        # Generate the level
        self._generate_level()

    def _generate_level(self):
        # Ground - extend across the entire level width
        ground_height = 20
        self.platforms.append(
            Platform(
                0,
                self.screen_height - ground_height,
                self.level_width,
                ground_height,
                (50, 50, 50),
            )
        )

        # Platform patterns - repeat 3 times
        for i in range(3):
            base_x = i * self.screen_width
            self.platforms.extend([
                Platform(base_x + 200, self.screen_height - 120, 100, 20, Color.RED.value),  # First jump
                Platform(base_x + 400, self.screen_height - 180, 100, 20, Color.GREEN.value),  # Higher platform
                Platform(base_x + 600, self.screen_height - 120, 100, 20, Color.BLUE.value),  # Back down
            ])

    def update_camera(self, player_x):
        self.camera.update(player_x)
        
    def draw(self, surface):
        # Create a temporary surface for the entire level
        level_surface = pygame.Surface((self.level_width, self.screen_height))
        level_surface.fill((0, 0, 0))  # Black background
        
        # Draw all platforms
        for platform in self.platforms:
            platform.draw(level_surface)
            
        # Draw the visible portion of the level using camera
        self.camera.draw(surface, level_surface)
