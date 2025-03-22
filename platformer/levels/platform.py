import pygame

class Platform:
    def __init__(self, x, y, width, height, color=(100, 100, 100)):  # Default gray color
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect) 