import pygame, sys
from pygame.locals import *

import gameObject


class Game:
    def __init__(self, caption, width, height, frame_rate):
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        self.width = width
        self.height = height
        self.ground = None
        self.groundRect = None

        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.ground = pygame.Surface(size=(self.width, self.height / 6))
        self.ground.fill((0, 200, 0))
        self.groundRect = self.ground.get_rect()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    sys.exit()

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        self.screen.fill(color=(0, 191, 235))
        self.screen.blit(self.ground, (0, (self.height - (self.height / 6))))

        for o in self.objects:
            o.draw(self.screen)

    def run(self):
        while not self.game_over:
            self.handleEvents()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

game = Game("Physics Simulator", 1280, 800, 60)
game.run()