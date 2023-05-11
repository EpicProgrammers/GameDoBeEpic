import sys
import pygame
from pygame.locals import *

class Events(object):
    def __init__(self, event_dict) -> None:
        self.event_dict = event_dict


    def check_events(self):
        for self.event in pygame.event.get():
            if self.event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if  self.event.type == KEYDOWN:
                self.key_press()
            if self.event.type == KEYUP:
                self.key_release()                
        return self.event_dict
    

    def key_press(self):
        if self.event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if self.event.key == K_w or self.event.key == K_SPACE:
            self.event_dict['jump'] = True
        if self.event.key == K_a:
            self.event_dict['move_left'] = True
        if self.event.key == K_d:
            self.event_dict['move_right'] = True
        if self.event.type == K_LSHIFT:
            self.event_dict['dash'] = True
        if self.event.type == K_s:
            pass


    def key_release(self):
        if self.event.key == K_a:
            self.event_dict['move_left'] = False
        if self.event.key == K_d:
            self.event_dict['move_right'] = False
        if self.event.key == K_w or self.event.key == K_SPACE:
            self.event_dict['jump'] = False
        if self.event.type ==K_RIGHT:
            self.event_dict['shoot'] = False
        if self.event.type == K_LSHIFT:
            self.event_dict['dash'] = False
        
