import pygame

from .player import Player

class Aang(Player):
	
	def __init__(self, is_player_one, sprites, display):
		super().__init__(is_player_one, sprites, display)
		
		#Characther atributes
		self.name = 'Aang'
		self.sprites = sprites[self.name.lower()]
		self.max_health = 100
		self.health = self.max_health
		self.health_percentage = self.health/self.max_health
		self.base_damage = 10
		"""
		This tuple corresponds to the sprite size based on a 128x128 box:
		xStart, xEnd, yStart, yEnd
		"""
		self.size = (40,48,0,128)
		self.hitbox = pygame.Rect(
            (self.position[0]+self.size[0], self.position[1]+self.size[2]),
            (self.size[1], self.size[3]),
        )

	def double_jump(self):
		#Glide mechanics
		pass