import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from star import Star

import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import pickle 

def run_game():
	pygame.init()
	ai_settings = Settings()

#ustawienia okienka
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Inwazja obcych")
	play_button = Button(ai_settings, screen, "Gra")
#stworzenie statku 'ship' i grupy pocisków 'bullets'
	ship = Ship(ai_settings, screen)
	alien = Alien(ai_settings, screen)
	star = Star(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	stars = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
#pętla gry
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, star, stars)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
			gf.update_stars(stars)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, stars)

run_game()
