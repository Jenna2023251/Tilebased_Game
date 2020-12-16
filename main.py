import pygame
import random
import os
from os import path
from settings import *
from sprites import *
from tilemap import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((800, 600))
        # Set the title bar
        pygame.display.set_caption(TITLE)
        # make the clock object
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(250, 100)
        self.running = True

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, "map2.txt"))

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.run
        self.load_data()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row)
                if tile == "P":
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                    if event.key == pygame.K_a:
                        self.player.move(dx=-1)
                    if event.key == pygame.K_d:
                        self.player.move(dx=1)
                    if event.key == pygame.K_w:
                        self.player.move(dy=-1)
                    if event.key == pygame.K_s:
                        self.player.move(dy=1)


    def draw_grid(self):
        for x in range (0, 800, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, 600))
        for y in range(0, 600, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (0, y), (800, y))

    def draw(self):
            self.screen.fill(BLACK)
            self.draw_grid()
            for sprite in self.all_sprites:
                self.screen.blit(sprite.image, self.camera.apply(sprite))
            pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

game = Game()
game.show_start_screen()
while game.running:
    game.new()
    game.run()
    game.show_go_screen()

pygame.quit()
