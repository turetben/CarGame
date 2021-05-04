import pygame
import sys
from pygame.locals import *  # TODO: change to specific imports
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
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display_surface.fill(WHITE)
pygame.display.set_caption("pycar-racing")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ASSETS_PATH / "Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center=(160, 520))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Beginning Game Loop
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display_surface.blit(background, (0, 0))
    for entity in all_sprites:
        display_surface.blit(entity.image, entity.rect)
        entity.move()

    FramePerSec.tick(FPS)
