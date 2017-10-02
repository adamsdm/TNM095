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
GRAY = (50,50,50)
BLACK = (0,0,0)
GREEN = (0,255,0)
# Size of one bodypart (i.e one gridpoint width/height)
BLOCK_SIZE = 14 
fps = 15
FPSCLOCK = pygame.time.Clock()
NUM_SNAKES = 10
NUM_FOOD = 10

# Dimension of grid
GRID_SIZE = [71, 41]
PADDING = BLOCK_SIZE/10
UI_WIDTH = 200

episodes = 0

gameDisplay = pygame.display.set_mode((GRID_SIZE[0]*BLOCK_SIZE  + UI_WIDTH, GRID_SIZE[1]*BLOCK_SIZE) )
pygame.display.set_caption("Snakebot")
gameDisplay.fill(BLACK)
pygame.display.update()

pygame.font.init() # you have to call this at the start, 

highscore = 0;

def init():
    global snakes
    global deadSnakes
    global foods
    global bot1

    foods = []
    snakes = []
    deadSnakes = []
    
    for i in range(NUM_FOOD):
        foods.append(Food(gameDisplay, GRID_SIZE, BLOCK_SIZE))

    # Instanciate initial snake positions before creating snakes to ensure that snakes don't spawn on top of eachoter
    
    positions = []
    for i in range(NUM_SNAKES):
        pos = [randint(0, GRID_SIZE[0]), randint(0, GRID_SIZE[1])]
        # Create a new random pos untill we find one that's not already used
        while pos in positions:
            pos = [randint(0, GRID_SIZE[0]), randint(0, GRID_SIZE[1])]
        positions.append(pos)
        

    for i in range(NUM_SNAKES):
        pos = [randint(0, GRID_SIZE[0]), randint(0, GRID_SIZE[1])]
        snakes.append( Snake(   gameDisplay, 
                                pos, 
                                GRID_SIZE, 
                                BLOCK_SIZE, 
                                foods
                            )
                     )


gameShouldClose = False

init()
while not gameShouldClose:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameShouldClose = True
        
        if (event.type == pygame.KEYDOWN and (event.key == pygame.K_PLUS)):
            fps = max(1, fps + 5)
        elif (event.type == pygame.KEYDOWN and (event.key == pygame.K_MINUS)):
            fps = max(1, fps - 5)

    gameDisplay.fill(BLACK)

    # Copy of snake to remove dead snakes
    for snake in list(snakes):
        # Check collision with walls or self
        
        if( snake.checkCollision() ):
            deadSnakes.append(snake) 
            snakes.remove(snake)
            #snake.isAlive = False
            # Restart game if ded
            if(len(snakes) == 0):
                episodes += 1
                init()

    # For each snake
    for snake in snakes:
        snake.act()
        snake.move()
        snake.draw()


        for otherSnake in list(snakes):
            if ( otherSnake != snake and snake.checkCollideWithSnake(otherSnake) ):
                deadSnakes.append(snake)
                snakes.remove(snake)
            


    for food in foods:
        if not food.isEaten:
            food.draw()
    
    for food in list(foods):
        if food.isEaten:
            foods.remove(food)

    # Remove eaten food

    # Update highscore
    if snakes[0].score > highscore:
        highscore = snakes[0].score

    # Draw UI
    pygame.draw.rect(gameDisplay, GRAY, [GRID_SIZE[0]*BLOCK_SIZE , 0, UI_WIDTH, GRID_SIZE[1]*BLOCK_SIZE])

    # Print all alive snakes    
    textsurface = myfont.render("--ALIVE SNAKES--", False, (0,255,0))
    gameDisplay.blit(textsurface,(GRID_SIZE[0]*BLOCK_SIZE + PADDING, 0))
    for i in range(len(snakes)):
        textsurface = myfont.render("Score: " + str(snakes[i].score), False, snakes[i].COLOR)
        gameDisplay.blit(textsurface,(GRID_SIZE[0]*BLOCK_SIZE + PADDING, 20 + i*18))
    
    # Print all dead snakes
    textsurfaceDead = myfont.render("---DEAD SNAKES---" , False, (255,0,0))
    gameDisplay.blit(textsurfaceDead,(GRID_SIZE[0]*BLOCK_SIZE + PADDING, GRID_SIZE[1]*BLOCK_SIZE/2 - 20))
    for i in range(len(deadSnakes)):
        textsurfaceDead = myfont.render("Score: " + str(deadSnakes[i].score), False, deadSnakes[i].COLOR)
        gameDisplay.blit(textsurfaceDead,(GRID_SIZE[0]*BLOCK_SIZE + PADDING, GRID_SIZE[1]*BLOCK_SIZE/2 + i*18))

        
    FPSCLOCK.tick(fps)
    pygame.display.update()
    



