import random

import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Caption and icon
pygame.display.set_caption("Fox Hunt")
icon = pygame.image.load('logo.bmp')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = 64
enemyY = 64
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        # 5 = 5 + -0.1 -> 5 = 5 - 0.1
        # 5 = 5 + 0.1

        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736


    # Enemy Movement

        enemyX += enemyX_change
        if enemyX <= 0:
            enemyX_change = 4
            enemyY += enemyY_change
        elif enemyX >= 736:
            enemyX_change = -4
            enemyY += enemyY_change












































    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
