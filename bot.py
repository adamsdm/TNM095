class Bot:
    def __init__(self,
                 snake,
                 food):
        self.snake = snake
    
    def act(self):
        self.snake.speed = [1,0]

