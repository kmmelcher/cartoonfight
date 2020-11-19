import pygame

import cartoonfight


class Player(object):

    def __init__(self, max_health, size, is_player_one, display):
        """
        :param max_health: (int) characther maximum health
        :param size: (int,int,int,int) xStart, xEnd, yStart, yEnd
        this coordinates are base on a 128x128 box.
        :param is_player_one: (bool) player one or player two
        :param display: (surface) game display
        return: (None)
        """
        self.name = ''
        self.display = display
        self.window_size = pygame.display.get_window_size()
        self.floor = self.window_size[1]-228
        self.size = size
                
        self.is_player_one = is_player_one

        if self.is_player_one:
            self.standingRight = True
            self.standingLeft = False
            self.position = [10,self.floor]
        else:
            self.standingLeft = True
            self.standingRight = False
            self.position = [self.window_size[0]-138,self.floor]

        self.hitbox = pygame.Rect(
            (self.position[0]+self.size[0], self.position[1]+self.size[2]),
            (self.size[1], self.size[3]),
        )
        self.show_hitbox = False

        #Player direction
        self.right = False
        self.left = False
        self.jumping = False

        self.basic_attack_left = False
        self.basic_attack_right = False
    
        self.speed = 12
        self.yspeed = 0
        
        self.framecount = 0
        self.walk_sprites = 9

        #Characther atributes
        self.max_health = max_health
        self.health = self.max_health
        self.alive = True

    def draw(self, sprites):

        if self.standingRight:
            self.display.blit(sprites['WR0'], self.position)

        elif self.standingLeft:
            self.display.blit(sprites['WL0'], self.position)

        elif self.right:
            self.display.blit(sprites['WR'+str(1+self.framecount%self.walk_sprites)], self.position)
            self.framecount += 1

        elif self.left:
            self.display.blit(sprites['WL'+str(1+self.framecount%self.walk_sprites)], self.position)
            self.framecount += 1

        elif self.base_atk_left:
            self.display.blit(sprites['KL'+str(self.framecount%4)], self.position)
            self.framecount += 1

        elif self.base_atk_right:
            self.display.blit(sprites['KR'+str(self.framecount%4)], self.position)
            self.framecount += 1
                
        if self.is_player_one:
            player_health = self.health/self.max_health
            color = (0,0,0)
            if player_health > 0.7:
                color = (0,255*player_health,0)
            elif player_health > 0.2:
                color = (50+255*(1-player_health),255*player_health*1.3,0)
            else:
                color = (255*(1-player_health),0,0)
                
            pygame.draw.rect(self.display,(200,100,100),(self.window_size[0]*0.05-2,self.window_size[1]*0.05-2,self.window_size[0]*0.4+4,self.window_size[1]*0.03+4))
            pygame.draw.rect(self.display,(200,200,200), (self.window_size[0]*0.05,self.window_size[1]*0.05,self.window_size[0]*0.4, self.window_size[1]*0.03))
            pygame.draw.rect(self.display,color, (self.window_size[0]*0.05,self.window_size[1]*0.05,self.window_size[0]*0.4*player_health, self.window_size[1]*0.03))
        else:
            player_health = self.health/self.max_health
            color = (0,0,0)
            if player_health > 0.7:
                color = (0,255*player_health,0)
            elif player_health > 0.2:
                color = (50+255*(1-player_health),255*player_health*1.3,0)
            else:
                color = (255*(1-player_health),0,0)

            pygame.draw.rect(self.display,(200,100,100),(self.window_size[0]*0.55-2,self.window_size[1]*0.05-2,self.window_size[0]*0.4+4,self.window_size[1]*0.03+4))
            pygame.draw.rect(self.display,(200,200,200),(self.window_size[0]*0.55,self.window_size[1]*0.05,self.window_size[0]*0.4,self.window_size[1]*0.03))
            pygame.draw.rect(self.display,color,(self.window_size[0]*0.55+self.window_size[0]*0.4*(1-player_health),self.window_size[1]*0.05,self.window_size[0]*0.4,self.window_size[1]*0.03))

        if self.show_hitbox:
            pygame.draw.rect(self.display, (235, 64, 52), self.hitbox, 4)

    #Player actions
    def move_right(self):
        if self.hitbox[0] < self.window_size[0] - self.size[0] -self.speed:
            self.position[0] += self.speed
            self.right = True
            self.left = False
            self.standingRight = False
            self.standingLeft = False
            self.hitbox = pygame.Rect(
                (self.position[0]+self.size[0], self.position[1]+self.size[2]),
                (self.size[1], self.size[3]),
            )
        else:
            self.stand()

    def move_left(self):
        if self.hitbox[0] > self.speed:
            self.position[0] -= self.speed
            self.right = False
            self.left = True
            self.standingRight = False
            self.standingLeft = False
            self.hitbox = pygame.Rect(
                (self.position[0]+self.size[0], self.position[1]+self.size[2]),
                (self.size[1], self.size[3]),
            )
        else:
            self.stand()

    def stand(self):
        if self.right:
            self.standingRight = True
            self.right = False
        elif self.left:
            self.standingLeft = True
            self.left = False

    def jump(self):
        gravity = 20
        if self.jumping:
            if self.position[1] <= self.floor:
                self.position[1] -= self.yspeed
                if self.position[1] > self.floor:
                    self.position[1] = self.floor + 1
                self.yspeed -= gravity
            else:
                self.position[1] = self.floor
                self.yspeed = 0
                self.jumping = False
        else:
            self.jumping = True
            self.yspeed = 100
        self.hitbox = pygame.Rect(
            (self.position[0]+self.size[0], self.position[1]+self.size[2]),
            (self.size[1], self.size[3]),
        )
