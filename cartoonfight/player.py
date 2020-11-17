import pygame


#definition of a player class
class Player(object):

    def __init__(self, position, maxHealth, size, isPlayerOne, display):
        self.name = ''
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

        self.base_atk_left = False
        self.base_atk_right = False

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

        elif self.base_atk_left:
            self.display.blit(sprites['KL'+str(self.framecount%4)], self.position)
            self.framecount += 1

        elif self.base_atk_right:
            self.display.blit(sprites['KR'+str(self.framecount%4)], self.position)
            self.framecount += 1

                
        if self.isPlayerOne:
            window_size = pygame.display.get_window_size()
            player_health = self.health/self.maxHealth
            color = (0,0,0)
            if player_health > 0.7:
                color = (0,255*player_health,0)
            elif player_health > 0.2:
                color = (50+255*(1-player_health),255*player_health*1.3,0)
            else:
                color = (255*(1-player_health),0,0)
                
            pygame.draw.rect(self.display,(200,100,100),(window_size[0]*0.05-2,window_size[1]*0.05-2,window_size[0]*0.4+4,window_size[1]*0.03+4))
            pygame.draw.rect(self.display,(200,200,200), (window_size[0]*0.05,window_size[1]*0.05,window_size[0]*0.4, window_size[1]*0.03))
            pygame.draw.rect(self.display,color, (window_size[0]*0.05,window_size[1]*0.05,window_size[0]*0.4*player_health, window_size[1]*0.03))
        else:
            window_size = pygame.display.get_window_size()
            player_health = self.health/self.maxHealth
            color = (0,0,0)
            if player_health > 0.7:
                color = (0,255*player_health,0)
            elif player_health > 0.2:
                color = (50+255*(1-player_health),255*player_health*1.3,0)
            else:
                color = (255*(1-player_health),0,0)

            pygame.draw.rect(self.display,(200,100,100),(window_size[0]*0.55-2,window_size[1]*0.05-2,window_size[0]*0.4+4,window_size[1]*0.03+4))
            pygame.draw.rect(self.display,(200,200,200),(window_size[0]*0.55,window_size[1]*0.05,window_size[0]*0.4,window_size[1]*0.03))
            pygame.draw.rect(self.display,color,(window_size[0]*0.55+window_size[0]*0.4*(1-player_health),window_size[1]*0.05,window_size[0]*0.4,window_size[1]*0.03))

    #actions of the player
    def mov_right(self):
        self.position[0] += self.speed
        self.right = True
        self.left = False
        self.standingRight = False
        self.standingLeft = False
    def mov_left(self):
        self.position[0] -= self.speed
        self.right = False
        self.left = True
        self.standingRight = False
        self.standingLeft = False
    def stand(self):
        if self.right:
            self.standingRight = True
            self.right = False
        elif self.left:
            self.standingLeft = True
            self.left = False




