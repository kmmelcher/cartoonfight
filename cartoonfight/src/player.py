import pygame


class Player(object):

    def __init__(self, position, max_health, size, is_player_one, display):
        self.name = ''
        self.display = display
        self.position = position
        self.size = size

        self.max_health = max_health
        self.health = self.max_health
        self.alive = True
        
        self.is_player_one = is_player_one

        if self.is_player_one:
            self.standingRight = True
            self.standingLeft = False
        else:
            self.standingLeft = True
            self.standingRight = False

        self.right = False
        self.left = False
        self.jumping = False

        self.basic_attack_left = False
        self.basic_attack_right = False
    
        self.speed = 12
        self.yspeed = 0
        
        self.framecount = 0
        self.walk_sprites = 9

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
            window_size = pygame.display.get_window_size()
            player_health = self.health/self.max_health
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
            player_health = self.health/self.max_health
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

    #Player actions
    def move_right(self):
        self.position[0] += self.speed
        self.right = True
        self.left = False
        self.standingRight = False
        self.standingLeft = False

    def move_left(self):
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

    def jump(self, FLOOR):
        gravity = 20
        if self.jumping:
            if self.position[1] <= FLOOR:
                self.position[1] -= self.yspeed
                if self.position[1] > FLOOR:
                    self.position[1] = FLOOR + 1
                self.yspeed -= gravity
            else:
                self.position[1] = FLOOR
                self.yspeed = 0
                self.jumping = False
        else:
            self.jumping = True
            self.yspeed = 100
