import pygame


class Obj(pygame.sprite.Sprite):

    def __init__(self, image, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y


class Pipe(Obj):

    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)

    def update(self, *args):
        self.rect[0] -= 3

        if self.rect[0] <= -100:
            self.kill()

    def move(self):
        self.rect[0] -= 3

        if self.rect[0] <= -100:
            self.kill()


class Coin(Obj):

    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)

        self.ticks = 0

    def update(self, *args):
        self.move()
        self.anim()

    def move(self):
        self.rect[0] -= 3

        if self.rect[0] <= -100:
            self.kill()

    def anim(self):
        self.ticks = (self.ticks + 1) % 6
        self.image = pygame.image.load("assets/"+ str(self.ticks) + ".png")


class Bird(Obj):

    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)

        self.ticks = 0

    def update(self, *args):
        self.anim()
        self.move()

    def anim(self):
        self.ticks = (self.ticks + 1) % 4
        self.image = pygame.image.load("assets/bird"+ str(self.ticks) + ".png")

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            print("voar")