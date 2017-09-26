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
BLOCK_SIZE = 14 
fps = 5
FPSCLOCK = pygame.time.Clock()

# Dimension of grid
GRID_SIZE = [71, 41]
PADDING = BLOCK_SIZE/10
UI_HEIGHT = 70;

episodes = 0

gameDisplay = pygame.display.set_mode((GRID_SIZE[0]*BLOCK_SIZE, GRID_SIZE[1]*BLOCK_SIZE + UI_HEIGHT) )
pygame.display.set_caption("Snakebot")
gameDisplay.fill(BLACK)
pygame.display.update()

pygame.font.init() # you have to call this at the start, 

highscore = 0;

def init():
    global snake1
    global food
    global bot1
    snake1 = Snake(gameDisplay, GRID_SIZE, BLOCK_SIZE)
    food = Food(gameDisplay, GRID_SIZE, BLOCK_SIZE)
    bot1 = Bot(snake1, food)    


gameShouldClose = False

init()
while not gameShouldClose:
    
    botAction = bot1.act()
    if botAction == UP:
        print("UP");
        if snake1.speed != [0, 1]:
            snake1.speed = [0, -1]
    elif botAction == DOWN:
        print("DOWN");
        if snake1.speed != [0, -1]:
            snake1.speed = [0, 1]
    elif botAction == LEFT:
        print("LEFT");
        if snake1.speed != [1, 0]:
            snake1.speed = [-1, 0]
    elif botAction == RIGHT:
        print("RIGHT");
        if snake1.speed != [-1, 0]:
            snake1.speed = [1, 0]
            
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
        

    gameDisplay.fill(BLACK)

    # Render shit
    snake1.move()
    snake1.draw()
    food.draw()

    # Update highscore
    if snake1.score > highscore:
        highscore = snake1.score

    # Draw UI
    pygame.draw.rect(gameDisplay, GRAY, [0 , GRID_SIZE[1]*BLOCK_SIZE, GRID_SIZE[0]*BLOCK_SIZE, UI_HEIGHT])
    
    textsurface = myfont.render("Score: " + str(snake1.score), False, (255, 255, 0))
    gameDisplay.blit(textsurface,(0,GRID_SIZE[1]*BLOCK_SIZE))
    textsurfaceHighscore = myfont.render("Highscore: " + str(highscore), False, (255, 255, 0))
    gameDisplay.blit(textsurfaceHighscore,(7 * BLOCK_SIZE,GRID_SIZE[1]*BLOCK_SIZE))
    textsurfaceEpisodes = myfont.render("Episodes: " + str(episodes), False, (255,255,0))
    gameDisplay.blit(textsurfaceEpisodes, (7 * BLOCK_SIZE, GRID_SIZE[1]*BLOCK_SIZE + BLOCK_SIZE))
    textsurfaceFPS = myfont.render("FPS: " + str(fps), False, (255,255,0))
    gameDisplay.blit(textsurfaceFPS, (0, GRID_SIZE[1]*BLOCK_SIZE + BLOCK_SIZE))

    if(snake1.body[0] == food.position):
        snake1.eat(True)
        food = Food(gameDisplay, GRID_SIZE, BLOCK_SIZE)
        bot1.set_food(food)
    else:
        snake1.eat(False)

    # Restart game if ded
    if(snake1.checkCollision()):
        episodes += 1
        bot1.update(episodes)
        init()
        
    FPSCLOCK.tick(fps)
    pygame.display.update()
    



