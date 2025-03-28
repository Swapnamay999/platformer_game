import pygame

class Camera:
    def __init__(self, screen_width, screen_height, level_width):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.level_width = level_width
        self.camera_x = 0

    def update(self, player_x):
        screen_center = self.screen_width // 2
        if player_x > screen_center:
            target_camera_x = player_x - screen_center
            self.camera_x = max(0, min(target_camera_x, self.level_width - self.screen_width))

    def draw(self, surface, level_surface):
        surface.blit(level_surface, (0, 0), 
                    (self.camera_x, 0, self.screen_width, self.screen_height))
