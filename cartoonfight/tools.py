"""
This module contains some resource loading functions.
"""
import pygame
import os


def load_all_graphics(directory,accept=(".png",".jpg")):
	"""
	Load all graphics with extensions in the accept argument.
	"""
	graphics = {}
	for pic in os.listdir(directory):
	    name,extension = os.path.splitext(pic)
	    if extension.lower() in accept:
	        img = pygame.image.load(os.path.join(directory,pic))
	        graphics[name]=img
	return graphics


def load_graphics_from_directories(directories):
	"""
	Calls the load_all_graphics() function for all directories passed.
	"""
	#Get path from directory above
	
	base_path = os.path.join('images')
	GRAPHICS = {}
	for directory in directories:
	    path = os.path.join(base_path, directory)
	    GRAPHICS[directory] = load_all_graphics(path)    
	return GRAPHICS
