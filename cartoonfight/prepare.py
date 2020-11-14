import pygame

from . import tools,player


pygame.init()

clock = pygame.time.Clock()
FPS = 5

#Game display
monitor = pygame.display.Info()
DISPLAY_SIZE = (monitor.current_w, monitor.current_h)
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE)
DISPLAY_RECT = DISPLAY.get_rect()

#Game title
CAPTION = "Cartoon Fight"
pygame.display.set_caption(CAPTION)

#load images
_SUB_DIRECTORIES = ['aang','goblin','warrior','backgrounds']
IMAGES = tools.load_images_from_directories(_SUB_DIRECTORIES)

#Scale background
background = pygame.transform.scale(IMAGES['backgrounds']['default'], DISPLAY_SIZE)
	
playerOne = player.Player((10,316), 100, (128,128), True, DISPLAY)
playerTwo = player.Player((700,380), 100, (64,64), False, DISPLAY)

def draw_window():
	DISPLAY.blit(background,(0,0))

	playerOne.draw(IMAGES['aang'])
	playerTwo.draw(IMAGES['goblin'])
	
	pygame.display.update()
	

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