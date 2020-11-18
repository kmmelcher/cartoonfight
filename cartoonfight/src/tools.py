"""
This module contains some loading functions.
"""
import pygame
import os


SRC_PATH = os.path.dirname (__file__)
RESOURCES_PATH = os.path.join(SRC_PATH,'../resources')

def load_images(directory,accept=(".png",".jpg")):
	"""
	Load all images with extensions in the accept argument.
	"""
	images = {}
	for pic in os.listdir(directory):
	    name,extension = os.path.splitext(pic)
	    if extension.lower() in accept:
	        img = pygame.image.load(os.path.join(directory,pic))
	        images[name]=img
	return images

def load_images_from_directories(directories):
	"""
	Calls the load_all_images() function for all directories passed.
	"""
	images_path = os.path.join(RESOURCES_PATH,'images')
	IMAGES = {}
	for directory in directories:
	    path = os.path.join(images_path, directory)
	    IMAGES[directory] = load_images(path)
	return IMAGES
