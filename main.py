import pygame, sys, os, random

from pygame.locals import *
from ball import *
from paddle import *

class Pong:

	def __init__(self, width=800, height=600):
		