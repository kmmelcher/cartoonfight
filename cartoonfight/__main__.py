import pygame

from .src import start


def main():
	start.game_loop()
	pygame.quit()

if __name__ == '__main__':
    main()