# -*- coding: utf-8 -*-
"""
Runs interactive video game Swim Little Fish Swim

@author: Amanda Sutherland, Ziyu (Selina) Wang

last modified: 10-18-15
"""

import pygame
from pygame.locals import *
import sfcontroller
from sfcontroller import *
import sfmodel
from sfmodel import *
import sfview
from sfview import *
import random
import math
import time

            

if __name__ == '__main__':
    pygame.init()
    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = SwimFishModel()
    view = SwimFishView(model,screen)
    controller = SwimFishMouseController(model)
    # controller = SwimFishKeyboardController(model)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEMOTION:
                controller.handle_mouse_event(event)
                controller.handle_collision()
            # if event.type == KEYDOWN:
            #     controller.handle_key_event(event)
        view.draw()
        time.sleep(.001)

    pygame.quit()
