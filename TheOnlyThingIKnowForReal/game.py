import pygame
import sys
import core_functions as f
import events as e
import player as p
import map_load as m
import orb as o
from pygame.locals import *
pygame.init()

class Game():
    def __init__(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((1920, 1080))
        display = pygame.Surface((480, 270))

        player = p.Player(40, 40, display)

        orbs = []
        orb_count = 3
        starting_angle = 0
        for i in range(orb_count):
            orb = o.Orb(display, player.x, player.y, starting_angle)
            orbs.append(orb)
            starting_angle += 120

        true_scroll = [0, 0]

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