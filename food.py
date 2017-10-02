from random import randint
import pygame

GRID_SIZE = [40, 40]
BLOCK_SIZE = 10 
PADDING = BLOCK_SIZE/10

GREEN = (0,255,0)

class Food:
    GREEN = (0, 255, 0)
    BLUE = (0,0,255)

    def __init__(self, window, GRID_SIZE, BLOCK_SIZE):
        self.position = [randint(0, GRID_SIZE[0]-1), randint(0, GRID_SIZE[1]-1)]
        self.window = window
        self.GRID_SIZE = GRID_SIZE 
        self.BLOCK_SIZE = BLOCK_SIZE
        self.color = GREEN
        self.PADDING = BLOCK_SIZE/10
        self.isEaten = False
    
    def setColor(self, color):
        self.color = color
    
    def draw(self):
        pygame.draw.rect(self.window, self.color, [self.position[0]*self.BLOCK_SIZE + self.PADDING, self.position[1]*self.BLOCK_SIZE + self.PADDING, self.BLOCK_SIZE-2*self.PADDING,self.BLOCK_SIZE-2*self.PADDING])
