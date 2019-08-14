# Imports
# ------------------------------
import pygame
import sys
import globals
import os
import numpy as np
from player import Player
from ai import AI

pygame.init()
pygame.font.init()


# Class Declaration
# ---------------------------------

class Game:

    def __init__(self):
        # display setup
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("AI World")
        self.screen = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
        # game setup
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.playing = True
        # setup game board
        self.rows = 10
        self.cols = 10
        self.game_table = np.zeros((self.rows, self.cols))
        self.game_table[0, 0] = 1
        self.game_table[0, 5] = 2
        self.game_table[1, 0] = 2
        self.game_table[1, 1] = 2
        self.game_table[1, 4] = 2
        self.game_table[2, 1] = 2
        self.game_table[2, 2] = 2
        self.game_table[3, 5] = 2
        self.game_table[3, 6] = 2
        self.game_table[3, 7] = 2
        self.game_table[4, 5] = 2
        self.game_table[5, 4] = 2
        self.game_table[6, 4] = 2
        self.game_table[7, 4] = 2
        # setup player
        self.player = Player(0, 0)
        # setup ai
        self.wesley = AI(self.player, self.game_table, self.rows, self.cols)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                np.save(os.path.join(globals.game_folder, 'qtable'), self.wesley.Q)
                pygame.quit()
                sys.exit()

    def update(self):
        self.wesley.run()

    def render(self):
        self.screen.fill(globals.WHITE)  # white background
        # draw board
        size = globals.WIDTH/10
        for i in range(1, self.rows):
            pygame.draw.line(self.screen, globals.BLACK, (0, size * i), (globals.WIDTH, size * i), 2)
            pygame.draw.line(self.screen, globals.BLACK, (size * i, 0), (size * i, globals.HEIGHT), 2)
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if self.game_table[i, j] == 1:
                    pygame.draw.circle(self.screen, globals.BLUE, (int(size / 2 + size * j), int(size / 2 + size * i)),
                                       int(size / 3))
                if self.game_table[i, j] == 2:
                    pygame.draw.circle(self.screen, globals.RED, (int(size/2 + size * j), int(size/2 + size * i)), int(size/3))
        pygame.display.flip()

    def run(self):
        dt = self.clock.tick(10)
        self.process_events()
        self.update()
        self.render()


if __name__ == '__main__':
    game = Game()
    while True:
        game.run()
