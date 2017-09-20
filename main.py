import pygame
from random import randint
from food import Food
from Snake import Snake

pygame.init()
myfont = pygame.font.SysFont("monospace", 12)


WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
# Size of one bodypart (i.e one gridpoint width/height)
BLOCK_SIZE = 10 
FPS = 10
FPSCLOCK = pygame.time.Clock()

# Dimension of grid
GRID_SIZE = [40, 40]
PADDING = BLOCK_SIZE/10


gameDisplay = pygame.display.set_mode((GRID_SIZE[0]*BLOCK_SIZE,GRID_SIZE[1]*BLOCK_SIZE))
pygame.display.set_caption("Snakebot")
gameDisplay.fill(BLACK)
pygame.display.update()

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

snake = Snake(gameDisplay)
food = Food(gameDisplay)

gameShouldClose = False

while not gameShouldClose:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameShouldClose = True
        
        # Handle movement
        
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP):
            if snake.speed != [0, 1]:
                snake.speed = [0, -1]
                print("UP")
                break
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN):
            if snake.speed != [0, -1]:
                snake.speed = [0, 1]
                print("DOWN")
                break
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT):
            if snake.speed != [1, 0]:
                snake.speed = [-1, 0]
                print("LEFT")
                break
        elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT):
            print("RIGHT")
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
        snake = Snake(gameDisplay)
        
    FPSCLOCK.tick(FPS)
    pygame.display.update()
    



