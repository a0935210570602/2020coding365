# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame
from pygame.locals import *
import random

WIDTH = 360  # width of our game window
HEIGHT = 480 # height of our game window
FPS = 30 # frames per second
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
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
has_key_down = 0
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                has_key_down = 1
            if event.key == K_UP:
                has_key_down = 2
            if event.key == K_LEFT:
                has_key_down = 3
            if event.key == K_RIGHT:
                has_key_down = 4
            if event.key == K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            if event.key == K_DOWN or event.key == K_UP or event.key == K_LEFT or event.key == K_RIGHT:
                has_key_down = 0
    if has_key_down == 1:
        surf_position['y'] += 1
        screen.fill(RED)
        screen.blit(surf,(surf_position['x'], surf_position['y']))
    if has_key_down == 2:
        surf_position['y'] -= 1
        screen.fill(RED)
        screen.blit(surf,(surf_position['x'], surf_position['y']))
    if has_key_down == 3:
        surf_position['x'] -= 1
        screen.fill(RED)
        screen.blit(surf,(surf_position['x'], surf_position['y']))
    if has_key_down == 4:
        surf_position['x'] += 1
        screen.fill(RED)
        screen.blit(surf,(surf_position['x'], surf_position['y']))
        
pygame.quit() 