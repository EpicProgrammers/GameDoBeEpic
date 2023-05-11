import json
import pygame
import core_functions as f
from pygame.locals import *

class Map_load(object):
    def __init__(self):
        self.dirt_img = f.load_img('images/tiles/dirto.png')
        self.grass_img = f.load_img('images/tiles/graso.png')
        self.grass_left = f.load_img('images/tiles/grass_left.png')
        self.grass_right = f.load_img('images/tiles/grass_right.png')
        self.dirt_mid_mid = f.load_img('images/tiles/dirt_mid_mid.png')
        self.dirt_mid_left = f.load_img('images/tiles/dirt_mid_left.png')
        self.dirt_mid_right = f.load_img('images/tiles/dirt_mid_right.png')
        self.dirt_bot_mid = f.load_img('images/tiles/dirt_bot_mid.png')
        self.dirt_bot_left = f.load_img('images/tiles/dirt_bot_left.png')
        self.dirt_bot_right = f.load_img('images/tiles/dirt_bot_right.png')


    def get_map(self, file_name):
        f = open(file_name)
        dat = json.load(f)
        f.close()
        data = dat["levels"][0]["layerInstances"][0]["gridTiles"]
        length = len(dat["levels"][0]["layerInstances"][0]["gridTiles"])
        return data, length


    def load_map(self, raw_data, scroll, display):
        self.object_list = []
        self.length = raw_data[1]
        self.data = raw_data[0]
        self.render(scroll, display)
        return self.object_list
        
    
    def render(self, scroll, display):
        for x in range(self.length):
            coordinates = self.data[x]["px"] 
            tile_type = self.data[x]["t"]
            if tile_type == 1:
                display.blit(self.grass_img, (coordinates[0] - scroll[0], coordinates[1] - 3 - scroll[1]))
            elif tile_type == 0:
                display.blit(self.grass_left, (coordinates[0] - 3 - scroll[0], coordinates[1] - 3 - scroll[1]))
            elif tile_type == 2:
                display.blit(self.grass_right, (coordinates[0] - scroll[0], coordinates[1] - 3 - scroll[1]))
            elif tile_type == 3:
                display.blit(self.dirt_mid_left, (coordinates[0] - scroll[0], coordinates[1] - scroll[1]))
            elif tile_type == 4:
                display.blit(self.dirt_mid_mid, (coordinates[0] - scroll[0], coordinates[1] - scroll[1]))
            elif tile_type == 5:
                display.blit(self.dirt_mid_right, (coordinates[0] - scroll[0], coordinates[1] - scroll[1]))
            elif tile_type == 6:
                display.blit(self.dirt_bot_left, (coordinates[0] - scroll[0], coordinates[1] - scroll[1]))
            elif tile_type == 7:
                display.blit(self.dirt_bot_mid, (coordinates[0] - scroll[0], coordinates[1] - scroll[1]))
            elif tile_type == 8:
                display.blit(self.dirt_bot_right, (coordinates[0] - scroll[0], coordinates[1] - scroll[1]))
            self.object_list.append(pygame.Rect(coordinates[0], coordinates[1], 16, 16))