import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo_icon.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('ufo.png')
playerX = 475
playerY = 600
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('laser-gun.png'))
    enemyX.append(random.randint(0, 950))
    enemyY.append((random.randint(0, 200)))
    enemyX_change.append(2)
    enemyY_change.append(25)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 600
bulletX_change = 0
bulletY_change = 5
bullet_state = 'ready'

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 30)
textX = 10
textY = 10

#Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 80)


def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255, 120,120))
    screen.blit(over_text, (260,250))

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 20, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Create the screen
screen = pygame.display.set_mode((1000, 650))
# background = pygame.image.load('background.jpg')

# Game Loop
running = True
while running:
    screen.fill((220, 180, 190))
    # background
    # screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4

            if event.key == pygame.K_RIGHT:
                playerX_change = 4

            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # Checking boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 950:
        playerX = 950
    player(playerX, playerY)

    for i in range(num_of_enemies):
        #Game Over
        if enemyY[i] > 570:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 950:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 600
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 950)
            enemyY[i] = random.randint(0, 200)
        enemy(enemyX[i], enemyY[i], i)
    # Bullet movement
    if bulletY <= 0:
        bulletY = 600
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    show_score(textX, textY)

    pygame.display.update()
