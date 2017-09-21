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
        self.food = food
    
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