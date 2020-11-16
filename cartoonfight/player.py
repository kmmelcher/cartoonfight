import pygame


#definition of a player class
class Player(object):

    def __init__(self, position, maxHealth, size, isPlayerOne, display):
        self.name = ' '
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
            w = pygame.display.get_window_size()
            ph = self.health/self.maxHealth
            pygame.draw.rect(self.display,(200,100,100),(w[0]*0.05-2,w[1]*0.05-2,w[0]*0.4+4,w[1]*0.03+4))
            pygame.draw.rect(self.display,(200,200,200), (w[0]*0.05,w[1]*0.05,w[0]*0.4, w[1]*0.03))
            pygame.draw.rect(self.display,(255*(1-ph),255*ph,0), (w[0]*0.05,w[1]*0.05,w[0]*0.4*ph, w[1]*0.03))
        else:
            w = pygame.display.get_window_size()
            ph = self.health/self.maxHealth
            pygame.draw.rect(self.display,(200,100,100),(w[0]*0.55-2,w[1]*0.05-2,w[0]*0.4+4,w[1]*0.03+4))
            pygame.draw.rect(self.display,(200,200,200),(w[0]*0.55,w[1]*0.05,w[0]*0.4,w[1]*0.03))
            pygame.draw.rect(self.display,(255*(1-ph),255*ph,0),(w[0]*0.55+w[0]*0.4*(1-ph),w[1]*0.05,w[0]*0.4,w[1]*0.03))


                
        
	
