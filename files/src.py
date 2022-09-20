import pygame
from files.colours import *

class Node:
    def __init__(self,row,col,width,t_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = white
        self.neighbours = []
        self.width = width
        self.total_rows = t_rows

    def find_position(self):
        return self.row,self.col

    def is_visited(self):
        return self.color == blue
    
    def is_blocked(self):
        return self.color == navy

    def is_start(self):
        return self.color == purple
    
    def is_destination(self):
        return self.color == orange

    def reset_board(self):
        self.color = white
    
    def create_blocker(self):
        self.color = navy

    def create_start(self):
        self.color = purple

    def create_visited(self):
        self.color = blue
    
    def create_destination(self):
        self.color = orange
    
    def create_path(self):
        self.color = yellow
    
    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.width))

    def __lt__(self, other):
        return False