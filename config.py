import pygame
import sys
pygame.init()

res = (1000, 800)
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

walltile = "walltile.png"
floortile = "floortile.png"
cheesesprite = "cheese-cheese-617686.png"
catsprite = "sneaky_cat-removebg.png"
mousesprite = "white-mouse-cliparts-219930.png"

tile_width = 10
tile_height = 10
column_no = width // tile_width
row_no = height // tile_height
clock = pygame.time.Clock()
rooms = []
