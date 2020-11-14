import pygame


#definition of a player class
class Player(object):

    def __init__(self, position, maxHealth, size, isPlayerOne, display):
        self.display = display
        self.position = position
        self.size = size

        self.maxHealth = maxHealth
        self.health = self.maxHealth
        self.alive = True
        
        self.isPlayerOne = isPlayerOne

        if self.isPlayerOne:
            self.standingRight = True
            self.standingLeft = False
        else:
            self.standingLeft = True
            self.standingRight = False

        self.right = False
        self.left = False

        self.speed = 18
        
        self.framecount = 0
        
        


    def draw(self, sprites):

        if self.standingRight:
            self.display.blit(sprites['WR0'], self.position)

        elif self.standingLeft:
            self.display.blit(sprites['WL0'], self.position)

        elif self.right:
            self.display.blit(sprites['WR'+str(1+self.framecount%4)], self.position)
            self.framecount += 1

        elif self.left:
            self.display.blit(sprites['WL'+str(1+self.framecount%4)], self.position)
            self.framecount += 1
                
        if self.isPlayerOne:
		    #put here the left health bar
            pass
        else:

		    #put here the right health bar
            pass
                
        
	