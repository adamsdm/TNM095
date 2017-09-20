import pygame
import math

class Snake:
    # Constructor
    def __init__(self, window, GRID_SIZE, BLOCK_SIZE):
        self.body = [ [math.floor(GRID_SIZE[0]/2),math.floor(GRID_SIZE[1]/2)], 
                      [math.floor(GRID_SIZE[0]/2),math.floor(GRID_SIZE[1]/2) - 1], 
                      [math.floor(GRID_SIZE[0]/2),math.floor(GRID_SIZE[1]/2) - 2], 
                      [math.floor(GRID_SIZE[0]/2),math.floor(GRID_SIZE[1]/2) - 3], 
                      [math.floor(GRID_SIZE[0]/2),math.floor(GRID_SIZE[1]/2) - 4] 
                    ]
        self.window = window
        self.speed = [0,1]
        self.score = 0
        self.GRID_SIZE = GRID_SIZE
        self.BLOCK_SIZE = BLOCK_SIZE
        self.PADDING = BLOCK_SIZE/10
        self.WHITE = (255,255,255)

    def draw(self):
        for bodypart in self.body:
            pygame.draw.rect(self.window, self.WHITE, [bodypart[0]*self.BLOCK_SIZE + self.PADDING, bodypart[1]*self.BLOCK_SIZE + self.PADDING, self.BLOCK_SIZE-2*self.PADDING,self.BLOCK_SIZE-2*self.PADDING])
    def eat(self, didEat):
        if(not didEat):
            del self.body[-1] # Remove the last position if snake didn't eat
        else:
            self.score += 1

    def move(self):
        head = self.body[0]

        print(head)
        # Calculate next position the snake will be in
        nextPosX = head[0] + self.speed[0]
        nextPosY = head[1] + self.speed[1]
        nextPos = [nextPosX, nextPosY]
        self.body.insert(0, nextPos) # insert the new position
    
        
    
    def checkCollision(self):
        
        head = self.body[0]
        # Wall collision
        if(head[0] < 0 or head[0] > self.GRID_SIZE[0] - 1):
            return True
        if(head[1] < 0 or head[1] > self.GRID_SIZE[1] - 1):
            return True

        # self collision
        for bodypart in self.body[1:]:
            if head == bodypart:
               return True 

        # no collisions
        return False