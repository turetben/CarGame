import pygame
import sys
import random
from pygame.locals import *
from pathlib import Path

# Initialize program
pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

# Root path to our assets
ASSETS_PATH = Path("Assets")
background = pygame.image.load(ASSETS_PATH / "AnimatedStreet.png")
player_image = pygame.image.load(ASSETS_PATH / "Player.png")

# Setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup a 300x300 pixel display with caption
SCREEN_WIDTH = 381
SCREEN_HEIGHT = 570
speed = 5
score = 0
speed_increase = 1
MAX_SPEED = 10

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display_surface.fill(WHITE)
pygame.display.set_caption("pycar-racing")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ASSETS_PATH / "Enemy.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), -50))

    def move(self):
        global score
        global speed
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_HEIGHT:
            score += 1
            if speed <= MAX_SPEED:
                speed += speed_increase
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ASSETS_PATH / "Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center=(160, 500))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

player = Player()
enemy1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(enemy1)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy1)

background_position = 0

# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if random.randint(0, 100) < 1:
        e = Enemy()
        enemies.add(e)
        all_sprites.add(e)

    display_surface.blit(background, (0, background_position))
    display_surface.blit(background, (0, background_position - SCREEN_HEIGHT + 10))
    background_position += speed
    background_position %= SCREEN_HEIGHT
    for entity in all_sprites:
        display_surface.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(player, enemies):
        print(score)
        for entity in all_sprites:
            entity.kill()
        pygame.quit()
        sys.exit()

    FramePerSec.tick(FPS)
