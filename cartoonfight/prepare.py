import pygame
import os

import tools
import player
#intialization
pygame.init()

#Game display
DISPLAY_SIZE = (850,480)
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE)
DISPLAY_RECT = DISPLAY.get_rect()


clock = pygame.time.Clock()
FPS = 5

#Game title
CAPTION = "Cartoon Fight"
pygame.display.set_caption(CAPTION)

#loading resources
_SUB_DIRECTORIES = ["backgrounds"]
GRAPHICS = tools.load_graphics_from_directories(_SUB_DIRECTORIES)

#Game backgroud
def draw_window():
	DISPLAY.blit(GRAPHICS['backgrounds']['default'],(0,0))

	player1.draw()
	player2.draw()
	
	pygame.display.update()
	
player1 = player.Player((10,300), 100, (128,128), True, DISPLAY_SIZE, DISPLAY)
player2 = player.Player((700,300), 100, (128,128), False, DISPLAY_SIZE, DISPLAY)

#Main loop
def game_loop():

	run = True

	while run:

		#Quit Game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw_window()
		clock.tick(FPS)
	

	pygame.quit()

