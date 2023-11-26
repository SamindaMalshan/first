import pygame,sys,random

pygame.init()

width = 1200
height = 700

screen = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

ballX = 5
ballY = 5
direction = 1
dirx = 1
playerSpeed = 0
opponentSpeed = 7

def ballAnimating():
    global ballX,ballY
    
    ball.x += ballX
    ball.y += ballY
    if ball.top <= 0 or ball.bottom >= height:
        ballY *= -1
    if ball.left <= 0 or ball.right >= width:
        ballRestart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ballX *= -1

def playerAnimating():
    player.y += playerSpeed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height

def opponentAi():
    if opponent.top < ball.y:
        opponent.top += opponentSpeed
    if opponent.bottom > ball.y:
        #print('fdsf')
        opponent.bottom -= opponentSpeed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= height:
        opponent.bottom = height

def ballRestart():
    global ballX,ballY
    ball.center = (width/2,height/2)
    ballX *= random.choice((1,-1))
    ballY *= random.choice((1,-1))

grey = (200,200,200)
#making objects
player = pygame.Rect(width-20,height/2-50,20,100)
opponent = pygame.Rect(1,height/2-50,20,100)
ball = pygame.Rect(width/2-10,height/2-10,20,20)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerSpeed -= 7
            if event.key == pygame.K_DOWN:
                playerSpeed += 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                playerSpeed += 7
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7
                
    ballAnimating()
    playerAnimating()
    opponentAi()
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(grey),player)
    pygame.draw.rect(screen,(grey),opponent)
    pygame.draw.ellipse(screen,(grey),ball)
    pygame.draw.line(screen,(grey),(width/2,0),(width/2,height))

    pygame.display.update()
    clock.tick(60)
