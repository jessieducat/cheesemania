from map import *

grid = make_grid()
for i in range(4):
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

