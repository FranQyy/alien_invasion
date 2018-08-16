import pygame
import random
import sys
from pygame.sprite import Sprite


class Star(Sprite):
	def __init__(self, ai_settings, screen):
		super().__init__()

		self.screen = screen
		self.image = pygame.image.load('images/star.bmp')
		self.image_rect = self.image.get_rect()

		self.MOVE = pygame.USEREVENT
		pygame.time.set_timer(self.MOVE, 1000)
		self.image_rect.x = random.choice(range(0,1200))
		self.image_rect.y = random.choice(range(0,700))

	def blit(self):
		self.screen.blit(self.image, self.image_rect)	

