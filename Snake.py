import pygame, os
import math
from random import randint
from bot import Bot
from food import Food


RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

class Snake:
    # Constructor
        
    def __init__(self, window, startPos, GRID_SIZE, BLOCK_SIZE, foods):
        self.body = [ [ startPos[0],startPos[1] ], 
                      [startPos[0],startPos[1]], 
                      [startPos[0],startPos[1]],
                      [startPos[0],startPos[1]],
                      [startPos[0],startPos[1]]
                    ]
        self.window = window
        self.speed = [0,1]
        self.score = 0
        self.GRID_SIZE = GRID_SIZE
        self.BLOCK_SIZE = BLOCK_SIZE
        self.PADDING = BLOCK_SIZE/10
        self.COLOR = (randint(100, 255),randint(100, 255),randint(100, 255))
        self.foods = foods
        
        self.bot = Bot(self, self.foods[0])    

    def draw(self):
        for bodypart in self.body:
            pygame.draw.rect(self.window, self.COLOR, [bodypart[0]*self.BLOCK_SIZE + self.PADDING, bodypart[1]*self.BLOCK_SIZE + self.PADDING, self.BLOCK_SIZE-2*self.PADDING,self.BLOCK_SIZE-2*self.PADDING])

    def eat(self):
        self.score += 1

    def move(self):
        head = self.body[0]

        # Calculate next position the snake will be in
        nextPosX = head[0] + self.speed[0]
        nextPosY = head[1] + self.speed[1]
        nextPos = [nextPosX, nextPosY]
        self.body.insert(0, nextPos) # insert the new position
        del self.body[-1] # Remove the last position

        self.bot.set_food(self.foods[0])

        if head == self.foods[0].position:
            del self.foods[0]
            self.foods.append( Food(self.window, self.GRID_SIZE, self.BLOCK_SIZE) )
            self.bot.set_food(self.foods[0])
            
    
        
    
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
    def act(self):
        botAction = self.bot.act()
        if botAction == UP:
            #print("UP");
            if self.speed != [0, 1]:
                self.speed = [0, -1]
        elif botAction == DOWN:
            #print("DOWN");
            if self.speed != [0, -1]:
                self.speed = [0, 1]
        elif botAction == LEFT:
            #print("LEFT");
            if self.speed != [1, 0]:
                self.speed = [-1, 0]
        elif botAction == RIGHT:
            #print("RIGHT");
            if self.speed != [-1, 0]:
                self.speed = [1, 0]
    