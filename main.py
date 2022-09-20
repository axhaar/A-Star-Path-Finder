import pygame
import math
from queue import PriorityQueue
from files.src import *
from files.colours import *

width = 750
WINDOW = pygame.display.set_mode((width,width))
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

def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col

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

			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, rows, width)
				location = grid[row][col]
				if not start and location != end:
					start = location
					start.create_start()

				elif not end and location != start:
					end = location
					end.create_destination()

				elif location != end and location != start:
					location.create_blocker()

	pygame.quit()

main(WINDOW, width)