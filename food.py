from random import randint
import pygame

GRID_SIZE = [40, 40]
BLOCK_SIZE = 10 
PADDING = BLOCK_SIZE/10

GREEN = (0,255,0)

class Food:
    def __init__(self, window):
        self.position = [randint(0, GRID_SIZE[0]-1), randint(0, GRID_SIZE[1]-1)]
        self.window = window
    
    def draw(self):
        pygame.draw.rect(self.window, GREEN, [self.position[0]*BLOCK_SIZE + PADDING, self.position[1]*BLOCK_SIZE + PADDING, BLOCK_SIZE-2*PADDING,BLOCK_SIZE-2*PADDING])
