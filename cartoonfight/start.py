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
    KEYDOWN,
    QUIT,
)


pygame.init()

#Frames Per Second
clock = pygame.time.Clock()
FPS = 6

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
	
xOne = 10
xTwo = DISPLAY_SIZE[0]-138
FLOOR = DISPLAY_SIZE[1]-228

playerOne = player.Player([xOne,FLOOR], 100, (128,128), True, DISPLAY)
playerTwo = player.Player([xTwo,FLOOR], 100, (128,128), False, DISPLAY)

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
		if user_press[K_d]:
			playerOne.position[0] += playerOne.speed
			playerOne.right = True
			playerOne.left = False
			playerOne.standingRight = False
			playerOne.standingLeft = False
		elif user_press[K_a]:
			playerOne.position[0] -= playerOne.speed
			playerOne.left = True
			playerOne.right = False
			playerOne.standingRight = False
			playerOne.standingLeft = False
		else:
			if playerOne.right:
				playerOne.standingRight = True
			elif playerOne.left:
				playerOne.standingLeft = True


		if user_press[K_RIGHT]:
			playerTwo.position[0] += playerTwo.speed
			playerTwo.right = True
			playerTwo.left = False
			playerTwo.standingRight = False
			playerTwo.standingLeft = False
		elif user_press[K_LEFT]:
			playerTwo.position[0] -= playerTwo.speed
			playerTwo.left = True
			playerTwo.right = False
			playerTwo.standingRight = False
			playerTwo.standingLeft = False
		else:
			if playerTwo.right:
				playerTwo.standingRight = True
			elif playerTwo.left:
				playerTwo.standingLeft = True

			playerTwo.right = False
			playerTwo.left = False

		draw_window()
		clock.tick(FPS)

	pygame.quit()