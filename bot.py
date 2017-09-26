from random import randint
from math import sqrt
import copy

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

class Bot:
    def __init__(self,
                 snake,
                 food):
        """ Creates an AI bot using q-learning
            variables:
            alpha: learning rate, high values consider recent event more
            gamma: discount factor, low value will yield a greedy snake whilst high values makes it consider long term rewards more
        """
        self.snake = snake
        self.episodes = 0
        self.food = food
        self.alpha = 0.1
        self.gamma = 0.5
    
    def update(self, episodes):
        self.episodes = episodes
    
    def act(self):
        
        self.is_close_to_body()
        
        action = self.move_to_food()

        #right
        if action == 0:
            return RIGHT
        #up
        elif action == 1:
            return UP
        #left
        elif action == 2:
            return LEFT
        #down
        elif action == 3:
            return DOWN

    def calc_manhattan_dist(self, head):
        """calculates the manhattan distance 
            from the snakes head to the current food position"""
        d_x = abs(self.food.position[0] - head[0])
        d_y = abs(self.food.position[1] - head[1])
        dist = d_x + d_y
        return dist

    def calc_euclid_dist(self, head):
        """calculates the euclidian distance 
            from the snakes head to the current food position"""
        d_x = abs(self.food.position[0] - head[0])
        d_y = abs(self.food.position[1] - head[1])
        dist = sqrt(pow(d_x,2) + pow(d_y, 2));
        return dist

    def calc_pos(self, dir):
        temp_head = copy.deepcopy(self.snake.body[0])
        #right
        if dir == 0:
            temp_head[0] = temp_head[0] + 1
        #up
        elif dir == 1:
            temp_head[1] = temp_head[1] - 1
        #left
        elif dir == 2:
            temp_head[0] = temp_head[0] - 1
        #down
        elif dir == 3:
            temp_head[1] = temp_head[1] + 1
        return temp_head

    def set_food(self, food):
        self.food = food
        
    def move_to_food(self):
        new_poses = [0.0]*4

        currDirr = self.snake.speed

        if currDirr == [1,0]: # Right
            #print("Curr dirr: RIGHT");
            skipIndex = LEFT
        elif currDirr == [0,1]: # Up
            skipIndex = UP
            #print("Curr dirr: down");
        elif currDirr == [-1, 0]: # Left
            skipIndex = RIGHT
            #print("Curr dirr: Left");
        elif currDirr == [0, -1]: # down
            skipIndex = DOWN
            #print("Curr dirr: up");


        for i in range(4):     
            nextHead = self.calc_pos(i)
            dist = self.calc_manhattan_dist(nextHead)
            #dist = self.calc_euclid_dist(nextHead)
            new_poses[i] = dist

            if i==skipIndex:
                new_poses[i] = float("inf")
        
        
        action = new_poses.index(min(new_poses))
        return action
        
    def is_close_to_body(self):
        proximity = [[0,0]]*5
        
        temp_head = copy.deepcopy(self.snake.body[0])
        
        proximity[0] = [temp_head[0] - 1, temp_head[1]]
        proximity[1
        
        
        
        
        