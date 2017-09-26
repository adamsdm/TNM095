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
myfont = pygame.font.SysFont("monospace", 20)

WHITE = (255,255,255)
GRAY = (100,100,100)
BLACK = (0,0,0)
GREEN = (0,255,0)
# Size of one bodypart (i.e one gridpoint width/height)
BLOCK_SIZE = 20 
fps = 5
FPSCLOCK = pygame.time.Clock()

# Dimension of grid
GRID_SIZE = [21, 21]
PADDING = BLOCK_SIZE/10
UI_HEIGHT = 70;

episodes = 0

gameDisplay = pygame.display.set_mode((GRID_SIZE[0]*BLOCK_SIZE, GRID_SIZE[1]*BLOCK_SIZE + UI_HEIGHT) )
pygame.display.set_caption("Snakebot")
gameDisplay.fill(BLACK)
pygame.display.update()

pygame.font.init() # you have to call this at the start, 


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
        
        if (event.type == pygame.KEYDOWN and (event.key == pygame.K_PLUS)):
            fps += 5;
        elif (event.type == pygame.KEYDOWN and (event.key == pygame.K_MINUS)):
            fps -= 5;

        
        # Handle movement
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
        print("UP");
        if snake.speed != [0, 1]:
            snake.speed = [0, -1]
    elif botAction == DOWN:
        print("DOWN");
        if snake.speed != [0, -1]:
            snake.speed = [0, 1]
    elif botAction == LEFT:
        print("LEFT");
        if snake.speed != [1, 0]:
            snake.speed = [-1, 0]
    elif botAction == RIGHT:
        print("RIGHT");
        if snake.speed != [-1, 0]:
            snake.speed = [1, 0]
        

    gameDisplay.fill(BLACK)

    # Render shit
    snake.move()
    snake.draw()
    food.draw()

    # Draw UI
    pygame.draw.rect(gameDisplay, GRAY, [0 , GRID_SIZE[1]*BLOCK_SIZE, GRID_SIZE[0]*BLOCK_SIZE, UI_HEIGHT])
    
    textsurface = myfont.render("Score: " + str(snake.score), False, (255, 255, 0))
    gameDisplay.blit(textsurface,(0,GRID_SIZE[1]*BLOCK_SIZE))
    textsurfaceEpisodes = myfont.render("Episodes: " + str(episodes), False, (255,255,0))
    gameDisplay.blit(textsurfaceEpisodes, (7 * BLOCK_SIZE, GRID_SIZE[1]*BLOCK_SIZE))
    textsurfaceFPS = myfont.render("FPS: " + str(fps), False, (255,255,0))
    gameDisplay.blit(textsurfaceFPS, (0, GRID_SIZE[1]*BLOCK_SIZE + BLOCK_SIZE))

    #TODO:  KIVY SLIDER
    # https://kivy.org/docs/api-kivy.uix.slider.html

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
        
    FPSCLOCK.tick(fps)
    pygame.display.update()
    



