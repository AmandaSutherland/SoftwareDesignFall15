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
    sound = pygame.mixer.Sound("sounds/POL-coconut-land-short.wav")
    sound.play(loops = -1)
    sound.set_volume(0.4)

    model = SwimFishModel()
    view = SwimFishView(model,screen)
    controller = SwimFishMouseController(model,view)
    # controller = SwimFishKeyboardController(model)

    running = True
    playing = True
    eaten = False
    playAgain = False
    init = time.time()
    counter = 0
    view.init_screen()
    time.sleep(5)
    while running:
        while playing and not eaten:
            now = time.time()
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:   #event is escape key
                        pygame.quit()
                elif event.type == MOUSEMOTION:
                    controller.handle_mouse_event(event)
                    # controller.handle_collision()
                # if event.type == KEYDOWN:
                #     controller.handle_key_event(event)
            view.draw()
            if (controller.handle_collision()):
                eaten = True
                init = time.time()
            if (now-init >= 10):
                view.level_up()
                time.sleep(5)
                counter = 0
                init = time.time()
            time.sleep(0.01)

        while eaten:
            if (counter <= 3):
                view.eaten()
                eaten = False
                playing = True
                time.sleep(3)
                counter += 1;
            else:
                view.lost()
                time.sleep(5)
                sound.stop()
                pygame.quit()
