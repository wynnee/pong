#created while working/teaching at Vision Tech Camps 
#following class materials made by Rahul Khurana

import pygame, sys, os, random
from pygame.locals import *
from ball import *
from paddle import *

class Pong:

	def __init__(self, width=800, height=600):
		pygame.init()

		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.clock = pygame.time.Clock()

		self.paddle1 = Paddle(50, self.height//2)
		self.paddle2 = Paddle(self.width-50, self.height//2)
		self.dir1 = ""
		self.dir2 = ""
		self.paddle1_sprite = pygame.sprite.renderPlain((self.paddle1))
		self.paddle2_sprite = pygame.sprite.renderPlain((self.paddle2))

		self.ball = Ball(self.width//2, self.height//2)
        self.ball_sprite = pygame.sprite.RenderPlain((self.ball))

        self.p1score = 0
        self.p2score = 0

        self.font = pygame.font.SysFont(None, 24)
        self.p1ScoreText = self.font.render('P1: ', True, (255, 255, 255), (0, 0, 0))
        self.p1ScoreRect = self.p1ScoreText.get_rect()
        self.p1ScoreRect.centerx = 50
        self.p1ScoreRect.centery = 50
        self.p2ScoreText = self.font.render('P2: ', True, (255, 255, 255), (0, 0, 0))
        self.p2ScoreRect = self.p2ScoreText.get_rect()
        self.p2ScoreRect.centerx = self.width-50
        self.p2ScoreRect.centery = 50


    def loop(self):
    	while True:
    		self.clock.tick(30)
    		self.screen.fill(Color(0,0,0))

    		#check for key presses and events
    		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
    				sys.exit()
    			#w, s for player 1, up and down arrows for player 2
    			elif event.type == pygame.KEYDOWN:
    				if event.key == K_w:
                        self.p1dir = "UP"
                    elif event.key == K_s:
                        self.p1dir = "DOWN"
    				if event.key == K_UP:
                        self.p2dir = "UP"
                    elif event.key == K_DOWN:
                        self.p2dir = "DOWN"
                #when player lets go of key, stop moving
                elif event.type == pygame.KEYUP:
                    if event.key == K_UP or event.key == K_DOWN:
                        self.p2dir = ""
                    if event.key == K_w or event.key == K_s:
                        self.p1dir = ""
              
            #check for collisions and victory conditions before moving ball/paddles


            #move ball/paddles

            self.ball.move()
            self.paddle1.move(self.p1dir)
            self.paddle2.move(self.p2dir)

            #update scores

            self.p1ScoreText = self.font.render('P1: ' + str(self.p1score), True, (255, 255, 255), (0, 0, 0))
            self.p2ScoreText = self.font.render('P2: ' + str(self.p2score), True, (255, 255, 255), (0, 0, 0))

            #update display using flip

            pygame.display.flip()



    def checkCollisions(self, paddle1, paddle2, ball):


    def checkScore(self):
    	if self.ball.rect.x > self.width:
            self.p1score += 1
            self.ball.__init__(self.width/2, self.height/2)

        if self.ball.rect.x < 0:
            self.p2score += 1
            self.ball.__init__(self.width/2, self.height/2)


if __name__ == "__main__":
    MainWindow = Pong()
    MainWindow.loop()