import sys
import pygame
from pygame.locals import *


def events(event_dict):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        if  event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print('lol')
                pygame.quit()
                sys.exit()
            if event.key == K_w or event.key == K_SPACE:
                event_dict['jump'] = True
                print('jump')
            if event.key == K_a:
                event_dict['move_left'] = True
            if event.key == K_d:
                event_dict['move_right'] = True
                print('right')
            if event.type == K_LSHIFT:
                event_dict['dash'] = True
                print("lol")
            if event.type == K_s:
                print("down")

        if event.type == KEYUP:
            if event.key == K_a:
                event_dict['move_left'] = False
            if event.key == K_d:
                event_dict['move_right'] = False
            if event.key == K_w or event.key == K_SPACE:
                event_dict['jump'] = False
            if event.type ==K_RIGHT:
                event_dict['shoot'] = False
            if event.type == K_LSHIFT:
                event_dict['dash'] = False
            
    return event_dict
        
