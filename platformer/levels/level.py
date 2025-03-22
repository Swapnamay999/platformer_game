import pygame
from .platform import Platform

from enum import Enum 

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
        
        # Generate the level
        self._generate_level()
    
    def _generate_level(self):
        # Ground
        ground_height = 20
        self.platforms.append(
            Platform(0, self.screen_height - ground_height, self.screen_width, ground_height, (50, 50, 50))
        )
        
        # Platform patterns
        # First section - Basic jumps
        self.platforms.extend([
            Platform(200, self.screen_height - 120, 100, 20),  # First jump
            Platform(400, self.screen_height - 180, 100, 20),  # Higher platform
            Platform(600, self.screen_height - 120, 100, 20),  # Back down
        ])
        
        # Second section - Vertical challenge
        self.platforms.extend([
            Platform(150, self.screen_height - 250, 80, 20),
            Platform(300, self.screen_height - 320, 80, 20),
            Platform(150, self.screen_height - 390, 80, 20),  # Top platform
        ])
        
        # Third section - Gap jumps
        self.platforms.extend([
            Platform(400, self.screen_height - 200, 60, 20),
            Platform(550, self.screen_height - 200, 60, 20),
            Platform(700, self.screen_height - 200, 60, 20),
        ])
        
        # Some floating platforms for exploration
        self.platforms.extend([
            Platform(300, self.screen_height - 400, 40, 20, (150, 150, 150)),
            Platform(500, self.screen_height - 350, 40, 20, (150, 150, 150)),
            Platform(650, self.screen_height - 450, 40, 20, (150, 150, 150)),
        ])
        
        # Add some walls/vertical platforms
        self.platforms.extend([
            Platform(100, self.screen_height - 120, 20, 100, Color.RED.value),  # Left wall
            Platform(700, self.screen_height - 300, 20, 280, Color.GREEN.value),  # Right wall
        ])
    
    def draw(self, surface):
        for platform in self.platforms:
            platform.draw(surface)
