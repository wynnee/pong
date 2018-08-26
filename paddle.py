import os, sys, random, pygame
from pygame.locals import *

class Paddle(pygame.sprite.Sprite):
	def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.width = 20
        self.height = 100
        self.image = pygame.image.load("paddle.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

    def move(self, dir):
        if dir == "UP":
            self.rect.move_ip(0,-10)
        elif dir == "DOWN":
            self.rect.move_ip(0,10)