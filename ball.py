import os, sys, random, pygame, math
from pygame.locals import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
    	pygame.sprite.Sprite.__init__(self)
        self.radius = 10
        self.image = pygame.image.load("ball.png").convert_alpha()
        self.speed = 15
        #random direction between 0 and 2pi
        self.angle = random.uniform(0,2*math.pi)
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY

    #flip the x component of the direction by subtracting from pi
    def flipX(self):
        self.angle = (math.pi) - self.angle

    #flip the y component of the direction by negating 
    def flipY(self):
        self.dir = -self.dir

    #move in the x direction speed*x of angle and in y direction speed*y of angle
    def move(self):
    	self.checkWallCollisions()
        self.rect.move_ip(self.speed * math.cos(self.dir), self.speed * math.sin(self.dir))
       
    #ball should bounce off horizontal walls in pong
    def checkWallCollisions(self):
    	if self.rect.y < 0 or self.rect.y > self.height - self.radius*2:
    		self.flipY