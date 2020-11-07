import pygame

pygame.init()

#Display size
display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width,display_height))

#Game title
pygame.display.set_caption('Cartoon Fight')

def game_loop():

	run = True

	while run:

		#Quit Game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

	pygame.quit()

game_loop()