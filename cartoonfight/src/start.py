import pygame
from pygame.locals import *

from . import tools,player


pygame.init()

#Timer
clock = pygame.time.Clock()
"""
Frames Per Second
so far we have 9 sprites for the movement of
each character so it makes two full animations per second
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

#Scale background
background = pygame.transform.scale(IMAGES['backgrounds']['default'], DISPLAY_SIZE)
	
playerOne = player.Player(100, (40,48,0,128), True, DISPLAY)
playerTwo = player.Player(100, (40,48,28,100), False, DISPLAY)

def draw_window():
	DISPLAY.blit(background,(0,0))

	playerOne.draw(IMAGES['aang'])
	playerTwo.draw(IMAGES['aang'])
	
	pygame.display.update()

def game_loop():

	run = True

	while run:

		#User hit key
		for event in pygame.event.get():
			#Quit Game
			if event.type == QUIT:
				run = False

		#User press key
		user_press = pygame.key.get_pressed()
		
		"""
		Player One Controls
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
		Player Two Controls
		"""
		if user_press[K_RIGHT]:
			playerTwo.move_right()
		elif user_press[K_LEFT]:
			playerTwo.move_left()
		else:
			playerTwo.stand()
		if user_press[K_UP] or playerTwo.jumping:
			playerTwo.jump()
		if user_press[K_RCTRL] or playerTwo.basic_attack_left or playerTwo.basic_attack_right:
			playerTwo.basic_attack(playerOne)

		draw_window()
		clock.tick(FPS)

	pygame.quit()
