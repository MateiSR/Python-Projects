import pygame
import os
pygame.init()  # Ininializing pygame library
RLEACCEL = pygame.RLEACCEL

width, height = 600, 300
size = (width, height)
gravity = 0.6

game_display = pygame.display.set_mode(size)
pygame.display.set_caption("Dino Run - pygame")


def check_exit():  # Checks for exit signal
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


def load_image(name, size_y = -1, size_x = -1, colorkey = None):
    full_path = os.path.join("resources", name)
    image = pygame.image.load(full_path)
    image = image.convert()

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)  #RLEACCEL = run length encoding acceleration

    if size_x != -1 or size_y != -1:
        image = pygame.transform.scale(image, (size_x, size_y))
    image_rect = image.get_rect()

    return (image, image_rect)


def load_spritesheet(sheet_name, name_x, name_y, scale_x = -1, scale_y = -1, colorkey = None):
    full_path = os.path.join("resources", sheet_name)
    sheet = pygame.image.load(full_path)
    sheet = sheet.convert()

    sheet_rect = sheet.get_rect()

    sprites = []

    size_x = sheet_rect.width / name_x
    size_y = sheet_rect.height / name_y

    for i in range(0, name_y):
        for j in range(0, name_x):
            rect = pygame.Rect((j * size_x, i * size_y, size_x, size_y))
            image = pygame.Surface(rect.size)
            image.convert()
            image.blit(sheet, (0, 0), rect)

            if colorkey is not None:
                if colorkey == -1:
                    colorkey = image.get_at((0, 0))
                    image.set_colorkey(colorkey, pygame.RLEACCEL)

            if scale_x != -1 or scale_y != -1:
                image = pygame.transform.scale(image, (scale_x, scale_y))

            sprites.append(image)

        sprite_rect = sprites[0].get_rect()
        return (sprites, sprite_rect)


def display_game_over(retry_button, game_over):
    retry_rect = retry_button.get_rect()
    retry_rect.centerx = width / 2
    retry_rect.top = height * 0.52

    game_over_rect =  game_over.get_rect()
    game_over_rect.centerx = width / 2
    game_over_rect.centery = height * 0.35

    game_display.blit(retry_button, retry_rect)
    game_display.blit(game_over, game_over_rect)

def extract_digits(num):  # big number fixes
    if num > -1:
        d = []
        i = 0
        while (num / 10 != 0):
            d.append(num % 10)
            num = int(num / 10)

        d.append(num % 10)

        for i in range(len(d), 5):
            d.append(0)
        d.reverse()
        return d

highest_scores = 0
game_clock = pygame.time.Clock()
FPS = 60
sound_jump = pygame.mixer.Sound("resources/jump.wav")
sound_die = pygame.mixer.Sound("resources/die.wav")
sound_checkpoint = pygame.mixer.Sound("resources/checkpoint.wav")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
background_color = (235, 235, 235)

def introduction_screen():
    ado_dino = Dino(44,47)
    ado_dino.isBlinking = True
    starting_game = False


    temp_ground, temp_ground_rect = load_spritesheet('ground.png',15,1,-1,-1,-1)
    temp_ground_rect.left = width/20
    temp_ground_rect.bottom = height


    while not starting_game:
        if pygame.display.get_surface() == None:
            print("Couldn't load display surface")
            return True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        ado_dino.isJumping = True
                        ado_dino.isBlinking = False
                        ado_dino.movement[1] = -1*temp_dino.jumpSpeed

        ado_dino.update()

        if pygame.display.get_surface() != None:
            game_display.fill(background_color)
            game_display.blit(temp_ground[0],temp_ground_rect)
            if ado_dino.blinking:
                game_display.blit(logo,logo_rect)
            ado_dino.draw()

            pygame.display.update()

        game_clock.tick(FPS)
        if ado_dino.jumping == False and ado_dino.blinking == False:
            starting_game = True



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


class Ground():
    def __init__(self, speed=-5):
        self.image, self.rect = load_image('ground.png',-1, -1, -1)
        self.image1, self.rect1 = load_image('ground.png',-1, -1, -1)
        self.rect.bottom = height
        self.rect1.bottom = height
        self.rect1.left = self.rect.right
        self.speed = speed

    def draw(self):
        game_display.blit(self.image, self.rect)
        game_display.blit(self.image1, self.rect1)

    def update(self):
        self.rect.left += self.speed
        self.rect1.left += self.speed

        if self.rect.right < 0:
            self.rect.left = self.rect1.right

        if self.rect1.right < 0:
            self.rect1.left = self.rect.right


class Cloud (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image, self.rect = load_image('cloud.png',int(90*30/42), 30, -1)
        self.speed = 1
        self.rect.left = x
        self.rect.top = y
        self.movement = [-1 * self.speed, 0]

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()


class Scoreboard():
    def __init__(self, x= -1, y= -1):
        self.score = 0
        self.screimages, self.screrect = load_spritesheet('numbers.png',12,1,11,int(11*6/5),-1)
        self.image = pygame.Surface((55,int(11*6/5)))
        self.rect = self.image.get_rect()
        if x == -1:
            self.rect.left = width*0.89
        else:
            self.rect.left = x
        if y == -1:
            self.rect.top = height*0.1
        else:
            self.rect.top = y

    def draw(self):
        game_display.blit(self.image, self.rect)

    def update(self,score):
        score_digits = extract_digits(score)
        self.image.fill(background_color)
        for s in score_digits:
            self.image.blit(self.screimages[s],self.screrect)
            self.screrect.left += self.screrect.width
        self.screrect.left = 0


def gameplay():
    global highest_scores
    gamespeed = 4
    start_menu = False
    game_over = False
    game_quit = False
    playerDino = Dino(44, 47)
    new_ground = Ground(-1 * gamespeed)
    scoreboards = Scoreboard()
    highScore = Scoreboard(width * 0.78)
    counter = 0

    cacti = pygame.sprite.Group()
    birds = pygame.sprite.Group()
    clouds = pygame.sprite.Group()
    last_obstacle = pygame.sprite.Group()

    Cactus.containers = cacti
    Birds.containers = birds
    Cloud.containers = clouds

    retry_button, retry_rect = load_image('replay_button.png', 35, 31, -1)
    game_over, game_over_rect = load_image('game_over.png', 190, 11, -1)

    temp_images, temp_rect = load_spritesheet('numbers.png', 12, 1, 11, int(11*6/5), -1)
    ado_image = pygame.Surface((22, int(11*6/5)))
    ado_rect = ado_image.get_rect()
    ado_image.fill(background_color)
    ado_image.blit(temp_images[10], temp_rect)
    temp_rect.left += temp_rect.width
    ado_image.blit(temp_images[11], temp_rect)
    ado_rect.top = height * 0.1
    ado_rect.left = width * 0.73

    logo, logo_rect = load_image('logo.png', 240, 40, -1)
    logo_rect.centerx = width*0.6
    logo_rect.centery = height*0.6

    while not game_quit:
        while start_menu:
            pass
        while not game_over:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
                game_over = True
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            if playerDino.rect.bottom == int(0.98*height):
                                playerDino.isJumping = True
                                if pygame.mixer.get_init() != None:
                                    sound_jump.play()
                                playerDino.movement[1] = -1 * playerDino.jumpSpeed

                        if event.key == pygame.K_DOWN:
                            if not (playerDino.isJumping and playerDino.isDead):
                                playerDino.isDucking = True

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_DOWN:
                            playerDino.isDucking = False
            for c in cacti:
                c.movement[0] = -1*gamespeed
                if pygame.sprite.collide_mask(playerDino,c):
                    playerDino.isDead = True
                    if pygame.mixer.get_init() != None:
                        die_sound.play()

            for b in birds:
                b.movement[0] = -1 * gamespeed
                if pygame.sprite.collide_mask(playerDino,b):
                    playerDino.isDead = True
                    if pygame.mixer.get_init() != None:
                        die_sound.play()

            if len(cacti) < 2:
                if len(cacti) == 0:
                    last_obstacle.empty()
                    last_obstacle.add(Cactus(gamespeed,40,40))
                else:
                    for l in last_obstacle:
                        if l.rect.right < width*0.7 and random.randrange(0,50) == 10:
                            last_obstacle.empty()
                            last_obstacle.add(Cactus(gamespeed, 40, 40))

            if len(birds) == 0 and random.randrange(0,200) == 10 and counter > 500:
                for l in last_obstacle:
                    if l.rect.right < width*0.8:
                        last_obstacle.empty()
                        last_obstacle.add(Birds(gamespeed, 46, 40))

            if len(clouds) < 5 and random.randrange(0,300) == 10:
                Cloud(width,random.randrange(height/5,height/2))

            playerDino.update()
            cacti.update()
            birds.update()
            clouds.update()
            new_ground.update()
            scoreboards.update(playerDino.score)
            highScore.update(highest_scores)

            if pygame.display.get_surface() != None:
                game_display.fill(background_col)
                new_ground.draw()
                clouds.draw(game_display)
                scoreboards.draw()
                if highest_scores != 0:
                    highScore.draw()
                    game_display.blit(ado_image, ado_rect)
                cacti.draw(game_display)
                birds.draw(game_display)
                playerDino.draw()

                pygame.display.update()
            game_clock.tick(FPS)

            if playerDino.isDead:
                game_over = True
                if playerDino.score > highest_scores:
                    highest_scores = playerDino.score

            if counter % 700 == 699:
                new_ground.speed -= 1
                gamespeed += 1

            counter = (counter + 1)

        if game_quit:
            break

        while game_over:
            if pygame.display.get_surface() == None:
                print("Couldn't load display surface")
                game_quit = True
                game_over = False
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_quit = True
                        game_over = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_quit = True
                            game_over = False

                        if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                            game_over = False
                            gameplay()
            highScore.update(highest_scores)
            if pygame.display.get_surface() != None:
                display_game_over(retry_button, game_over)
                if highest_scores != 0:
                    highScore.draw()
                    game_display.blit(ado_image, ado_rect)
                pygame.display.update()
            game_clock.tick(FPS)

    pygame.quit()
    quit()

"""
while True:  # Infinite game loop, keeps process running
    check_exit()
    pygame.draw.rect(game_display, white, [30, 30, 40, 50])
    pygame.display.update()
"""
def main():
    isGameQuit = introduction_screen()
    if not isGameQuit:
        gameplay()

main()