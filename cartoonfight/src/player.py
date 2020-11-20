import pygame


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
    
        self.speed = 8
        self.yspeed = 0
        
        self.framecount = 0
        self.attack_count = 0
        self.walk_sprites = 9

        #Characther atributes
        self.max_health = max_health
        self.health = self.max_health
        self.base_damage = 10
        self.alive = True

        self.attack_hitbox = []
        self.attacked = False

    def draw(self, sprites):
        if self.basic_attack_left:
            self.display.blit(sprites['BAL'+str((self.attack_count//3)%4)], self.position)
            self.attack_count += 1

        elif self.basic_attack_right:
            self.display.blit(sprites['BAR'+str((self.attack_count//3)%4)], self.position)
            self.attack_count += 1

        elif self.standingRight:
            self.display.blit(sprites['WR0'], self.position)

        elif self.standingLeft:
            self.display.blit(sprites['WL0'], self.position)

        elif self.right:
            self.display.blit(sprites['WR'+str(1+(self.framecount//3)%self.walk_sprites)], self.position)
            self.framecount += 1

        elif self.left:
            self.display.blit(sprites['WL'+str(1+(self.framecount//3)%self.walk_sprites)], self.position)
            self.framecount += 1

        self.health_bar()

        if self.show_hitbox:
            pygame.draw.rect(self.display, (235, 64, 52), self.hitbox, 4)
            if self.attacked:
                pygame.draw.rect(self.display, (235, 64, 52), self.attack_hitbox, 4)

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
    def basic_attack(self, other_player):
        if self.right or self.standingRight:
            self.basic_attack_right = True
            self.basic_attack_left = False
        elif self.left or self.standingLeft:
            self.basic_attack_left = True
            self.basic_attack_right = False

        if self.attack_count > 9:
            self.basic_attack_left = False
            self.basic_attack_right = False
            self.attack_count = 0
        elif self.attack_count == 7:
            direction = 0
            if self.basic_attack_right:
                direction = 40
            else:
                direction = -40
            self.attacked = True
            self.attack_hitbox = (pygame.Rect(
                (self.position[0]+self.size[1]+direction, self.position[1] + self.size[3]/3),
                (40, 40),
            ))

            if self.attack_hitbox.colliderect(other_player.hitbox):
                other_player.health -= self.base_damage
                if other_player.health < 0:
                    other_player.health = 0
            
    def health_bar(self):
        player_health = self.health/self.max_health
        color = (0,0,0)
        if player_health > 0.7:
            color = (0,255*player_health,0)
        elif player_health > 0.2:
            color = (50+255*(1-player_health),255*player_health*1.3,0)
        else:
            color = (255*(1-player_health),0,0)
            
        if self.is_player_one:
            pygame.draw.rect(
                    self.display,(200,100,100),
                    (
                        self.window_size[0]*0.05-2,
                        self.window_size[1]*0.05-2,
                        self.window_size[0]*0.4+4,
                        self.window_size[1]*0.03+4
                    )
            )
            pygame.draw.rect(
                    self.display,(200,200,200), 
                    (
                        self.window_size[0]*0.05,
                        self.window_size[1]*0.05,
                        self.window_size[0]*0.4, 
                        self.window_size[1]*0.03
                    )
            )
            pygame.draw.rect(
                    self.display,color, 
                    (
                        self.window_size[0]*0.05,
                        self.window_size[1]*0.05,
                        self.window_size[0]*0.4*player_health, 
                        self.window_size[1]*0.03
                    )
            )
        else:
            pygame.draw.rect(
                    self.display,(200,100,100),
                    (
                        self.window_size[0]*0.55-2,
                        self.window_size[1]*0.05-2,
                        self.window_size[0]*0.4+4,
                        self.window_size[1]*0.03+4
                    )
            )
            pygame.draw.rect(
                    self.display,(200,200,200),
                    (
                        self.window_size[0]*0.55,
                        self.window_size[1]*0.05,
                        self.window_size[0]*0.4,
                        self.window_size[1]*0.03
                    )
            )
            pygame.draw.rect(
                    self.display,color,
                    (
                        self.window_size[0]*0.55+self.window_size[0]*0.4*(1-player_health),
                        self.window_size[1]*0.05,
                        self.window_size[0]*0.4*player_health,
                        self.window_size[1]*0.03
                    )
            )
