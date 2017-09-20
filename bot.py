from random import randint

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

class Bot:
    def __init__(self,
                 snake,
                 food):
        self.snake = snake
        self.episodes = 0
    
    def update(episodes):
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