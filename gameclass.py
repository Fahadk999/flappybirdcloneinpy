import pygame

class Player (pygame.sprite.Sprite):
    def __init__ (self, x, y, g, jumpF):
        super().__init__()

        self.image = pygame.image.load("FlappyBird/circle.png").convert_alpha()

        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel_y = 0
        self.g = g
        self.jumpF = jumpF

    def update (self):
        self.vel_y += self.g

        self.rect.y += self.vel_y


    def jump (self):
        self.vel_y = self.jumpF


class Pipe (pygame.sprite.Sprite):
    def __init__ (self, x, y, position):
        super().__init__()

        self.image = pygame.image.load("FlappyBird/newpipetaller.png")

        self.image = pygame.transform.scale(self.image, (100, 500))

        if position == "bottom":
            self.image = pygame.transform.flip(self.image, False, True)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update (self):
        self.rect.x -= 5

        if self.rect.x < -150:
            self.kill()

    