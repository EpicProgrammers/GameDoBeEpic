import pygame
import collisionTest as c
from pygame.locals import *


class Physiks_obj(object):
    def __init__(self, x, y, x_size, y_size):
        self.width = x_size
        self.height = y_size
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.x = x
        self.y = y

    def move(self, rect, movement, platforms):
        self.rect = rect
        self.x = self.rect.x
        self.y = self.rect.y
        self.x += movement[0]
        self.rect.x = int(self.x)
        block_hit_list = c.collision_test(self.rect, platforms)
        collision_types = {'top': False, 'bottom': False, 'right': False,
                           'left': False, 'slant_bottom': False, 'data': []}
        # added collision data to "collision_types". ignore the poorly chosen variable name
        for block in block_hit_list:
            markers = [False, False, False, False]
            if movement[0] > 0:
                self.rect.right = block.left
                collision_types['right'] = True
                markers[0] = True
            elif movement[0] < 0:
                self.rect.left = block.right
                collision_types['left'] = True
                markers[1] = True
            collision_types['data'].append([block, markers])
            self.x = self.rect.x
        self.y += movement[1]
        self.rect.y = int(self.y)
        block_hit_list = c.collision_test(self.rect, platforms)
        for block in block_hit_list:
            markers = [False, False, False, False]
            if movement[1] > 0:
                self.rect.bottom = block.top
                collision_types['bottom'] = True
                markers[2] = True
            elif movement[1] < 0:
                self.rect.top = block.bottom
                collision_types['top'] = True
                markers[3] = True
            collision_types['data'].append([block, markers])
            self.change_y = 0
            self.y = self.rect.y
        return collision_types
