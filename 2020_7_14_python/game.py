# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame 
from pygame.locals import*

pygame.init()


width, height = 640, 480                      
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Andy's game")        

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

