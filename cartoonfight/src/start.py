import sys
import pygame
from pygame.locals import *

from . import tools, character


pygame.init()

#Timer
clock = pygame.time.Clock()
"""
Frames Per Second
"""
FPS = 27

#Game display
monitor = pygame.display.Info()
DISPLAY_SIZE = (monitor.current_w, monitor.current_h)
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE)

#Game title
CAPTION = "Cartoon Fight"
pygame.display.set_caption(CAPTION)

#load images
_SUB_DIRECTORIES = ['aang','goblin','warrior','backgrounds']
IMAGES = tools.load_images_from_directories(_SUB_DIRECTORIES)

#load fonts
FONTS = tools.load_fonts()

#Scale background
background = pygame.transform.scale(
	IMAGES['backgrounds']['air_temple'],
	DISPLAY_SIZE,
)
	
playerOne = character.Aang(True, IMAGES, DISPLAY)
playerTwo = character.Aang(False, IMAGES, DISPLAY)

def draw_window():
	DISPLAY.blit(background,(0,0))

	playerOne.draw(FONTS['default'])
	playerTwo.draw(FONTS['default'])
	
	pygame.display.update()

def game_loop():
	run = True
	
	while run:

		for event in pygame.event.get():
			#Quit Game
			if event.type == QUIT:
				run = False

		#User press key
		user_press = pygame.key.get_pressed()

		"""
		Player One press keys
		"""
		if user_press[K_d]:
			playerOne.move_right()
		elif user_press[K_a]:
			playerOne.move_left()
		else:
			playerOne.stand()
		if user_press[K_w] or playerOne.jumping:
			playerOne.jump()
		if user_press[K_f] or playerOne.basic_attack_left or playerOne.basic_attack_right:
			playerOne.basic_attack(playerTwo)

		"""
		Player Two press keys
		"""
		if user_press[K_RIGHT]:
			playerTwo.move_right()
		elif user_press[K_LEFT]:
			playerTwo.move_left()
		else:
			playerTwo.stand()
		if user_press[K_UP] and playerTwo.jumping:
			playerTwo.double_jump()
		if user_press[K_UP] or playerTwo.jumping:
			playerTwo.jump()
		
		
		if user_press[K_RCTRL] or playerTwo.basic_attack_left or playerTwo.basic_attack_right:
			playerTwo.basic_attack(playerOne)

		draw_window()
		clock.tick(FPS)

	#Both methods are needed to avoid underrun error
	pygame.quit()
	sys.exit()
