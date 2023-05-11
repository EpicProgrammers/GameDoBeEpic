import pygame
import math
from pygame.locals import *

def load_img(path):
    img = pygame.image.load(path).convert()
    img.set_colorkey((0, 0, 0))
    return img


def fancy_spin(self, distance):
    self.center_of_rotation_x = distance[0]
    self.center_of_rotation_y = distance[1]
    self.x = self.center_of_rotation_x + self.radius * math.cos(self.angle)  # Starting position x
    self.y = self.center_of_rotation_y - self.radius * math.sin(self.angle)  # Starting position y
    

   # def display(self, scroll):
     #   self.surface.blit(self.img, (self.x - scroll[0], self.y - scroll[1]))
    #    self.angle = self.angle + self.omega  # New angle, we add angular velocity
     #   self.x = self.x + self.radius * self.omega * math.cos(self.angle)  # New x
     #   self.y = self.y - self.radius * self.omega * math.sin(self.angle)  # New y
