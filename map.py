import pygame
from random import randint
from config import *

class room():
    def __init__(self, room_height, room_width):
        self.room_height = room_height
        self.room_width = room_width
        self.tiles = []

    def __add_tiles__(self, add_tiles):
        for y in range(self.room_height):
            self.tiles.append([])
            for x in range(self.room_width):
                self.tiles[y].append(add_tiles[y][x])

    def __get_centre__(self):
        self.centerx, self.centery = self.tiles[self.room_height // 2][self.room_width // 2].__get_centre__()
        return self.centerx, self.centery


class tile(pygame.Rect):
    def __init__(self, type, x, y):
        super().__init__(self)
        self.x = x
        self.y = y
        self.height = 16
        self.width = 16
        self.type = type

    def __draw__(self):
        # draw tile to screen
        if self.type == "W":
            tile_colour = colour_orange
        if self.type == "R":
            tile_colour = colour
        if self.type == "B":
            tile_colour = background_colour
        pygame.draw.rect(screen, tile_colour, self)

    def __get_centre__(self):
        return self.centerx, self.centery


def make_grid():
    # setup a grid for the whole screen
    grid = []
    for y in range(row_no):
        grid.append([])
        for x in range(column_no):
            grid[y].append(tile("B", x * tile_width, y * tile_height))
    return grid


def room_dims():
    # randomly set room location and dimensions
    r_h = randint(10, 30)
    r_w = randint(10, 30)
    r_x = randint(2, column_no - r_w)
    r_y = randint(2, row_no - r_h)
    return r_h, r_w, r_x, r_y


def generate_room(grid, rooms, column_no, row_no):
    room_tiles = []
    # creates a new room Rect at random co-ordinates and sizes
    r_h, r_w, r_x, r_y = room_dims()
    while not attempt_room(grid, r_h, r_w, r_x, r_y):
        r_h, r_w, r_x, r_y = room_dims()
    for y in range(r_y, r_y + r_h):
        room_tiles.append([])
        for x in range(r_x, r_x + r_w):
            grid[y][x].type = "R"
            room_tiles[y - r_y].append(grid[y][x])

    grid = wallify(grid, r_h, r_w, r_x, r_y)
    new_room = room(r_h, r_w)
    new_room.__add_tiles__(room_tiles)
    rooms.append(new_room)
    return grid


def attempt_room(grid, r_h, r_w, r_x, r_y):
    # check to see if a room is in that space already
    for y in range(r_y, r_y + r_h):
        for x in range(r_x, r_x + r_w):
            if grid[y][x].type == "R" or grid[y][x].type == "W":
                return False
    return True


def wallify(grid, r_h, r_w, r_x, r_y):
    # draw walls around the edge of the room
    for x in range(r_x - 1, r_x + r_w + 1):
        grid[r_y - 1][x].type = "W"
    for x in range(r_x - 1, r_x + r_w + 1):
        grid[r_y + r_h][x].type = "W"
    for y in range(r_y - 1, r_y + r_h + 1):
        grid[y][r_x - 1].type = "W"
    for y in range(r_y - 1, r_y + r_h + 1):
        grid[y][r_x + r_w].type = "W"
    return grid