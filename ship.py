import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self, ai_settings, screen):
		super().__init__()
	#przypisanie pobranych argumentów
		self.screen = screen
		self.ai_settings = ai_settings
	#pobranie obrazka
		self.image = pygame.image.load('images/rocket.bmp')
	#funkcja get_rect() dla statku kosm. i okienka
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
	#położenie kwadracika statku kosmicznego
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	#zamiana położenia X na float'a
		self.center = float(self.rect.centerx)
	#ruch statku
		self.moving_right = False
		self.moving_left = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
	#przypisanie położenia statku typu float do 
		self.rect.centerx = self.center


	def blitme(self):
	#wyświetlenie statku kosm.
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.center = self. screen_rect.centerx