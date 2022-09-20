import pygame
import math
from queue import PriorityQueue
from files.src import *
from files.colours import *

WINDOW = pygame.display.set_mode((750,750))
pygame.display.set_caption("A* PathFinder Beta")

def make_board(rows,width):
    board = []
    node_width = width // rows
    for i in range(rows):
        board.append([])
        for j in range(rows):
            node = Node(i,j,node_width,rows)
            board[i].append(node)
    return board

def create_grid_lines(window,rows,width):
     node_width = width // rows
     for i in range (rows):
         pygame.draw.line(window,grey,(0,i * node_width),(width,i * node_width))
         for j in range (rows):
            pygame.draw.line(window,grey,(j * node_width,0),(j * node_width,width))  

def draw(window,grid,rows,width):
    window.fill(white)

    for row in grid:
        for node in row:
            node.draw(window)
    create_grid_lines(window,rows,width)
    pygame.display.update()

def main(win, width):
	rows = 30
	grid = make_board(rows, width)

	start = None
	end = None

	run = True
	while run:
		draw(win, grid, rows, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
	pygame.quit()

main(WINDOW, 750)