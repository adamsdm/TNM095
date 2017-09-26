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
fps = 15
FPSCLOCK = pygame.time.Clock()
NUM_SNAKES = 4

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
    global snakes
    global foods
    global bot1
    foods = [Food(gameDisplay, GRID_SIZE, BLOCK_SIZE)]

    snakes = []

    for i in range(NUM_SNAKES):
        snakes.append(Snake(gameDisplay, [randint(0, GRID_SIZE[0]), randint(0, GRID_SIZE[1])], GRID_SIZE, BLOCK_SIZE, foods))


gameShouldClose = False

init()
while not gameShouldClose:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameShouldClose = True
        
        if (event.type == pygame.KEYDOWN and (event.key == pygame.K_PLUS)):
            fps += 5;
        elif (event.type == pygame.KEYDOWN and (event.key == pygame.K_MINUS)):
            fps -= 5;

    gameDisplay.fill(BLACK)

    # Render shit
    for i in range(len(snakes)):
        snakes[i].act()
        snakes[i].move()
        snakes[i].draw()
        if( snakes[i].checkCollision() ):
            del snakes[i]
            # Restart game if ded
            if(len(snakes) == 0):
                episodes += 1
                init()
        

    for food in foods:
        food.draw()

    # Update highscore
    if snakes[0].score > highscore:
        highscore = snakes[0].score

    # Draw UI
    pygame.draw.rect(gameDisplay, GRAY, [0 , GRID_SIZE[1]*BLOCK_SIZE, GRID_SIZE[0]*BLOCK_SIZE, UI_HEIGHT])
    
    textsurface = myfont.render("Score: " + str(snakes[0].score), False, (255, 255, 0))
    gameDisplay.blit(textsurface,(0,GRID_SIZE[1]*BLOCK_SIZE))
    textsurfaceHighscore = myfont.render("Highscore: " + str(highscore), False, (255, 255, 0))
    gameDisplay.blit(textsurfaceHighscore,(7 * BLOCK_SIZE,GRID_SIZE[1]*BLOCK_SIZE))
    textsurfaceEpisodes = myfont.render("Episodes: " + str(episodes), False, (255,255,0))
    gameDisplay.blit(textsurfaceEpisodes, (7 * BLOCK_SIZE, GRID_SIZE[1]*BLOCK_SIZE + BLOCK_SIZE))
    textsurfaceFPS = myfont.render("FPS: " + str(fps), False, (255,255,0))
    gameDisplay.blit(textsurfaceFPS, (0, GRID_SIZE[1]*BLOCK_SIZE + BLOCK_SIZE))

        
    FPSCLOCK.tick(fps)
    pygame.display.update()
    



