import pygame.freetype
import pygame.mouse
import config
from sprites import handle_movement
from sprites import Cat
from text import *
from map import *

pygame.init()


def save_score(name, score):
    file = open("leaderboard", 'a')
    file.write(name + ": " + str(score))
    file.write('\n')


def main_menu():
    pygame.display.set_caption("Menu")

    name = "Click to edit"
    name_text = smallfont.render(name, True, colour)
    name_rect = name_text.get_rect(x=200, y=600)
    active = False
    invalid = False

    while True:
        screen.fill(background_colour)
        mouse = pygame.mouse.get_pos()

        MENU_RECT = MENU_TEXT.get_rect(center=(width / 2 - 170, height / 2 - 220))

        play_button = button(colour, colour_light, (width / 2 - 35, height / 2 - 100), 140, 40, text='Play')


class PlayScreen:
    def __init__(self):
        self.running = True

    def play_screen(self):
        grid = make_grid()
        pygame.display.set_caption("CHEESEMANIA")
        roomlist = []
        score = 0
        for i in range(num_rooms):
            grid, roomlist = generate_room(grid, rooms, column_no, row_no, i)
            # grid = join_rooms(rooms)

        first_room = rooms[0]
        first_room_tiles = first_room.tiles
        first_room_tiles[4][4].type = "P"
        first_room_first_tile = first_room_tiles[4][4]
        first_room_row = int(first_room_first_tile.y / 20)
        postition = grid[first_room_row].index(first_room_first_tile)
        config.player_loc.append(first_room_row)
        config.player_loc.append(postition)

        cats = []
        cheeses = []
        for room in roomlist:
            centrepoint = room.__get_centre__()
            new_cheese = cheesesprite.get_rect()
            new_cheese.x = centrepoint[0]
            new_cheese.y = centrepoint[1]
            cheeses.append(new_cheese)

            corners = room.__get_corners__()
            new_cat = Cat((corners[0][0] + 1) * 20, (corners[0][1] + 1) * 20, corners)
            cats.append(new_cat)

        first_loop = True
        if first_loop:
            start_time = pygame.time.get_ticks()
            first_loop = False



        while self.running:

            current_time = pygame.time.get_ticks()
            time_remaining = round(((config.gamelength - (current_time - start_time)) / 1000), 1)

            if current_time - start_time > config.gamelength:
                win = False
                save_score(name, score)
                end = EndGame(score, win)
                end.screen_loop(win)
                return win

            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            for row in grid:
                for tile in row:
                    tile.__draw__()

            current_mouse = config.grid[config.player_loc[0]][config.player_loc[1]]

            for i in range(num_rooms):
                cats[i].display()
                cats[i].movement()
                cat_rect = cats[i].image.get_rect(x=cats[i].x, y=cats[i].y)
                check_collision = cat_rect.colliderect(current_mouse)
                if check_collision:
                    win = False
                    save_score(name, score)
                    end = EndGame(score, win)
                    end.screen_loop(win)
                    return win

            for cheese in cheeses:
                screen.blit(cheesesprite, cheese)
                check_collision = cheese.colliderect(current_mouse)
                if check_collision:
                    cheeses.remove(cheese)
                    score = score + (time_remaining * 10)
                if len(cheeses) == 0:
                    score = score + (time_remaining * 20)
                    save_score(name, score)
                    win = True
                    end = EndGame(score, win)
                    end.screen_loop(win)
                    return win

            keys_pressed = pygame.key.get_pressed()
            handle_movement(keys_pressed)

            drawdoors(grid, rooms)
            # screen.blit(player.image, (player.x, player.y))
            score_text = smallfont.render("score = " + str(score), True, colour_orange)
            screen.blit(score_text, (80, 10))
            time_text = smallfont.render("time remaining = " + str(time_remaining), True, colour_orange)
            screen.blit(time_text, (400, 10))
            pygame.display.update()


def rules_screen():
    pygame.display.set_caption("Rules")
    running = True
    back_rules_rect = back_text.get_rect(topleft=(30, 20))
    while running:
        screen.fill(background_colour)
        pygame.draw.rect(screen, colour_dark, back_rules_rect)
        screen.blit(back_text, (30, 20))
        screen.blit(RULES_TEXT, (width / 2 - 100, 80))
        screen.blit(ruleslist1_text, (width / 2 - 350, height / 2 - 240))
        screen.blit(ruleslist7_text, (width / 2 - 350, height / 2 - 210))
        screen.blit(ruleslist8_text, (width / 2 - 350, height / 2 - 180))
        screen.blit(ruleslist6_text, (width / 2 - 350, height / 2 - 120))
        screen.blit(ruleslist9_text, (width / 2 - 350, height / 2 - 90))
        screen.blit(ruleslist2_text, (width / 2 - 350, height / 2 - 30))
        screen.blit(ruleslist10_text, (width / 2 - 350, height / 2))
        screen.blit(ruleslist11_text, (width / 2 - 350, height / 2 + 30))
        screen.blit(ruleslist3_text, (width / 2 - 350, height / 2 + 90))
        screen.blit(ruleslist4_text, (width / 2 - 350, height / 2 + 120))
        screen.blit(ruleslist12_text, (width / 2 - 350, height / 2 + 150))
        screen.blit(ruleslist5_text, (width / 2 - 350, height / 2 + 180))
        screen.blit(ruleslist13_text, (width / 2 - 350, height / 2 + 210))
        pygame.display.update()

        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if back_rules_rect.collidepoint(ev.pos):
                    running = False
                    return False
            if ev.type == pygame.QUIT:
                pygame.quit()


def leaderboard_screen():
    pygame.display.set_caption("Leaderboard")
    file = open("leaderboard")
    file_text = file.read()
    file_list = file_text.splitlines()
    running = True
    back_lb_rect = back_text.get_rect(topleft=(30, 20))

    # create list of scores
    while running:
        screen.fill(background_colour)
        screen.blit(lbtitletext, (width / 2 - 170, height / 2 - 220))
        pygame.draw.rect(screen, colour_dark, back_lb_rect)
        screen.blit(back_text, (30, 20))
        scores = []
        for i in range(len(file_list)):
            scores.append(float(file_list[i].split(":")[1]))

        # create list of top 10 scores and display them in descending order
        sorted_scores = sorted(scores, reverse=True)
        indices = []
        for i in range(10):
            indices.append(scores.index(sorted_scores[i]))
        for i in range(len(indices)):
            screen.blit(smallfont.render((str(i + 1) + ". " + file_list[indices[i]]), True, colour_orange),
                        (150, 250 + (i * 45)))

        pygame.display.update()
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if back_lb_rect.collidepoint(ev.pos):
                    running = False
                    return False
            if ev.type == pygame.QUIT:
                pygame.quit()


name = "Click to edit"
name_text = smallfont.render(name, True, colour)
name_rect = name_text.get_rect(x=200, y=280)
active = False
invalid = False


class EndGame:
    def __init__(self, score, win):
        self.screen = pygame.display.set_mode(res)
        self.running = True
        self.score_text = smallfont.render(("score = "+ str(score)), True, colour_orange)
        self.lb_text_end = smallfont.render("leaderboard", True, colour_orange)
        self.button = self.lb_text_end.get_rect()
        self.button.x = width / 2 - 150
        self.button.y = height / 2 + 50
        self.win = win

    def screen_loop(self, win):
        while self.running:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.collidepoint(event.pos):
                        running = True
                        while running:
                            running = leaderboard_screen()
            self.screen.fill(background_colour)
            self.screen.blit(self.score_text, (width / 2 - 150, height / 2 ))
            if self.win:
                self.screen.blit(win_text, (width / 2 - 170, height / 2 - 120))
            else:
                self.screen.blit(game_over_text, (width / 2 - 170, height / 2 - 120))
            self.screen.blit(self.lb_text_end, (width / 2 - 150, (height / 2) + 50))
            pygame.display.update()


class Game:

    def game(self, active, name, name_text):
        while True:
            screen.fill(background_colour)
            mouse = pygame.mouse.get_pos()

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    pygame.quit()

                    # checks if a mouse is clicked
                if ev.type == pygame.MOUSEBUTTONDOWN:

                    if name_rect.collidepoint(ev.pos):
                        active = True
                        if name == "Click to edit":
                            name = ""
                        else:
                            active = False

                    # if the mouse is clicked on the button the game is terminated

                    # play button
                    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 100 <= mouse[1] <= height / 2 - 60:
                        new_play = PlayScreen()
                        while new_play.running:
                            new_play.play_screen()
                    # quit button
                    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 <= mouse[1] <= height / 2 + 40:
                        pygame.quit()
                    # rules button
                    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 100 <= mouse[1] <= height / 2 + 140:
                        running = True
                        while running:
                            running = rules_screen()
                    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 200 <= mouse[1] <= height / 2 + 240:
                        running = True
                        while running:
                            running = leaderboard_screen()
                        # fills the screen with a colour

                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += ev.unicode

                name_text = smallfont.render(name, True, colour)

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

            # name input
            if active:
                pygame.draw.rect(screen, colour_light, name_rect)
            else:
                pygame.draw.rect(screen, colour_dark, name_rect)
            screen.blit(name_text, (200, 280))

            # updates the frames of the game
            pygame.display.update()

        self.screen.blit(titletext, (width / 2 - 170, height / 2 - 220))

        pygame.display.set_caption("Cheesemania")


game = Game()
game.game(active, name, name_text)
