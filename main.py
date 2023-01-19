import pygame
import pygame.freetype
import pygame.mouse
from config import *
from button import *
from sprites import *
from text import *
from map import *

pygame.init()

def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        screen.fill(background_colour)
        mouse = pygame.mouse.get_pos()

        MENU_TEXT = titlefont.render("CHEESEMANIA", True, colour_orange)
        MENU_RECT = MENU_TEXT.get_rect(center=(width / 2 - 170, height / 2 - 220))

        play_button = button(colour, colour_light, (width / 2 - 35, height / 2 - 100), 140, 40, text='Play')

def play_screen():
    grid = make_grid()
    for i in range(5):
        grid = generate_room(grid, rooms, column_no, row_no)
        # grid = join_rooms(rooms)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        for row in grid:
            for tile in row:
                tile.__draw__()

        pygame.display.update()

def rules_screen():
    pygame.display.set_caption("Rules")

    while True:
        screen.fill(background_colour)
        screen.blit(ruleslist1_text, (width/2-350, height/2-240))
        screen.blit(ruleslist7_text, (width / 2 - 350, height / 2 - 210))
        screen.blit(ruleslist8_text, (width / 2 - 350, height / 2 - 180))
        screen.blit(ruleslist6_text,(width/2-350,height/2-120))
        screen.blit(ruleslist9_text, (width / 2 - 350, height / 2 - 90))
        screen.blit(ruleslist2_text, (width / 2 - 350, height / 2 -30))
        screen.blit(ruleslist10_text, (width / 2 - 350, height / 2 ))
        screen.blit(ruleslist11_text, (width / 2 - 350, height / 2 +30))
        screen.blit(ruleslist3_text, (width / 2 - 350, height / 2 +90))
        screen.blit(ruleslist4_text, (width / 2 - 350, height / 2+120))
        screen.blit(ruleslist12_text, (width / 2 - 350, height / 2 + 150))
        screen.blit(ruleslist5_text, (width / 2 - 350, height / 2+180 ))
        screen.blit(ruleslist13_text, (width / 2 - 350, height / 2 + 210))
        pygame.display.update()
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

def leaderboard_screen():
    pygame.display.set_caption("Leaderboard")

    while True:
        screen.fill(background_colour)
        screen.blit(lbtitletext, (width / 2 - 170, height / 2 - 220))
        pygame.display.update()
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                pygame.quit()

while True:
    screen.fill(background_colour)
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            #play button
            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 100 <= mouse[1] <= height / 2 - 60:
                play_screen()
            #quit button
            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()
            #rules button
            if width / 2 - 70 <=mouse[0] <= width/2+70 and height / 2 + 100 <= mouse[1] <= height / 2 + 140:
                rules_screen()
            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 +200 <= mouse[1] <= height / 2 +240:
                leaderboard_screen()
                # fills the screen with a colour

    # stores the (x,y) coordinates into
    # the variable as a tuple

    # if mouse is hovered on a button it
    # changes to lighter shade

    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, colour_light, [width / 2 - 70, height / 2, 140, 40])

    else:
        pygame.draw.rect(screen, colour_dark, [width / 2 - 70, height / 2, 140, 40])

    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 100 <= mouse[1] <= height / 2 - 100 + 40:
        pygame.draw.rect(screen, colour_light, [width / 2 - 70, height / 2 - 100, 140, 40])

    else:
        pygame.draw.rect(screen, colour_dark, [width / 2 - 70, height / 2 - 100, 140, 40])

    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 100 <= mouse[1] <= height / 2 + 100 + 40:
        pygame.draw.rect(screen, colour_light, [width / 2 - 70, (height / 2) + 100, 140, 40])

    else:
        pygame.draw.rect(screen, colour_dark, [width / 2 - 70, (height / 2) + 100, 140, 40])

    if width / 2 - 100 <= mouse[0] <= width / 2 + 100 and height / 2 + 200 <= mouse[1] <= height / 2 + 200 + 40:
        pygame.draw.rect(screen, colour_light, [width / 2 - 100, (height / 2) + 200, 200, 40])

    else:
        pygame.draw.rect(screen, colour_dark, [width / 2 - 100, (height / 2) + 200, 200, 40])

        # superimposing the text onto our button
    screen.blit(quittext, (width / 2 - 35, height / 2))
    screen.blit(playtext, (width / 2 - 35, height / 2 - 100))
    screen.blit(titletext, (width / 2 - 170, height / 2 - 220))
    screen.blit(rules_text, (width / 2 - 35, (height / 2) + 100))
    screen.blit(leaderboard_text, (width / 2 - 80, (height / 2) + 200,))

    # updates the frames of the game
    pygame.display.update()

self.screen.blit(titletext, (width / 2 - 170, height / 2 - 220))

pygame.display.set_caption("Cheesemania")

