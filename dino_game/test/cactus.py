import pygame, random

class Cactus(pygame.sprite.Sprite):
    def __init__(self, speed = 5, size_x = -1, size_y = -1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self.rect = load_spritesheet("cactus-small.png", 3, 1, size_x, size_y, -1)
        self.rect.bottom = int(0.98 * height)
        self.rect.left = width_screen + self.rect.width
        self.image = self.images[random.randrange(0, 3)]
        self.movement = [-1 * speed, 0]


    def draw(self):
        game_display.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()