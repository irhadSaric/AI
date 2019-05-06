import sys

import pygame
from Battleships.Field import *
from Battleships.Board import *
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

BLOCK_SIZE = 50


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

matrix = []
for i in range(10):
    temp = []
    for j in range(10):
        temp.append(Field(pygame.Rect(j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), i, j))
    matrix.append(temp)

clock = pygame.time.Clock()
is_running = True
moves_counter = 1


board = Board(matrix)

board.random_place_carrier()
board.random_place_battleship()
board.random_place_submarine()
board.random_place_cruiser()
board.random_place_destroyer()

# board.matrix[0][5].ship_placed = True
# board.matrix[0][6].ship_placed = True
# board.matrix[0][7].ship_placed = True
# board.matrix[0][8].ship_placed = True
#
# board.matrix[1][6].ship_placed = True
# board.matrix[2][6].ship_placed = True
# board.matrix[3][6].ship_placed = True
# board.matrix[4][6].ship_placed = True
#
# board.matrix[4][4].ship_placed = True
# board.matrix[4][5].ship_placed = True
# board.matrix[4][7].ship_placed = True
# board.matrix[4][8].ship_placed = True
# board.matrix[4][9].ship_placed = True
#
# board.matrix[3][9].ship_placed = True
# board.matrix[5][9].ship_placed = True
#
# board.matrix[7][1].ship_placed = True
# board.matrix[7][2].ship_placed = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    board.display(screen)
    is_running = board.compare(screen)
    pygame.display.update()
    pygame.time.wait(10)



    clock.tick(25)

pygame.quit()
