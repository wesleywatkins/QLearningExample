import pygame
import os

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
SKYBLUE = (135, 206, 250)
YELLOW = (255, 218, 15)

WIDTH, HEIGHT = 800, 800
PW, PH = 80, 80
CW, CH = 60, 60

score = 0

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')


def load_police_image():
    return pygame.image.load(os.path.join(img_folder, 'Police.png'))
