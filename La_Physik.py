import pygame
from pygame.locals import *


class Physiks_obj(object):
    def __init__(self, x, y, x_size, y_size):
        self.width = x_size
        self.height = y_size
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.x = x
        self.y = y
        self.collision_types = {}

    def move(self, rect, movement, platforms):
        self.collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        self.rect = rect
        self.x = self.rect.x
        self.y = self.rect.y
        self.horizontal_collisions(movement[0], platforms)
        self.vertical_collisions(movement[1], platforms)
        return self.collision_types


    def horizontal_collisions(self, movement, platforms):
        self.x += movement
        self.rect.x = int(self.x)
        self.block_hit_list = self.collision_test(self.rect, platforms)
        self.horizontal_collide(movement)
        
    
    def horizontal_collide(self, movement):
        for block in self.block_hit_list:
            if movement > 0:
                self.rect.right = block.left
                self.collision_types['right'] = True
            elif movement < 0:
                self.rect.left = block.right
                self.collision_types['left'] = True
            self.x = self.rect.x


    def vertical_collisions(self, movement, platforms):
        self.y += movement
        self.rect.y = int(self.y)
        self.block_hit_list = self.collision_test(self.rect, platforms)
        self.vertical_collide(movement)
    

    def vertical_collide(self, movement):
        for block in self.block_hit_list:
            if movement > 0:
                self.rect.bottom = block.top
                self.collision_types['bottom'] = True
            elif movement < 0:
                self.rect.top = block.bottom
                self.collision_types['top'] = True
            self.change_y = 0
            self.y = self.rect.y
    

    def collision_test(self, object_1, object_list):
        hit_list = []
        for obj in object_list:
            if obj.colliderect(object_1):
                hit_list.append(obj)
        return hit_list