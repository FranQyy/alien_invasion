class Settings():
	def __init__(self):
	#okienko
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (0, 0, 102)
	#statek
		self.ships_limit = 2
	#posisk
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 255, 255, 255
		self.bullets_allowed = 5
	#obcy
		self.fleet_drop_speed = 5
	#zmiana szybkości gry
		self.speedup_scale = 1.3
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed_factor = 2.0
		self.bullet_speed_factor = 3.5
		self.alien_speed_factor = 1.5
		self.fleet_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_points *= self.speedup_scale
