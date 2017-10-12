import random
from math import sqrt
import copy
import numpy as np

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

Q = np.random.rand(64,5)
Q = np.multiply(Q, 100)

print(Q)



class Bot:
    def __init__(self,
                 snake,
                 food,
                 GRID_SIZE):
        """ Creates an AI bot using q-learning
            variables:
            alpha: learning rate, high values consider recent event more
            gamma: discount factor, low value will yield a greedy snake whilst high values makes it consider long term rewards more
        """
        self.snake = snake
        self.food = food
        self.alpha = 0.7
        self.gamma = 0.6
        self.GRID_SIZE = GRID_SIZE
        self.action = DOWN 
        self.reward = np.matrix('0 0 0 -200 100; 10 -100 10 -200 0;\
            10 10 10 -1000 0; 10 -1000 50 -1000 0; -1000 10 10 -200 0;\
            -1000 -1000 10 -200 0; -1000 10 10 -1000 0; -1000 -1000 50 -1000 0;\
            10 10 -1000 -200 0; 10 -1000 -1000 -200 0; 10 10 -1000 -1000 0;\
            10 -1000 -1000 -1000 0; -1000 50 -1000 -200 0; -1000 -1000 -1000 -200 0;\
            -1000 50 -1000 -1000 0; -1000 -1000 -1000 -1000 0;\
            0 -200 0 0 100; 10 -100 10 10 0;\
            10 -200 10 -1000 0; 10 -1000 50 -1000 0; -1000 -200 10 10 0;\
            -1000 -1000 10 10 0; -1000 -200 10 -1000 0; -1000 -1000 50 -1000 0;\
            10 -200 -1000 10 0; 10 -1000 -1000 10 0; 10 -200 -1000 -1000 0;\
            10 -1000 -1000 -1000 0; -1000 -200 -1000 50 0; -1000 -1000 -1000 50 0;\
            -1000 -200 -1000 -1000 0; -1000 -1000 -1000 -1000 0;\
            -200 0 0 0 100; -200 -100 10 10 0;\
            -200 10 10 -1000 0; 10 -1000 50 -1000 0; -1000 10 10 10 0;\
            -1000 -1000 10 10 0; -1000 10 10 -1000 0; -1000 -1000 50 -1000 0;\
            -200 10 -1000 10 0; -200 -1000 -1000 10 0; -200 10 -1000 -1000 0;\
            -200 -1000 -1000 -1000 0; -1000 50 -1000 50 0; -1000 -1000 -1000 50 0;\
            -1000 50 -1000 -1000 0; -1000 -1000 -1000 -1000 0;\
            0 0 -200 0 100; 10 -100 -200 10 0;\
            10 10 -200 -1000 0; -1000 -1000 -200 -1000 0; -1000 10 -200 10 0;\
            -1000 -1000 -200 10 0; -1000 10 -200 -1000 0; -1000 -1000 -200 -1000 0;\
            10 10 -1000 10 0; 10 -1000 -1000 10 0; 10 10 -1000 -1000 0;\
            10 -1000 -1000 -1000 0; -1000 50 -1000 50 0; -1000 -1000 -1000 50 0;\
            -1000 50 -1000 -1000 0; -1000 -1000 -1000 -1000 0') 
        self.features = [False]*8
        self.old_state = 0
        self.state = 0 #state can be 0 - 15
        self.episodes = 0

        #print("Q: ", Q)
        #print("alpha: ", self.alpha)
        print("\n\n")


        #print(str(self.reward))
    
    def set_episodes(self, _episodes):
        self.episodes = _episodes
    
    def set_feature_vec(self):
        temp_head = copy.deepcopy(self.snake.body[0])
        
        self.features[0] = self.is_blocked_up()
        self.features[1] = self.is_blocked_down()
        self.features[2] = self.is_blocked_right()
        self.features[3] = self.is_blocked_left()
        
        self.features[4] = False
        self.features[5] = False
        self.features[6] = False
        self.features[7] = False
        
        # dir = up
        if self.snake.speed == [0,-1]:
            self.features[4] = True
        # dir = down
        elif self.snake.speed == [0,1]:
            self.features[5] = True
        # dir = left
        elif self.snake.speed == [-1,0]:
            self.features[6] = True
        #dir = right
        elif self.snake.speed == [1,0]:
            self.features[7] = True
        
    
    def determine_state(self):
        up = self.features[0]
        down = self.features[1]
        right = self.features[2]
        left = self.features[3]
        speed_up = self.features[4]
        speed_down = self.features[5]
        speed_left = self.features[6]
        speed_right = self.features[7]
        

        state = 0
        state = up*1 + down*2 + right*4 + left*8 + 16*speed_down + 32*speed_left + 48*speed_right
        return state

    def update_Q(self, state, action, next_state):
        Qmax = Q[next_state, :].max()
        #print("qmax = " + str(Qmax))

        # Q-learning algorithm
        Q[state, action] = (1 - self.alpha) * Q.item(state, action) + self.alpha * (self.reward.item(state, action) + self.gamma * Qmax)
        
        

    def get_best_action(self):
        curr_row = Q[self.state, :]
        best_action = curr_row.argmax(axis = 0)
        # print(column)
        # indices = np.where(curr_row == curr_row.max())
        # index = randint(0,indices[0].size - 1)
        # #print(index)
        # column = indices[0][index]

        return best_action
    
    def act(self):
        
        #is_close = self.is_close_to_body()
        #is_closeBorder = self.is_close_to_border()
        
        #action = self.move_to_food()
        self.set_feature_vec()
        self.old_state = self.state
        self.state = self.determine_state()
        self.action = self.get_best_action()
        
        #print("best action = " + str(self.action))

        if self.action == 4:
            food_action = self.move_to_food()
            #right
            if food_action == 0:
                return RIGHT
            #up
            elif food_action == 1:
                return UP
            #left
            elif food_action == 2:
                return LEFT
            #down
            elif food_action == 3:
                return DOWN    

        #right
        if self.action == 0:
            return RIGHT
        #up
        elif self.action == 1:
            return UP
        #left
        elif self.action == 2:
            return LEFT
        #down
        elif self.action == 3:
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

        if currDirr == [1,0]: # Righti
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
     
    def is_blocked_up(self):
       if self.snake.speed == [0,1]:
           return False
       
       temp_head = copy.deepcopy(self.snake.body[0])
       temp_head = [temp_head[0], temp_head[1] - 1]
       # border condition
       if temp_head[1] < 0:
            return True 
       for body_part in self.snake.body:
           if temp_head == body_part:
               return True
       return False 
    
    def is_blocked_right(self):
       if self.snake.speed == [-1,0]:
           return False
        
       temp_head = copy.deepcopy(self.snake.body[0])
       temp_head = [temp_head[0] + 1, temp_head[1]]
       #border condition
       if temp_head[0] == self.GRID_SIZE[0] :
            return True
       for body_part in self.snake.body:
           if temp_head == body_part:
               return True
       return False 
    
    def is_blocked_left(self):
       if self.snake.speed == [1,0]:
           return False
        
       temp_head = copy.deepcopy(self.snake.body[0])
       temp_head = [temp_head[0] - 1, temp_head[1]]

       #border condition
       if temp_head[0] < 0:
            return True

       for body_part in self.snake.body:
           if temp_head == body_part:
               return True
       return False 
    
    def is_blocked_down(self):
       if self.snake.speed == [0,-1]:
           return False
       
       temp_head = copy.deepcopy(self.snake.body[0])
       temp_head = [temp_head[0], temp_head[1] + 1]
       #border condition
       if temp_head[1] == self.GRID_SIZE[1]:
            return True
       for body_part in self.snake.body:
           if temp_head == body_part:
               return True
       return False 
       
    
    def is_close_to_body(self):
        proximity = [[0,0]]*5
        
        temp_head = copy.deepcopy(self.snake.body[0])
        #needs smarter way
        if self.snake.speed == [0,-1]: #UP
            proximity[0] = [temp_head[0] - 1, temp_head[1]] #LEFT
            proximity[1] = [temp_head[0] + 1, temp_head[1]] #RIGHT
            proximity[2] = [temp_head[0], temp_head[1] - 1] #UP
            proximity[3] = [temp_head[0] - 1, temp_head[1] - 1] #UP-LEFT
            proximity[4] = [temp_head[0] + 1, temp_head[1] - 1] #RIGHT
        elif self.snake.speed == [0,1]: #DOWN
            proximity[0] = [temp_head[0] + 1, temp_head[1]] #LEFT
            proximity[1] = [temp_head[0] - 1, temp_head[1]] #RIGHT
            proximity[2] = [temp_head[0], temp_head[1] + 1] #UP
            proximity[3] = [temp_head[0] + 1, temp_head[1] + 1] #UP-LEFT
            proximity[4] = [temp_head[0] - 1, temp_head[1] + 1] #RIGHT
        elif self.snake.speed == [1,0]:#RIGHT
            proximity[0] = [temp_head[0] , temp_head[1] - 1] #LEFT
            proximity[1] = [temp_head[0] , temp_head[1] + 1] #RIGHT
            proximity[2] = [temp_head[0] + 1, temp_head[1]] #UP
            proximity[3] = [temp_head[0] + 1, temp_head[1] - 1] #UP-LEFT
            proximity[4] = [temp_head[0] + 1, temp_head[1] + 1] #RIGHT
        elif self.snake.speed == [-1,0]:
            proximity[0] = [temp_head[0], temp_head[1] + 1] #LEFT
            proximity[1] = [temp_head[0], temp_head[1] - 1] #RIGHT
            proximity[2] = [temp_head[0] - 1, temp_head[1]] #UP
            proximity[3] = [temp_head[0] - 1, temp_head[1] + 1] #UP-LEFT
            proximity[4] = [temp_head[0] - 1, temp_head[1] - 1] #RIGHT
        
        for pos in proximity:
            for body_part in self.snake.body:
                if pos == body_part:
                    return True
        return False        
        
    def is_close_to_border(self):
        temp_head = copy.deepcopy(self.snake.body[0])
        
        if temp_head[0] == self.GRID_SIZE[0] - 1:
            return True
        elif temp_head[0] == 0:
            return True
        elif temp_head[1] == 0:
            return True
        elif temp_head[1] == self.GRID_SIZE[1] - 1:
            return True
        return False
        
    #def move_from_self():
        
        
        
        
        
        