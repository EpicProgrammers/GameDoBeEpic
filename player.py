import pygame
from pygame.locals import *
import core_functions as f
import La_Physik as p


class Player(object):
    def __init__(self, x, y, display) -> None:
        self.img = f.load_img("images/mister.png")
        self.l_img = pygame.transform.flip(self.img, True, False)
        self.size_x = self.img.get_width()
        self.size_y = self.img.get_height()
        self.x = x
        self.y = y
        self.obj = p.Physiks_obj(x, y, self.size_x, self.size_y)
        self.display = display
        self.y_move = 0
        self.gravity = 0.25
        self.air_timer = 0
        self.jumps = 0
        self.jump_height = -4
        self.moving_right = False
        self.moving_left = False
        self.facing_left = False
        self.facing_right = True
        self.shoot_right = False
        self.movement = [0, 0]
        self.dashes = 2
        self.dash_cooldown = 120
        self.dash_duration = 20
        self.event_dict = {}


    def collide(self, platforms):
        collisions = self.obj.move(self.rect, self.movement, platforms)
        self.x = self.obj.x
        self.y = self.obj.y
        if collisions['bottom']:
            self.y_move = 0
            self.air_timer = 0
            self.jumps = 0
        if collisions['top']:
            self.y_move = 0
        elif self.air_timer < 7:
            self.air_timer += 1


    def move(self, event_dict):
        self.event_dict = event_dict
        self.movement = [0, 0]
        self.move_x()
        self.dash()
        self.move_y()
        self.rect = pygame.Rect(self.x, self.y, self.size_x, self.size_y)

    
    def move_x(self):
        if self.event_dict['move_right']:
            self.movement[0] += 2
            self.facing_right = True
            self.facing_left = False
        if self.event_dict['move_left']:
            self.movement[0] -= 2
            self.facing_left = True
            self.facing_right = False


    def dash(self):
        if self.event_dict['dash'] and self.dash_cooldown >= 120: # and self.dash_duration > 0:
            if self.facing_left:
                self.movement[0] -= 30
                self.dash_cooldown = 0
            if self.facing_right and self.dash_cooldown >= 120:
                self.movement[0] += 30
                self.dash_cooldown = 0
        if self.dash_cooldown < 120:
            self.dash_cooldown += 1
        if self.dash_duration > 0:
            self.dash_duration -= 1
            
        
    def move_y(self):
        self.movement[1] += self.y_move
        self.y_move += self.gravity
        if self.y_move > 3:
            self.y_move = 3
        if self.event_dict['jump'] and self.air_timer < 6 and self.jumps < 1:
            self.y_move = self.jump_height
            self.jumps += 1


    def render(self, scroll):
        if self.facing_left:
            self.display.blit(self.l_img, (self.x - scroll[0], self.y - scroll[1]))
        if self.facing_right:
            self.display.blit(self.img, (self.x - scroll[0], self.y - scroll[1]))
