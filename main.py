import pygame 
#Initialize the pygame
pygame.init()

#Creating screen
screen = pygame.display.set_mode((800,600))

#Icon and Title
pygame.display.set_caption("Jumper")
icon = pygame.image.load('fences.png')
pygame.display.set_icon(icon)

#Character / Player
playerImg = pygame.image.load('gnome.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player():
    screen.blit(playerImg,(playerX,playerY))

#Game loop, all events go here
running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #Keystroke arrow pressed? Which direction?
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.1
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.1
            if event.key == pygame.K_UP:
                playerY_change -= 0.1
            if event.key == pygame.K_DOWN:
                playerY_change += 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    playerY += playerY_change
    playerX += playerX_change
    player()
    pygame.display.update()
    
