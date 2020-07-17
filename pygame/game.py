# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
from pygame.locals import *
from keyboard_controler import Keyboard_controler
from tetris_board import Tetris_board

import random
WIDTH = 293  # width of our game window
HEIGHT = 545 # height of our game window
FPS = 120 # frames per second

#define game set
BLOCK_SIZE = 20
MEDIUM_BOARD = 7

# define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
# screen.fill(RED)

# surf = pygame.Surface((50, 50))
# surf_position = {'x':200, 'y':200}
# surf.fill(GREEN)
# rect = surf.get_rect()
# screen.blit(surf,(surf_position['x'], surf_position['y']))
# pygame.display.flip()
keyboard_controler = Keyboard_controler()

area = []
for i in range(25):
    area.append([1,0,0,0,0,0,0,0,0,0,0,0,0,1])
area.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1])
surf = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
#draw
for i in range(0,len(area)):
    for j in range(len(area[i])):  
        surf_position = {'x':j*21, 'y':i*21}
        if area[i][j] == 1:
            surf.fill(GREEN)
        else:
            surf.fill(WHITE)
        rect = surf.get_rect()
        screen.blit(surf,(surf_position['x'], surf_position['y']))
pygame.display.flip()

# position = {'x':200, 'y':300}
# mytetris = tetris_board(position)
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    #     if event.type == KEYDOWN:
    #         if event.key == K_DOWN:
    #             keyboard_controler.addKey('Down')
    #         if event.key == K_UP:
    #             keyboard_controler.addKey('Up')
    #         if event.key == K_LEFT:
    #             keyboard_controler.addKey('Left')
    #         if event.key == K_RIGHT:
    #             keyboard_controler.addKey('Right')
    #         if event.key == K_ESCAPE:
    #             running = False
    #     if event.type == pygame.KEYUP:
    #         if event.key == K_DOWN:
    #             keyboard_controler.deleteKey('Down')
    #         if event.key == K_UP:
    #             keyboard_controler.deleteKey('Up')
    #         if event.key == K_LEFT:
    #             keyboard_controler.deleteKey('Left')
    #         if event.key == K_RIGHT:
    #             keyboard_controler.deleteKey('Right')
    # if keyboard_controler.hasKey('Down'):
    #     surf_position['y'] += 1
    #     screen.fill(RED)
    #     screen.blit(surf,(surf_position['x'], surf_position['y']))
    # if keyboard_controler.hasKey('Up'):
    #     surf_position['y'] -= 1
    #     screen.fill(RED)
    #     screen.blit(surf,(surf_position['x'], surf_position['y']))
    # if keyboard_controler.hasKey('Left'):
    #     surf_position['x'] -= 1
    #     screen.fill(RED)
    #     screen.blit(surf,(surf_position['x'], surf_position['y']))
    # if keyboard_controler.hasKey('Right'):
    #     surf_position['x'] += 1
    #     screen.fill(RED)
    #     screen.blit(surf,(surf_position['x'], surf_position['y']))

    # Update
    
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit() 