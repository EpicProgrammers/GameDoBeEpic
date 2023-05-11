import pygame
import math
import core_functions as f
from pygame.locals import *


class Orb(object):
    def __init__(self, display, x, y, starting_angle):
        self.img = f.load_img('images/orb/orb1.png')
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
        self.display = display
        self.center_of_rotation_x = x
        self.center_of_rotation_y = y 
        self.starting_angle = starting_angle
        self.radius = 21  # distance from player to orb
        self.angle = math.radians(self.starting_angle)  # starting angle, 0, 120, 240
        self.omega = 0.03  # Angular velocity
        self.action = 'idle'


    def vibe(self, distance):
        if self.action == 'idle':
            self.center_of_rotation_x = distance[0] # player position
            self.center_of_rotation_y = distance[1]
            self.x = self.center_of_rotation_x + self.radius * math.cos(self.angle)  # x position
            self.y = self.center_of_rotation_y - self.radius * math.sin(self.angle)  # y position
        elif self.action == 'shoot':
            self.x += 5

    
    def render(self, scroll):
        self.display.blit(self.img, (self.x - scroll[0], self.y - scroll[1]))
        self.angle = self.angle + self.omega  # New angle, we add angular velocity


