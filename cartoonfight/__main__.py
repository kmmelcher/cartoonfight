import pygame

from .data import tools, prepare


def main():
	prepare.game_loop()
	pygame.quit()

if __name__ == '__main__':
    main()