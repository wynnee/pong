import os, sys, random, pygame, math
from pygame.locals import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 10
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.speed = 15
        #random angle between 0 and 2pi
        self.angle = random.uniform(0,2*math.pi)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

    #flip the x component of the direction by subtracting from pi
    def flipX(self):
        self.angle = (math.pi) - self.angle
        
    #move in the x direction speed*x of angle and in y direction speed*y of angle
    def move(self, height):
        self.checkWallCollisions(height)
        self.rect.move_ip(self.speed * math.cos(self.angle), self.speed * math.sin(self.angle))
       
    #ball should bounce off horizontal walls in pong
    def checkWallCollisions(self, height):
        if self.rect.y < 0 or self.rect.y > height - self.radius*2:
            self.angle = -self.angle