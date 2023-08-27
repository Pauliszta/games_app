import pygame
from pygame.locals import *
import sys
import random

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXEL_TO_MOVE = 3


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ballImage = pygame.image.load('ball/images/ball.png')
targetImage = pygame.image.load('ball/images/target.jpg')
bounceSound = pygame.mixer.Sound('sounds/boing.wav')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0)

ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keyPressedTuple = pygame.key.get_pressed()

        if keyPressedTuple[pygame.K_LEFT]:
            ballX = ballX - N_PIXEL_TO_MOVE
        if keyPressedTuple[pygame.K_RIGHT]:
            ballX = ballX + N_PIXEL_TO_MOVE
        if keyPressedTuple[pygame.K_UP]:
            ballY = ballY - N_PIXEL_TO_MOVE
        if keyPressedTuple[pygame.K_DOWN]:
            ballY = ballY + N_PIXEL_TO_MOVE

        if event.type == pygame.MOUSEBUTTONUP:
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)

        ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
        if ballRect.colliderect(targetRect):
            bounceSound.play()
            print('Gratulacje! Udało Ci się znaleźć miejsce docelowe dla piłki.')
    
    
    window.fill(BLACK)

    window.blit(ballImage, (ballX, ballY))


    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
