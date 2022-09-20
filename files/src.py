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
    
    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.width))

    def __lt__(self, other):
        return False