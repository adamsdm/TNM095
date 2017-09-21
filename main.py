import pygame
from random import randint
from bot import Bot
from food import Food
from Snake import Snake

RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3

pygame.init()
myfont = pygame.font.SysFont("monospace", 12)

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
# Size of one bodypart (i.e one gridpoint width/height)
BLOCK_SIZE = 20 
FPS = 5
FPSCLOCK = pygame.time.Clock()

# Dimension of grid
GRID_SIZE = [21, 21]
PADDING = BLOCK_SIZE/10

episodes = 0

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
    snake = Snake(gameDisplay, GRID_SIZE, BLOCK_SIZE)
    food = Food(gameDisplay, GRID_SIZE, BLOCK_SIZE)
    bot = Bot(snake, food)    


gameShouldClose = False

init()
while not gameShouldClose:
    
    botAction = bot.act()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameShouldClose = True
        ## Handle movement
        
        # if (event.type == pygame.KEYDOWN and (event.key == pygame.K_UP)):
        #     if snake.speed != [0, 1]:
        #         snake.speed = [0, -1]
        #         break
        # elif (event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN)):
        #     if snake.speed != [0, -1]:
        #         snake.speed = [0, 1]
        #         break
        # elif (event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT)):
        #     if snake.speed != [1, 0]:
        #         snake.speed = [-1, 0]
        #         break
        # elif (event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT)):
        #     if snake.speed != [-1, 0]:
        #         snake.speed = [1, 0]
        #         break
    if botAction == UP:
        if snake.speed != [0, 1]:
            snake.speed = [0, -1]
    elif botAction == DOWN:
        if snake.speed != [0, -1]:
            snake.speed = [0, 1]
    elif botAction == LEFT:
        if snake.speed != [1, 0]:
            snake.speed = [-1, 0]
    elif botAction == RIGHT:
        if snake.speed != [-1, 0]:
            snake.speed = [1, 0]
        

    gameDisplay.fill(BLACK)
    textsurface = myfont.render("Score: " + str(snake.score), False, (255, 255, 0))
    gameDisplay.blit(textsurface,(0,0))
    textsurfaceEpisodes = myfont.render("Episodes: " + str(episodes), False, (255,255,0))
    gameDisplay.blit(textsurfaceEpisodes, (5 * BLOCK_SIZE, 0))

    
    # Render shit
    snake.move()
    snake.draw()
    food.draw()

    if(snake.body[0] == food.position):
        snake.eat(True)
        food = Food(gameDisplay, GRID_SIZE, BLOCK_SIZE)
        bot.set_food(food)
    else:
        snake.eat(False)

    # Restart game if ded
    if(snake.checkCollision()):
        episodes += 1
        bot.update(episodes)
        init()
        
    FPSCLOCK.tick(FPS)
    pygame.display.update()
    



