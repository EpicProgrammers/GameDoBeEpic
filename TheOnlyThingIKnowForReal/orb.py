import pygame
import math
import core_functions as f
from pygame.locals import *


class Orb(object):
    def __init__(self, surface, x, y, starting_angle):
        self.img = f.load_img('images/orb/orb1.png')
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
        self.idle = True
        self.surface = surface
        self.position_list = []
        self.center_of_rotation_x = x
        self.center_of_rotation_y = y 
        self.starting_angle = starting_angle
        for i in range(64):
            if i == 0 or i == 17 or i == 33 or i == 49:
                z = 0
            if i <= 16:
                pp = [self.x + z, self.y + z]
            elif i <= 32:
                pp = [self.x + 16 - z, self.y + 16 + z]
            elif i <= 48:
                pp = [self.x - z, self.y + 32 - z]
            else:
                pp = [self.x - 16 + z, self.y + 16 - z]
            self.position_list.append(pp)
            z += 1
        self.list_pos = 0
        self.p_move = [x, y]
        self.radius = 21
        self.angle = math.radians(self.starting_angle)  # pi/4 # starting angle 45 degrees
        self.omega = 0.03  # Angular velocity
        self.action = 'idle'
        self.x_offset = math.sin(self.angle) * self.radius
        self.y_offset = int(math.cos(self.angle) * self.radius)


    def vibe(self, distance):
        if self.action == 'idle':
            self.center_of_rotation_x = distance[0]
            self.center_of_rotation_y = distance[1]
            self.x = self.center_of_rotation_x + self.radius * math.cos(self.angle)  # Starting position x
            self.y = self.center_of_rotation_y - self.radius * math.sin(self.angle)  # Starting position y
            
        elif self.action == 'shoot':
            self.x += 5
    

    def display(self, scroll):
        self.surface.blit(self.img, (self.x - scroll[0], self.y - scroll[1]))
        self.angle = self.angle + self.omega  # New angle, we add angular velocity
        self.x = self.x + self.radius * self.omega * math.cos(self.angle + math.pi / 2)  # New x
        self.y = self.y - self.radius * self.omega * math.sin(self.angle + math.pi / 2)  # New y

    def rotate(self, distance):
        self.center_of_rotation_x = distance[0]
        self.center_of_rotation_y = distance[1]
        self.x = self.center_of_rotation_x + self.x_offset
        self.y = self.center_of_rotation_y - self.y_offset


