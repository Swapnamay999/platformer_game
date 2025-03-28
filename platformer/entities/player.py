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
        self.original_x = x
        self.original_y = y

        # Movement attributes
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 8
        self.jump_power = 15
        self.gravity = 0.8
        self.on_ground = False
        self.acceleration = 0.8  # Increased for more responsive movement
        self.deceleration = 0.6  # Adjusted for smoother deceleration
        self.min_velocity = 0.1  # Minimum velocity threshold

    def update(self, platforms, screen_width, screen_height):
        # Apply gravity
        self.velocity_y += self.gravity

        # Apply horizontal acceleration/deceleration
        if self.velocity_x > 0:
            self.velocity_x = max(0, self.velocity_x - self.deceleration)
            if self.velocity_x < self.min_velocity:
                self.velocity_x = 0
        elif self.velocity_x < 0:
            self.velocity_x = min(0, self.velocity_x + self.deceleration)
            if self.velocity_x > -self.min_velocity:
                self.velocity_x = 0

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
        self.velocity_x = max(-self.speed, self.velocity_x - self.acceleration)

    def move_right(self):
        self.velocity_x = min(self.speed, self.velocity_x + self.acceleration)

    def stop(self):
        # Don't immediately stop, let the deceleration handle it
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def reset_position(self):
        self.rect.x = self.original_x
        self.rect.y = self.original_y
        self.velocity_x = 0
        self.velocity_y = 0
