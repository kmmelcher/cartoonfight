import pygame
import os

from . import tools

#intialization
pygame.init()

#Game display
DISPLAY_SIZE = (850,480)
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE)
DISPLAY_RECT = DISPLAY.get_rect()

#Game title
CAPTION = "Cartoon Fight"
pygame.display.set_caption(CAPTION)

#loading resources
_SUB_DIRECTORIES = ["aang", "backgrounds"]
GRAPHICS = tools.load_graphics_from_directories(_SUB_DIRECTORIES)

#Game backgroud
def draw_window():
	DISPLAY.blit(GRAPHICS['backgrounds']['default'],(0,0))
	pygame.display.update()

#Main loop
def game_loop():

	run = True

	while run:

		#Quit Game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw_window()

	pygame.quit()

