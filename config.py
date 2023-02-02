import pygame
import os
import sys
pygame.init()

res = (1000, 760)
screen = pygame.display.set_mode(res)
width = screen.get_width()
height = screen.get_height()

colour = (255, 255, 204)
colour_light = (53, 133, 151)
colour_dark = (34, 85, 96)
colour_orange = (240, 128, 60)
background_colour = (239, 241, 106)
black = (0,0,0)


buttonfont = pygame.font.SysFont('Corbel', 35)
smallfont = pygame.font.SysFont("Corbel", 40)
titlefont = pygame.font.Font("Strong Brain.ttf", 45)

walltile = pygame.image.load("walltile.png")
floortile = pygame.image.load("floortile.jpg")
backtile = pygame.image.load("background.png")
cheesesprite = pygame.image.load("cheese-cheese-617686.png")
cheesesprite = pygame.transform.scale(cheesesprite, (20, 20))
catsprite = pygame.image.load("sneaky_cat-removebg.png")
catsprite = pygame.transform.scale(catsprite, (80, 80))
mousesprite = pygame.image.load("white-mouse-cliparts-219930.png")
mousesprite = pygame.transform.scale(mousesprite, (50,50))

tile_width = 20
tile_height = 20
column_no = width // tile_width
row_no = height // tile_height
clock = pygame.time.Clock()
rooms = []
