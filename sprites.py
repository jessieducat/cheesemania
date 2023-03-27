import pygame
import math
import random
import config


def handle_movement(keys_pressed):
    if keys_pressed[pygame.K_LEFT]:
        if config.player_loc[1] != 0 and config.grid[config.player_loc[0]][config.player_loc[1]-1].type != "W":
            current_tile = config.grid[config.player_loc[0]][config.player_loc[1]]
            config.player_loc[1] -= 1
            new_tile = config.grid[config.player_loc[0]][config.player_loc[1]]
            config.mouse_image = config.mouseleftsprite
            current_tile.type = "R"
            new_tile.type = "P"
    elif keys_pressed[pygame.K_RIGHT]:
        if config.player_loc[1] != int(config.screen.get_width()/20) and config.grid[config.player_loc[0]][config.player_loc[1]+1].type != "W":
            current_tile = config.grid[config.player_loc[0]][config.player_loc[1]]
            config.player_loc[1] += 1
            new_tile = config.grid[config.player_loc[0]][config.player_loc[1]]
            config.mouse_image = config.mouserightsprite
            current_tile.type = "R"
            new_tile.type = "P"
    elif keys_pressed[pygame.K_UP]:
        if config.player_loc[0] != 0 and config.grid[config.player_loc[0]-1][config.player_loc[1]].type != "W":
            current_tile = config.grid[config.player_loc[0]][config.player_loc[1]]
            config.player_loc[0] -= 1
            new_tile = config.grid[config.player_loc[0]][config.player_loc[1]]
            config.mouse_image = config.mouserightsprite
            current_tile.type = "R"
            new_tile.type = "P"
    elif keys_pressed[pygame.K_DOWN]:
        if config.player_loc[0] != int(config.screen.get_height()/20) and config.grid[config.player_loc[0] + 1][config.player_loc[1]].type != "W":
            current_tile = config.grid[config.player_loc[0]][config.player_loc[1]]
            config.player_loc[0] += 1
            new_tile = config.grid[config.player_loc[0]][config.player_loc[1]]
            config.mouse_image = config.mouserightsprite
            current_tile.type = "R"
            new_tile.type = "P"
    else:
        return


class Cat():
    def __init__(self, x_pos, y_pos, corners):
        self.x = x_pos
        self.y = y_pos
        speeds = [1.25, 2.5, 5]
        self.speed = speeds[random.randint(0, 2)]
        self.image = config.catsprite
        self.corners = corners

        # corners = topleft, topright, bottomleft, bottomright
        self.TopLeft = (20*(self.corners[0][0]+1), 20*(self.corners[0][1]+1))
        self.TopRight = (20*(self.corners[1][0]-1), 20*(self.corners[1][1]+1))
        self.BottomLeft = (20*(self.corners[2][0]+1), 20*(self.corners[2][1]-1))
        self.BottomRight = (20*(self.corners[3][0]-1), 20*(self.corners[3][1]-1))

    def display(self):
        config.screen.blit(self.image, (self.x, self.y))

    def movement(self):
        if self.x+40 < self.TopRight[0] and self.y == self.TopLeft[1]:
            self.x += self.speed
        elif self.x > self.BottomLeft[0] and self.y+40 == self.BottomLeft[1]:
            self.x -= self.speed
        elif self.y+40 < self.BottomRight[1] and self.x+40 == self.BottomRight[0]:
            self.y += self.speed
        elif self.y > self.TopLeft[1] and self.x == self.TopLeft[0]:
            self.y -= self.speed




