import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight):
        super().__init__()
        self.RADIUS = 10
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.circle = pygame.Surface((self.RADIUS, self.RADIUS))
        self.rect = self.circle.get_rect()
        self.circle.fill(self.color)
        self.rect.y = 250
        self.rect.x = 200
        self.speedx = 6
        self.speedy = 4
        self.score = 0

    def move(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top <= 0:
             self.speedy = -self.speedy
        if self.rect.bottom >= self.windowHeight:
            self.speedy = self.speedy
        if self.rect.left <= 0:
            self.speedx = -self.speedx
        if self.rect.right >= self.windowWidth:
            self.speedx = -self.speedx
        pass

    def collide_block(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.speedy = -self.speedy
            self.score += 1  # creates score
            return True

    def collide_paddle(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.speedy = -self.speedy

