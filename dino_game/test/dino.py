import pygame
class Dino():
    def __init__(self, size_x = -1, size_y = -1):
            self.images, self.rect = load_spritesheet('dino.png' ,5 ,1 ,size_x, size_y, -1)
            self.images1, self.rect1 = load_spritesheet('dino_ducking.png', 2, 1, 59, size_y, -1)
            self.rect.bottom = int(0.98 * height)
            self.rect.left = width / 15
            self.image = self.images[0]
            self.index = 0
            self.counter = 0
            self.score = 0
            self.jumping = False
            self.dead = False
            self.ducking = False
            self.blinking = False
            self.movement = [0, 0]
            self.jump_speed = 11.5

            self.stand_pos_width = self.rect.width
            self.duck_pos_width = self.rect1.width


    def draw(self):
        game_display.blit(self.image, self.rect)


    def checkbounds(self):
        if self.rect.bottom > int(0.98 * height):
            self.rect.bottom = int(0.98 * height_screen)
            self.jumping = False


    def update(self):
        if self.jumping:
            self.movement[1] = self.movement[1] + gravity

        if self.jumping:
            self.index = 0
        elif self.blinking:
            if self.index == 0:
                if self.counter % 400 == 399:
                    self.index = (self.index + 1) % 2
                elif self.counter % 20 == 19:
                    self.index = (self.index + 1) % 2

        elif self.ducking:
            if self.counter % 5 == 0:
                self.index = (self.index + 1) % 2
        else:
            if self.counter % 5 == 0:
                self.index = (self.index + 1) % 2 + 2
            if self.dead:
                self.index = 4
            if not self.ducking:
                self.image = self.images[self.index]
                self.rect.width = self.stand_pos_width
            else:
                self.image = self.images1[(self.index) % 2]
                self.rect.width = self.duck_pos_width


            self.rect = self.rect.move(self.movement)
            self.checkbounds()

            if not self.dead and self.counter % 7 == 6 and self.blinking == False:
                self.score += 1
                if self.score % 100 == 0 and self.score != 0:
                    if pygame.mixer.get_init() != None:
                        sound_checkpoint.play()
            self.counter = (self.counter + 1)

