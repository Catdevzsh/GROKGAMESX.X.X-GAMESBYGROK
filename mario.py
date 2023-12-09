import sys
import random
import pygame
from pygame.locals import *

pygame.init()

# Game settings
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Display settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mario Bros')
clock = pygame.time.Clock()

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.centery = SCREEN_HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
        self.jump = False

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 5
        if keystate[pygame.K_SPACE]:
            self.jump = True
        self.rect.x += self.speedx
        if self.jump:
            self.speedy = -15
            self.jump = False
        self.rect.y += self.speedy
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.speedy = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_WIDTH)
        self.rect.y = random.randrange(0, SCREEN_HEIGHT)
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.speedx *= -1
        elif self.rect.left <= 0:
            self.rect.left = 0
            self.speedx *= -1
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.speedy *= -1
        elif self.rect.top <= 0:
            self.rect.top = 0
            self.speedy *= -1

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Mario()
all_sprites.add(player)

for i in range(5):
    e = Enemy()
    all_sprites.add(e)
    enemies.add(e)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
