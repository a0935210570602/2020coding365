# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
from pygame.locals import *
from keyboard_controler import Keyboard_controler

import random
WIDTH = 360  # width of our game window
HEIGHT = 480 # height of our game window
FPS = 120 # frames per second

# Colors (R, G, B)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
running = True
screen.fill(RED)
pygame.display.flip()
surf = pygame.Surface((50, 50))
surf_position = {'x':200, 'y':200}
surf.fill(GREEN)
rect = surf.get_rect()
screen.blit(surf,(surf_position['x'], surf_position['y']))
pygame.display.flip()

keyboard_controler = Keyboard_controler()
while running:
    # keep loop running at the right speed
    clock.tick(FPS)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                keyboard_controler.addKey('Down')
            if event.key == K_UP:
                keyboard_controler.addKey('Up')
            if event.key == K_LEFT:
                keyboard_controler.addKey('Left')
            if event.key == K_RIGHT:
                keyboard_controler.addKey('Right')
            if event.key == K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            if event.key == K_DOWN:
                keyboard_controler.deleteKey('Down')
            if event.key == K_UP:
                keyboard_controler.deleteKey('Up')
            if event.key == K_LEFT:
                keyboard_controler.deleteKey('Left')
            if event.key == K_RIGHT:
                keyboard_controler.deleteKey('Right')
    if keyboard_controler.hasKey('Down'):
        surf_position['y'] += 1
        screen.fill(RED)
        screen.blit(surf,(surf_position['x'], surf_position['y']))
    if keyboard_controler.hasKey('Up'):
        surf_position['y'] -= 1
        screen.fill(RED)
        screen.blit(surf,(surf_position['x'], surf_position['y']))
    if keyboard_controler.hasKey('Left'):
        surf_position['x'] -= 1
        screen.fill(RED)
        screen.blit(surf,(surf_position['x'], surf_position['y']))
    if keyboard_controler.hasKey('Right'):
        surf_position['x'] += 1
        screen.fill(RED)
        screen.blit(surf,(surf_position['x'], surf_position['y']))
        
pygame.quit() 