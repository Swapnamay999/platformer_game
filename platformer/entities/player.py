import pygame
from pygame.locals import *

class Player:
    def __init__(self, x, y):
        # Create a 25x25 red square player
        self.width = 25
        self.height = 25
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Movement attributes
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5
        self.jump_power = 15
        self.gravity = 1
        self.on_ground = False
    
    def update(self, platforms, screen_width, screen_height):
        # Apply gravity
        self.velocity_y += self.gravity
        
        # Update horizontal position
        self.rect.x += self.velocity_x
        
        # Check screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity_x = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
            self.velocity_x = 0
        
        # Check horizontal collisions
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_x > 0:  # Moving right
                    self.rect.right = platform.rect.left
                elif self.velocity_x < 0:  # Moving left
                    self.rect.left = platform.rect.right
        
        # Update vertical position
        self.rect.y += self.velocity_y
        self.on_ground = False
        
        # Check vertical collisions
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Moving down
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.velocity_y = 0
                elif self.velocity_y < 0:  # Moving up
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0
        
        # Check vertical screen boundaries
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity_y = 0
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.velocity_y = 0
            self.on_ground = True
    
    def jump(self):
        if self.on_ground:
            self.velocity_y = -self.jump_power
    
    def move_left(self):
        self.velocity_x = -self.speed
    
    def move_right(self):
        self.velocity_x = self.speed
    
    def stop(self):
        self.velocity_x = 0
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)