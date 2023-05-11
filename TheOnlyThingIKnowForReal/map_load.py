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

    def get_map(file_name):
        f = open(file_name)
        dat = json.load(f)
        f.close()
        data = dat["levels"][0]["layerInstances"][0]["gridTiles"]
        length = len(dat["levels"][0]["layerInstances"][0]["gridTiles"])
        return data, length

    def load_map(self, dat, scroll, display):
        object_list = []
        length = dat[1]
        data = dat[0]
        for x in range(length):
            px = data[x]["px"]
            t = data[x]["t"]
            if t == 1:
                display.blit(self.grass_img, (px[0] - scroll[0], px[1] - 3 - scroll[1]))
            elif t == 0:
                display.blit(self.grass_left, (px[0] - 3 - scroll[0], px[1] - 3 - scroll[1]))
            elif t == 2:
                display.blit(self.grass_right, (px[0] - scroll[0], px[1] - 3 - scroll[1]))
            elif t == 3:
                display.blit(self.dirt_mid_left, (px[0] - scroll[0], px[1] - scroll[1]))
            elif t == 4:
                display.blit(self.dirt_mid_mid, (px[0] - scroll[0], px[1] - scroll[1]))
            elif t == 5:
                display.blit(self.dirt_mid_right, (px[0] - scroll[0], px[1] - scroll[1]))
            elif t == 6:
                display.blit(self.dirt_bot_left, (px[0] - scroll[0], px[1] - scroll[1]))
            elif t == 7:
                display.blit(self.dirt_bot_mid, (px[0] - scroll[0], px[1] - scroll[1]))
            elif t == 8:
                display.blit(self.dirt_bot_right, (px[0] - scroll[0], px[1] - scroll[1]))
            object_list.append(pygame.Rect(px[0], px[1], 16, 16))
        return object_list