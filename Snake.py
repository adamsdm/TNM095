import pygame

GRID_SIZE = [40, 40]
BLOCK_SIZE = 10 
PADDING = BLOCK_SIZE/10

WHITE = (255,255,255)

class Snake:
    # Constructor
    def __init__(self, window):
        self.body = [ [0,4], [0,3], [0,2], [0,1], [0,0] ]
        self.window = window
        self.speed = [0,1]
        self.score = 0

    def draw(self):
        for bodypart in self.body:
            pygame.draw.rect(self.window, WHITE, [bodypart[0]*BLOCK_SIZE + PADDING, bodypart[1]*BLOCK_SIZE + PADDING, BLOCK_SIZE-2*PADDING,BLOCK_SIZE-2*PADDING])
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
        if(head[0] < 0 or head[0] > GRID_SIZE[0]):
            return True
        if(head[1] < 0 or head[1] > GRID_SIZE[1]):
            return True

        # self collision
        for bodypart in self.body[1:]:
            if head == bodypart:
               return True 

        # no collisions
        return False