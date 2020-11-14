import pygame


#definition of a player class
class Player(object):

    def __init__(self, position, maxhealth, size, pOne, display):
        self.display = display
        self.position = position
        self.size = size

        self.maxHealth = maxhealth
        self.health = self.maxHealth
        self.alive = True
        
        self.standing = False
        self.right = True
        self.left = False
        
        self.framecount = 0
        
        self.playerOne = pOne


    def draw(self, sprites):

        if self.standing:
            #put here the animation of the standing caracter
            pass
        else:
            if self.right:
                self.display.blit(sprites['WR'+str(self.framecount%4)], self.position)
                #put here the animation of right walking caracter
                pass
            elif self.left:
                #put here the animation of left walking caracter
                pass
                
        if self.playerOne:
		#put here the left health bar
            pass
        else:
		#put here the right health bar
            pass
                
        self.framecount += 1
	