import pygame
from random import randint
from bot import Bot
from food import Food

pygame.init()
myfont = pygame.font.SysFont("monospace", 12)

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
# Size of one bodypart (i.e one gridpoint width/height)
BLOCK_SIZE = 20 
FPS = 10
FPSCLOCK = pygame.time.Clock()

# Dimension of grid
GRID_SIZE = [20, 20]
PADDING = BLOCK_SIZE/10


class Snake:
    # Constructor
    def __init__(self, window):
        self.body = [ [0,4], [0,3], [0,2], [0,1], [0,0] ]
        self.window = window
        self.speed = [0,1]
        self.score = 0

    def draw(self):
        for bodypart in self.body:
            pygame.draw.rect(self.window, WHITE, [bodypart[0]*BLOCK_SIZE + PADDING, bodypart[1]*BLOCK_SIZE + PADDING, BLOCK_SIZE-2*PADDING,BLOCK_SIZE-2*PADDING])
    def eat(self, didEat):
        if(not didEat):
            del self.body[-1] # Remove the last position if snake didn't eat
        else:
            self.score += 1

    def move(self):
        head = self.body[0]
        # Calculate next position the snake will be in
        nextPosX = head[0] + self.speed[0]
        nextPosY = head[1] + self.speed[1]
        nextPos = [nextPosX, nextPosY]
        self.body.insert(0, nextPos) # insert the new position
    
        
    
    def checkCollision(self):
        
        head = self.body[0]
        # Wall collision
        if(head[0] < 0 or head[0] > GRID_SIZE[0]):
            return True
        if(head[1] < 0 or head[1] > GRID_SIZE[1]):
            return True

        # self collision
        for bodypart in self.body[1:]:
            if head == bodypart:
               return True 

        # no collisions
        return False


gameDisplay = pygame.display.set_mode((GRID_SIZE[0]*BLOCK_SIZE,GRID_SIZE[1]*BLOCK_SIZE))
pygame.display.set_caption("Snakebot")
gameDisplay.fill(BLACK)
pygame.display.update()

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

def init():
    global snake
    global food
    global bot
    snake = Snake(gameDisplay)
    food = Food(gameDisplay)
    bot = Bot(snake, food)    







gameShouldClose = False

init()
while not gameShouldClose:
    print("start")
    bot.act()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameShouldClose = True
        
        # Handle movement
        
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP):
            if snake.speed != [0, 1]:
                snake.speed = [0, -1]
                break
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN):
            if snake.speed != [0, -1]:
                snake.speed = [0, 1]
                break
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT):
            if snake.speed != [1, 0]:
                snake.speed = [-1, 0]
                break
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT):
            if snake.speed != [-1, 0]:
                snake.speed = [1, 0]
                break
        

    gameDisplay.fill(BLACK)
    textsurface = myfont.render("Score: " + str(snake.score), False, (255, 255, 0))
    gameDisplay.blit(textsurface,(0,0))

    
    # Render shit
    snake.move()
    snake.draw()
    food.draw()

    if(snake.body[0] == food.position):
        snake.eat(True)
        food = Food(gameDisplay)
    else:
        snake.eat(False)

    # Restart game if ded
    if(snake.checkCollision()):
        init()
        
    FPSCLOCK.tick(FPS)
    pygame.display.update()
    



