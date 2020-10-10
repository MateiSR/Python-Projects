import pygame, random

class Birds(pygame.sprite.Sprite):
    def __init__(self, speed = 5, self_x = -1, self_y = -1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images, self_rect = load_spritesheet("birds.png", 2, 1, size_x, size_y, -1)
        self.birds_height = [height * 0.82, height * 0.75, height * 0.60]
        self.rect.centery = self.birds_height[random.randrange(0, 3)]
        self.rect.left = width + self.rect.width
        self.image = self.images[0]
        self.movement = [-1 * speed, 0]
        self.index = 0
        self.counter = 0

    def draw(self):
        game_display.blit(self.image, self.rect)


    def update(self):
        if self.counter % 10 == 0:
            self.index = (self.index + 1) % 2
        self.image = self.images[self.index]
        self.rect = self.rect.move(self.movement)
        self.counter = (self.counter + 1)
        if self.rect.right < 0:
            self.kill()