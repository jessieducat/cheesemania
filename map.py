import pygame
from random import randint
from config import *

class room():
    def __init__(self, room_height, room_width, room_x, room_y):
        self.room_height = room_height
        self.room_width = room_width
        self.room_x = room_x
        self.room_y = room_y

        self.tiles = []

    def __add_tiles__(self, add_tiles):
        for y in range(self.room_height):
            self.tiles.append([])
            for x in range(self.room_width):
                self.tiles[y].append(add_tiles[y][x])

    def __get_centre__(self):
        self.centerx, self.centery = self.tiles[self.room_height // 2][self.room_width // 2].__get_centre__()
        return self.centerx, self.centery

    def __get_corners__(self):
        self.topleft = (self.room_x-1, self.room_y-1)
        self.topright = (self.room_x+self.room_width+1, self.room_y-1)
        self.bottomleft = (self.room_x-1, self.room_y+self.room_height+1)
        self.bottomright = (self.room_x+self.room_width+1, self.room_y+self.room_height+1)
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

        pygame.draw.rect(screen, tile_colour, self)
        image = pygame.transform.scale(image,(self.width,self.height))
        screen.blit(image,(self.x,self.y))



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
    r_h = randint(8, 20)
    r_w = randint(8, 20)
    r_x = randint(2, column_no - r_w-2)
    r_y = randint(2, row_no - r_h-2)
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
    new_room = room(r_h, r_w, r_x, r_y)
    new_room.__add_tiles__(room_tiles)
    rooms.append(new_room)
    drawdoors(grid, rooms)
    return grid , rooms

def collide(A,B, grid):
    Atopleft, Atopright,Abottomleft, Abottomright = A.__get_corners__()
    print(Atopleft[0], Atopright,Abottomleft, Abottomright)
    Btopleft, Btopright, Bbottomleft, Bbottomright = B.__get_corners__()
    print(Btopleft[1], Btopright, Bbottomleft, Bbottomright)

    if Btopright[0] == Atopleft[0]:
        if Atopleft[1]<Btopright[1]<Abottomleft[1]:
            touchingwalldistance = Abottomleft[1] - Btopright[1]
            midtouchingwall = (Btopright[0], Btopright[1]+(touchingwalldistance//2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1]][midtouchingwall[0]-1].type = "R"
            print("touching")
        if Atopleft[1]<Bbottomright[1]<Abottomleft[1]:
            touchingwalldistance = Bbottomright[1] - Atopleft[1]
            midtouchingwall = (Btopright[0], Atopright[1]+(touchingwalldistance//2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1]][midtouchingwall[0]-1].type = "R"
            print("touching")

    if Btopright[0] == Atopleft[0]+1 or Btopright[0]-1 == Atopleft[0]:
        if Atopleft[1]<Btopright[1]<Abottomleft[1]:
            touchingwalldistance = Abottomleft[1] - Btopright[1]
            midtouchingwall = (Btopright[0]-1, Btopright[1]+(touchingwalldistance//2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            print("touching")
        if Atopleft[1]<Bbottomright[1]<Abottomleft[1]:
            touchingwalldistance = Bbottomright[1] - Atopleft[1]
            midtouchingwall = (Btopright[0]-1, Atopright[1]+(touchingwalldistance//2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            print("touching")

    if Bbottomright[1] == Atopright[1]:
        if Atopleft[0] < Bbottomright[0] < Atopright[0]:
            touchingwalldistance = Bbottomright[0]- Atopleft[0]
            midtouchingwall = (Atopleft[0]+(touchingwalldistance//2), Atopright[1])
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1]-1][midtouchingwall[0]].type = "R"
            print("touching")
        if Atopleft[0] < Bbottomleft[0] < Atopright[0]:
            touchingwalldistance = Atopright[0] - Bbottomleft[0]
            midtouchingwall = (Bbottomleft[0]+(touchingwalldistance//2), Atopright[1])
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1]-1][midtouchingwall[0]].type = "R"
            print("touching")

    if Bbottomright[1] == Atopright[1]+1 or Bbottomright[1]+1 == Atopright[1]:
        if Atopleft[0] < Bbottomright[0] < Atopright[0]:
            touchingwalldistance = Bbottomright[0]- Atopleft[0]
            midtouchingwall = (Atopleft[0]+(touchingwalldistance//2), Atopright[1]-1)
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            print("touching")
        if Atopleft[0] < Bbottomleft[0] < Atopright[0]:
            touchingwalldistance = Atopright[0] - Bbottomleft[0]
            midtouchingwall = (Bbottomleft[0]+(touchingwalldistance//2), Atopright[1]-1)
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            print("touching")

    if Btopleft[0] == Atopright[0]:
        if Atopright[1]<Btopleft[1]<Abottomright[1]:
            touchingwalldistance = Abottomright[1] - Btopleft[1]
            midtouchingwall = (Btopleft[0], Btopleft[1]+(touchingwalldistance//2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1]][midtouchingwall[0]-1].type = "R"
            print("touching")
        if Atopright[1]<Bbottomleft[1]<Abottomright[1]:
            touchingwalldistance = Bbottomleft[1] - Atopright[1]
            midtouchingwall = (Btopleft[0], Atopleft[1]+(touchingwalldistance//2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1]][midtouchingwall[0]-1].type = "R"
            print("touching")

    if Btopleft[0] == Atopright[0]-1 or Btopleft[0]+1 == Atopright[0]:
        if Atopright[1]<Btopleft[1]<Abottomright[1]:
            touchingwalldistance = Abottomright[1] - Btopleft[1]
            midtouchingwall = (Btopleft[0]-1, Btopleft[1]+(touchingwalldistance//2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            print("touching")
        if Atopright[1]<Bbottomleft[1]<Abottomright[1]:
            touchingwalldistance = Bbottomleft[1] - Atopright[1]
            midtouchingwall = (Btopleft[0]-1, Atopleft[1]+(touchingwalldistance//2))
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            print("touching")

    if Btopright[1] == Abottomright[1]:
        if Abottomleft[0] < Btopright[0] < Abottomright[0]:
            touchingwalldistance = Btopright[0]- Abottomleft[0]
            midtouchingwall = (Abottomleft[0]+(touchingwalldistance//2), Abottomright[1])
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1]-1][midtouchingwall[0]].type = "R"
            print("touching")
        if Abottomleft[0] < Btopleft[0] < Abottomright[0]:
            touchingwalldistance = Abottomright[0] - Btopleft[0]
            midtouchingwall = (Btopleft[0]+(touchingwalldistance//2), Abottomright[1])
            grid[midtouchingwall[1]][midtouchingwall[0]].type = "R"
            grid[midtouchingwall[1]-1][midtouchingwall[0]].type = "R"
            print("touching")

def drawdoors(grid, rooms):
    for roomA in rooms:
        for roomB in rooms:
            if roomA != roomB:
                collide(roomA, roomB, grid)


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

def doors(grid, r_h, r_w, r_x, r_y):
    # creates door between touching rooms
    pass

def corridors(grid, r_h, r_w, r_x, r_y):
    # creates corridor to nearest room with rooms not touching anything
    pass

def hole(grid):
    # creates 2 holes in the left and right sides of the screen as start and end points
    for y in range(row_no):
        pass

