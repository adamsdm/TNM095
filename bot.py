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
        dist = self.calc_dist(self.snake.body[0])
        new_poses = []

        for i in range(0,4):
            head = self.calc_pos(i)
            dist = self.calc_dist(head)
            new_poses.append(dist)

        action = new_poses.index(min(new_poses))
        #print ("action = " + str(action))

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

    def calc_dist(self, head):
        """calculates the manhattan distance 
            from the snakes head to the current food position"""
        d_x = abs(self.food.position[0] - head[0])
        d_y = abs(self.food.position[1] - head[1])
        dist = d_x + d_y
        return dist

    def calc_pos(self, dir):
        temp_head = self.snake.body[0]
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