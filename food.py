from random import randint
import pygame

GRID_SIZE = [40, 40]
BLOCK_SIZE = 10 
PADDING = BLOCK_SIZE/10

GREEN = (0,255,0)

class Food:
    def __init__(self, window, GRID_SIZE, BLOCK_SIZE):
        self.position = [randint(0, GRID_SIZE[0]-1), randint(0, GRID_SIZE[1]-1)]
        self.window = window
        self.GRID_SIZE = GRID_SIZE 
        self.BLOCK_SIZE = BLOCK_SIZE
        self.GREEN = (0, 255, 0)
        self.PADDING = BLOCK_SIZE/10
    
    def draw(self):
        pygame.draw.rect(self.window, self.GREEN, [self.position[0]*self.BLOCK_SIZE + self.PADDING, self.position[1]*self.BLOCK_SIZE + self.PADDING, self.BLOCK_SIZE-2*self.PADDING,self.BLOCK_SIZE-2*self.PADDING])
