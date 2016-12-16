import pygame

class Paddle(pygame.sprite.Sprite):

    def __init__(self, color):
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 1
        self.color = color
        self.line = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.rect = self.line.get_rect()
        self.line.fill(self.color)
        self.rect.y = 570



    def move(self):
        x_pos = pygame.mouse.get_pos()[0]
        self.rect.x = x_pos