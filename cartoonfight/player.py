import pygame

import tools


#importinh images of the caracters
_SUB_DIRECTORIES = ["aang"]
GRAPHICS = tools.load_graphics_from_directories(_SUB_DIRECTORIES)

#definition of a player class
class Player(object):

    def __init__(self, position, maxhealth, size, p, displaysize, display):
        self.alive = True
        self.position = position
        self.size = size
        self.maxHealth = maxhealth
        self.health = self.maxHealth
        
        self.standing = False
        self.right = True
        self.left = False
        
        self.framecount = 0
        self.displaySize = displaysize
        self.display = display
        
        self.player1 = p


    def draw(self):

        if self.standing:
            #put here the animation of the standing caracter
            pass
        else:
            if self.right:
                self.display.blit(GRAPHICS['aang']['WR'+str(self.framecount%4)], self.position)
                #put here the animation of right walking caracter
                pass
            elif self.left:
                #put here the animation of left walking caracter
                pass
                
        if self.player1:
		#put here the left health bar
            pass
        else:
		#put here the right health bar
            pass
                
        self.framecount += 1
	
	
	
	
