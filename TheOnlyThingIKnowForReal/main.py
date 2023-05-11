import pygame
import sys
import core_functions as f
import events as e
import player as p
import map_load as m
import orb as o
import game
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1080))
display = pygame.Surface((480, 270))

# To do:
# 1. images
# 2. animations

dirt_img = f.load_img('images/tiles/dirto.png')
grass_img = pygame.image.load('images/tiles/graso.png').convert()
grass_img.set_colorkey((0, 0, 0))
grass_left = pygame.image.load('images/tiles/grass_left.png').convert()
grass_left.set_colorkey((0, 0, 0))
grass_right = pygame.image.load('images/tiles/grass_right.png').convert()
grass_right.set_colorkey((0, 0, 0))
dirt_mid_mid = pygame.image.load('images/tiles/dirt_mid_mid.png').convert()
dirt_mid_left = pygame.image.load('images/tiles/dirt_mid_left.png').convert()
dirt_mid_right = pygame.image.load('images/tiles/dirt_mid_right.png').convert()
dirt_bot_mid = pygame.image.load('images/tiles/dirt_bot_mid.png').convert()
dirt_bot_left = pygame.image.load('images/tiles/dirt_bot_left.png').convert()
dirt_bot_right = pygame.image.load('images/tiles/dirt_bot_right.png').convert()


player = p.Player(40, 40, display)

orbs = []
orb_count = 3
starting_angle = 0
for i in range(orb_count):
    orb = o.Orb(display, player.x, player.y, starting_angle)
    orbs.append(orb)
    starting_angle += 120



true_scroll = [0, 0]

def load_map(dat, scroll):
    object_list = []
    length = dat[1]
    data = dat[0]
    for x in range(length):
        px = data[x]["px"]
        t = data[x]["t"]
        if t == 1:
            display.blit(grass_img, (px[0] - scroll[0], px[1] - 3 - scroll[1]))
        elif t == 0:
            display.blit(
                grass_left, (px[0] - 3 - scroll[0], px[1] - 3 - scroll[1]))
        elif t == 2:
            display.blit(
                grass_right, (px[0] - scroll[0], px[1] - 3 - scroll[1]))
        elif t == 3:
            display.blit(dirt_mid_left, (px[0] - scroll[0], px[1] - scroll[1]))
        elif t == 4:
            display.blit(dirt_mid_mid, (px[0] - scroll[0], px[1] - scroll[1]))
        elif t == 5:
            display.blit(dirt_mid_right,
                         (px[0] - scroll[0], px[1] - scroll[1]))
        elif t == 6:
            display.blit(dirt_bot_left, (px[0] - scroll[0], px[1] - scroll[1]))
        elif t == 7:
            display.blit(dirt_bot_mid, (px[0] - scroll[0], px[1] - scroll[1]))
        elif t == 8:
            display.blit(dirt_bot_right,
                         (px[0] - scroll[0], px[1] - scroll[1]))
        object_list.append(pygame.Rect(px[0], px[1], 16, 16))
    return object_list


def main():  # looping for real this time
    map_data = m.get_map("test_map.json")
    scroll = [0, 0]
    gaming = True
    event_dict = {
        'move_left': False, 'move_right': False, 'jump': False, 'dash': False, 'shoot': False, 'idle_orb': True
        }
    gray = (112,128,144)
    blue = (140, 230, 250)
    while gaming:
        display.fill((blue))
        object_list = load_map(map_data, scroll)
        movement = player.move(event_dict)
        player.collide(object_list)
        true_scroll[0] += (player.rect.x-true_scroll[0]-1920/8.1)/5
        true_scroll[1] += (player.rect.y-true_scroll[1]-1080/6.5)/5
        scroll = true_scroll.copy()
        print(scroll)
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
        print(scroll)

        player.p_display(scroll)
        for i in range(orb_count):
            if event_dict['idle_orb']:
                orbs[i].rotate((player.x, player.y + 5))
                orbs[i].vibe((player.x, player.y))
                orbs[i].display(scroll)
        

        event_dict = e.events(event_dict)

        surf = pygame.transform.scale(display, (1920, 1080))
        screen.blit(surf, (0, 0))
        pygame.display.update()
        clock.tick(60)


#main()
game = game.Game()
game.main()