import pygame
import random
from random import randint
from config import *

random.seed(10)

class room():
    def __init__(self, room_height, room_width, room_x, room_y, name):
        self.room_height = room_height
        self.room_width = room_width
        self.room_x = room_x
        self.room_y = room_y
        self.tiles = []
        self.name = name
        self.touchingrooms = set()

    def __add_tiles__(self, add_tiles):
        for y in range(self.room_height):
            self.tiles.append([])
            for x in range(self.room_width):
                self.tiles[y].append(add_tiles[y][x])

    def __get_centre__(self):
        self.centerx, self.centery = self.tiles[self.room_height // 2][self.room_width // 2].__get_centre__()
        return self.centerx, self.centery

    def __get_name__(self):
        return self.name

    def __add_touching_room__(self, name):
        self.touchingrooms.add(name)

    def __get_len_set__(self):
        return len(self.touchingrooms)

    def __get_corners__(self):
        self.topleftcorner = (self.room_x - 1, self.room_y - 1)
        self.toprightcorner = (self.room_x + self.room_width + 1, self.room_y - 1)
        self.bottomleftcorner = (self.room_x - 1, self.room_y + self.room_height + 1)
        self.bottomrightcorner = (self.room_x + self.room_width + 1, self.room_y + self.room_height + 1)
        return self.topleftcorner, self.toprightcorner, self.bottomleftcorner, self.bottomrightcorner

    def __get_tile_corners__(self):
        self.topleft = (self.room_x - 1, self.room_y - 1)
        self.topright = (self.room_x + self.room_width, self.room_y - 1)
        self.bottomleft = (self.room_x - 1, self.room_y + self.room_height)
        self.bottomright = (self.room_x + self.room_width, self.room_y + self.room_height)
        return self.topleft, self.topright, self.bottomleft, self.bottomright

class tile(pygame.Rect):
    def __init__(self, type, x, y):
        super().__init__(self)
        self.x = x
        self.y = y
        self.height = 20
        self.width = 20
        self.type = type

    def __draw__(self):
        # draw tile to screen
        if self.type == "W":
            tile_colour = colour_orange
            image = walltile
        if self.type == "R":
            tile_colour = colour
            image = floortile
        if self.type == "B":
            tile_colour = background_colour
            image = backtile
        if self.type == "P":
            tile_colour = colour
            image = mousesprite

        pygame.draw.rect(screen, tile_colour, self)
        image = pygame.transform.scale(image, (self.width, self.height))
        screen.blit(image, (self.x, self.y))

    def __get_centre__(self):
        return self.centerx, self.centery


def make_grid():
    # setup a grid for the whole screen
    for y in range(row_no):
        grid.append([])
        for x in range(column_no):
            grid[y].append(tile("B", x * tile_width, y * tile_height))
    return grid


def room_dims(i,column_no,row_no):
    # randomly set room location and dimensions
    roomA_w = rooms[i-1].room_width
    roomA_h = rooms[i-1].room_height
    roomA_x = rooms[i-1].room_x
    roomA_y = rooms[i - 1].room_y
    r_h = randint(MIN_ROOM_HEIGHT, MAX_ROOM_HEIGHT)
    r_w = randint(MIN_ROOM_WIDTH, MAX_ROOM_WIDTH )
    r_x = randint(max(4 , roomA_x-(MAX_ROOM_WIDTH-3)), min((roomA_x+roomA_w+1), column_no - r_w - 2) )
    r_y = randint(max(4,roomA_y -(MAX_ROOM_HEIGHT-3)), min((roomA_y+roomA_h+1), row_no - r_h - 2))
    return r_h, r_w, r_x, r_y


def generate_room(grid, rooms, column_no, row_no, i):
    room_tiles = []
    # creates a new room Rect at random co-ordinates and sizes
    if len(rooms)==0:
        r_h = randint(MIN_ROOM_HEIGHT, MAX_ROOM_HEIGHT)
        r_w = randint(MIN_ROOM_WIDTH, MAX_ROOM_WIDTH)
        r_x = randint(4, column_no - r_w - 2)
        r_y = randint(4, row_no - r_h - 2)
    else:
        r_h, r_w, r_x, r_y = room_dims(i, column_no, row_no)
    while not attempt_room(grid, r_h, r_w, r_x, r_y):
        r_h, r_w, r_x, r_y = room_dims(i,column_no, row_no)
    for y in range(r_y, r_y + r_h):
        room_tiles.append([])
        for x in range(r_x, r_x + r_w):
            grid[y][x].type = "R"
            room_tiles[y - r_y].append(grid[y][x])

    grid = wallify(grid, r_h, r_w, r_x, r_y)
    new_room = room(r_h, r_w, r_x, r_y, roomnames[i])
    new_room.__add_tiles__(room_tiles)
    rooms.append(new_room)
    return grid, rooms


def collide(A, B, grid):
    Atopleft, Atopright, Abottomleft, Abottomright = A.__get_tile_corners__()
    Btopleft, Btopright, Bbottomleft, Bbottomright = B.__get_tile_corners__()

    if Btopright[0] == Atopleft[0]:
        if Atopleft[1] < Btopright[1] < Abottomleft[1]:
            # WORKING
            touchingwalldistance = Abottomleft[1] - Btopright[1]
            midtouchingwall = (Btopright[0], Btopright[1] + (touchingwalldistance // 2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1]][midtouchingwall[0] -1].type = "R"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())
        elif Atopleft[1] < Bbottomright[1] < Abottomleft[1]:
            touchingwalldistance = Bbottomright[1] - Atopleft[1]
            midtouchingwall = (Btopright[0], Atopright[1] + (touchingwalldistance // 2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1]][midtouchingwall[0] + 1].type = "R"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())

    if Bbottomright[1] == Atopright[1]:
        if Atopleft[0] < Bbottomright[0] < Atopright[0]:
            touchingwalldistance = Bbottomright[0] - Atopleft[0]
            midtouchingwall = (Atopleft[0] + (touchingwalldistance // 2), Atopright[1])
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1] - 1][midtouchingwall[0]].type = "R"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())
        elif Atopleft[0] < Bbottomleft[0] < Atopright[0]:
            touchingwalldistance = Atopright[0] - Bbottomleft[0]
            midtouchingwall = (Bbottomleft[0] + (touchingwalldistance // 2), Atopright[1])
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1] - 1][midtouchingwall[0]].type = "R"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())

    if Btopleft[0] == Atopright[0]:
        if Atopright[1] < Btopleft[1] < Abottomright[1]:
            touchingwalldistance = Abottomright[1] - Btopleft[1]
            midtouchingwall = (Btopleft[0], Btopleft[1] + (touchingwalldistance // 2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1]][midtouchingwall[0] - 1].type = "R"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())
        elif Atopright[1] < Bbottomleft[1] < Abottomright[1]:
            touchingwalldistance = Bbottomleft[1] - Atopright[1]
            midtouchingwall = (Btopleft[0], Atopleft[1] + (touchingwalldistance // 2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1]][midtouchingwall[0] - 1].type = "R"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())

    if Btopright[1] == Abottomright[1]:
        if Abottomleft[0] < Btopright[0] < Abottomright[0]:
            touchingwalldistance = Btopright[0] - Abottomleft[0]
            midtouchingwall = (Abottomleft[0] + (touchingwalldistance // 2), Abottomright[1])
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1] - 1][midtouchingwall[0]].type = "R"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())
        elif Abottomleft[0] < Btopleft[0] < Abottomright[0]:
            touchingwalldistance = Abottomright[0] - Btopleft[0]
            midtouchingwall = (Btopleft[0] + (touchingwalldistance // 2), Abottomright[1])
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1] - 1][midtouchingwall[0]].type = "R"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())

    if Btopright[0] == Atopleft[0] + 1 or Btopright[0] - 1 == Atopleft[0]:
        if Atopleft[1] < Btopright[1] < Abottomleft[1]:
            # WORKING
            touchingwalldistance = Abottomleft[1] - Btopright[1]
            midtouchingwall = (Btopright[0] -1, Btopright[1] + (touchingwalldistance // 2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())
        elif Atopleft[1] < Bbottomright[1] < Abottomleft[1]:
            touchingwalldistance = Bbottomright[1] - Atopleft[1]
            midtouchingwall = (Btopright[0] - 1, Atopright[1] + (touchingwalldistance // 2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())
    if Bbottomright[1] == Atopright[1] - 1:
        if Atopleft[0] < Bbottomright[0] < Atopright[0]:
            touchingwalldistance = Bbottomright[0] - Atopleft[0]
            midtouchingwall = (Atopleft[0] + (touchingwalldistance // 2), Atopright[1]-1)
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "B"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())
        elif Atopleft[0] < Bbottomleft[0] < Atopright[0]:
            touchingwalldistance = Atopright[0] - Bbottomleft[0]
            midtouchingwall = (Bbottomleft[0] + (touchingwalldistance // 2), Atopright[1]-1)
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "B"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())

    if Btopleft[0] == Atopright[0] - 1 or Btopleft[0] + 1 == Atopright[0]:
        if Atopright[1] < Btopleft[1] < Abottomright[1]:
            touchingwalldistance = Abottomright[1] - Btopleft[1]
            midtouchingwall = (Btopleft[0], Btopleft[1] + (touchingwalldistance // 2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())
        elif Atopright[1] < Bbottomleft[1] < Abottomright[1]:
            # WORKING
            touchingwalldistance = Bbottomleft[1] - Atopright[1]
            midtouchingwall = (Btopleft[0], Atopleft[1] + (touchingwalldistance // 2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())

    if Btopright[1] == Abottomright[1] + 2:
        if Abottomleft[0] < Btopright[0] < Abottomright[0]:
            touchingwalldistance = Btopright[0] - Abottomleft[0]
            midtouchingwall = (Abottomleft[0] + (touchingwalldistance // 2), Abottomright[1] + 1)
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "B"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())
        elif Abottomleft[0] < Btopleft[0] < Abottomright[0]:
            touchingwalldistance = Abottomright[0] - Btopleft[0]
            midtouchingwall = (Btopleft[0] + (touchingwalldistance // 2), Abottomright[1]+1)
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "B"
            A.__add_touching_room__(B.__get_name__())
            B.__add_touching_room__(A.__get_name__())


def drawdoors(grid, rooms):
    for i in range(5):
        for j in range(i, 5):
            if rooms[i] != rooms[j]:
                collide(rooms[i], rooms[j], grid)


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



