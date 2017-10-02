import pygame, os
import math
from random import randint
from bot import Bot
from food import Food
from math import sqrt

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

        # Find closest food
        self.closest_food = self.findClosestFood()
        self.bot = Bot(self, self.closest_food)    

    def findClosestFood(self):
        min_distance = float("inf")
        closest_food = self.foods[0]

        for i in range(len(self.foods)):
            food = self.foods[i]
            if(food.isEaten):
                continue
            head = self.body[0]
            d_x = abs(food.position[0] - head[0])
            d_y = abs(food.position[1] - head[1])
            dist = sqrt(pow(d_x,2) + pow(d_y, 2))


            if dist < min_distance :
                min_distance = dist
                closest_food = food

        return closest_food

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

        self.closest_food = self.findClosestFood()
        self.bot.set_food(self.closest_food)

        # Check if head on food 
        for food in list(self.foods):
            if head == food.position:
                self.eat()
                self.foods.remove(food)
                self.foods.append( Food(self.window, self.GRID_SIZE, self.BLOCK_SIZE) )

                self.closest_food = self.findClosestFood()
                self.bot.set_food(self.closest_food)
                
    
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

    def checkCollideWithSnake(self, otherSnake):
        head = self.body[0]
        if (head) in otherSnake.body:
            return True
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
    