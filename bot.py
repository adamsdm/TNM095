from random import randint

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
        rnd = randint(0,3)
        
        #right
        if rnd == 0:
            return RIGHT
        #up
        elif rnd == 1:
            return UP
        #left
        elif rnd == 2:
            return LEFT
        #down
        elif rnd == 3:
            return DOWN

    def calc_dist(self):
        """calculates the manhattan distance 
            from the snakes head to the current food position"""
        d_x = abs(self.food.position[0] - self.snake.body[0][0])
        d_y = abs(self.food.position[1] - self.snake.body[0][1])
        dist = d_x + d_y
        return dist

    def set_food(self, food):
        self.food = food