from random import randint

class Bot:
    def __init__(self,
                 snake,
                 food):
        self.snake = snake
    
    def act(self):
        rnd = randint(0,3)
        
        #right
        if rnd == 0:
            self.snake.speed = [1,0]
        #up
        elif rnd == 1:
            self.snake.speed = [0,-1]
        #left
        elif rnd == 2:
            self.snake.speed = [-1,0]
        #down
        elif rnd == 3:
            self.snake.speed = [0, 1]