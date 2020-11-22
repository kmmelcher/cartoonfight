"""
This module contains some loading functions.
"""
import pygame
import os


SRC_PATH = os.path.dirname (__file__)
RESOURCES_PATH = os.path.join(SRC_PATH,'../resources')

def load_images(directory,accept=(".png",".jpg")):
	"""
	Load images with extensions in the accept argument.
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
	Calls the load_images() function for all directories passed.
	"""
	images_path = os.path.join(RESOURCES_PATH,'images')
	IMAGES = {}
	for directory in directories:
	    path = os.path.join(images_path, directory)
	    IMAGES[directory] = load_images(path)
	return IMAGES

def load_fonts():
	"""
    Create a dictionary of font files in given directory
    if their extensions are in accept.
    """
	accept = ('.ttf')
	fonts_path = os.path.join(RESOURCES_PATH,'fonts')
	fonts = {}
	for font in os.listdir(fonts_path):
	    name,ext = os.path.splitext(font)
	    if ext.lower() in accept:
	        fonts[name] = os.path.join(fonts_path,font)
	return fonts
