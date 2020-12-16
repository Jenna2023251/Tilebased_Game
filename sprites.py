import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image = pygame.image.load("img/Chara_01.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.x = x
        self.y = y
        self.targetx = x
        self.targety = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE



    # this was meant for more fluid motion when moving the sprite
        #self.pos = vec(400, 300)
        #self.vel = vec(0, 0)
        #self.acc = vec(0, 0)

    #def update(self):
        #self.acc = vec(0, 0)
        #keystate = pygame.key.get_pressed()
        #if keystate[pygame.K_a]:
            #self.acc.x = -PLAYER_ACC
        #if keystate[pygame.K_d]:
            #self.acc.x = PLAYER_ACC

            #self.acc += self.vel * PLAYER_FRICTION

            #self.vel += self.acc
            #self.pos += self.vel + 0.5 * self.acc

            #if self.pos.x > 800:
                #self.pos.x = 0
            #if self.pos.x < 0:
                #self.pos.x = 800

            #self.rect.center = self.pos
