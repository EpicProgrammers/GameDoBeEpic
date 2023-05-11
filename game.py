import pygame
import events as e
import player as p
import map_load as m
import orb as o
from pygame.locals import *
pygame.init()

class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.display = pygame.Surface((480, 270))
        self.player = p.Player(40, 40, self.display)
        self.orbs = []
        self.orb_count = 3
        starting_angle = 0
        for i in range(self.orb_count):
            orb = o.Orb(self.display, self.player.x, self.player.y, starting_angle)
            self.orbs.append(orb)
            starting_angle += 120
        self.true_scroll = [0, 0]
        self.map = m.Map_load()
        self.event_dict = {'move_left': False, 'move_right': False, 'jump': False, 'dash': False, 'shoot': False, 'idle_orb': True}
        self.events = e.Events(self.event_dict)
        self.map_data = self.map.get_map("test_map.json")
        self.scroll = [0, 0]
        self.gaming = True
        #self.gray = (112,128,144)
        self.blue = (140, 230, 250)


    def main(self):  # looping for real this time
        while self.gaming:
            self.display.fill((self.blue))
            object_list = self.map.load_map(self.map_data, self.scroll, self.display)
            self.player.move(self.event_dict)
            self.player.collide(object_list)
            self.true_scroll[0] += (self.player.rect.x-self.true_scroll[0]-1920/8.1)/5
            self.true_scroll[1] += (self.player.rect.y-self.true_scroll[1]-1080/6.5)/5
            self.scroll = self.true_scroll.copy()
            self.scroll = [int(a) for a in self.scroll]

            self.player.render(self.scroll)
            for i in range(self.orb_count):
                if self.event_dict['idle_orb']:
                    self.orbs[i].vibe((self.player.x, self.player.y + 3))
                    self.orbs[i].render(self.scroll)

            self.event_dict = self.events.check_events()

            surf = pygame.transform.scale(self.display, (1920, 1080))
            self.screen.blit(surf, (0, 0))
            pygame.display.update()
            self.clock.tick(60)