import pygame

from . import tools,player

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_a,
    K_d,
    K_w,
    KEYDOWN,
    QUIT,
)


pygame.init()

#Timer
clock = pygame.time.Clock()
"""
Frames Per Second
so far we have 9 sprites for the movement of
each character so it makes two full animations per second
"""
FPS = 18

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
	
playerOneX = 10
playerTwoX = DISPLAY_SIZE[0]-138
FLOOR = DISPLAY_SIZE[1]-228

playerOne = player.Player([playerOneX,FLOOR], 100, (128,128), True, DISPLAY)
playerTwo = player.Player([playerTwoX,FLOOR], 100, (128,128), False, DISPLAY)

def draw_window():
	DISPLAY.blit(background,(0,0))

	playerOne.draw(IMAGES['aang'])
	playerTwo.draw(IMAGES['warrior'])
	
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
			playerOne.jump(FLOOR)

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
			playerTwo.jump(FLOOR)

		draw_window()
		clock.tick(FPS)

	pygame.quit()
