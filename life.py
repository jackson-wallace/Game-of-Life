import pygame
import numpy as np
import random

# The rules of Life are as follows:
#   1. Any living cell with two or three neighbors survives to the next generation
#   2. Any dead cell with three living neighbors becomes a living cell in the next generation
#   3. All other living cells die in the next generation. Similarly, all other dead cells stay dead

color_about_to_die = (83, 89, 154)
color_alive = (109, 157, 197)
color_background = (0, 0, 0)
color_grid = (0, 0, 0)

def update(surface, cur, sz):
    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    for r, c in np.ndindex(cur.shape):
        num_alive = np.sum(cur[r-1:r+2, c-1:c+2]) - cur[r, c]

        if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
            color = color_about_to_die
        elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
            nxt[r, c] = 1
            color = color_alive

        color = color if cur[r, c] == 1 else color_background
        pygame.draw.rect(surface, color, (c*sz, r*sz, sz-1, sz-1))

    return nxt

def init(dim_x, dim_y):
    cells = np.zeros((dim_y, dim_x))

    for i in range(len(cells)):
        for j in range(len(cells[i])):
            cells[i][j] = random.randint(0,1)

    return cells

def main(dim_x, dim_y, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((dim_x * cellsize, dim_y * cellsize))
    pygame.display.set_caption("Life")

    cells = init(dim_x, dim_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(color_grid)
        cells = update(surface, cells, cellsize)
        pygame.display.update()

if __name__ == "__main__":
    main(240, 120, 8)