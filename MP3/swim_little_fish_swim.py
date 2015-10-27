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
    view = SwimFishView(model, screen)
    controller = SwimFishMouseController(model, view)
    # controller = SwimFishKeyboardController(model)

    choices = ['images/octopus1_png.png', 'images/crab1.png', 'images/jellyfish.png', 'images/shark.png', 'images/stingray.png']

    running = True
    playing = True
    eaten = False
    playAgain = False
    init = time.time()
    last_monster_spawn = init
    time_since_last_movement = init
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
            #control the monsters's spawning
            if now - last_monster_spawn >= 2.5:
                last_monster_spawn = now
                for x in range(100,620,310):
                    choice = choices[random.randint(0, 4)]
                    monster = Monster(100, 100, choice, x, 0)
                    model.monsters.append(monster)
            #control the monsters' movement
            if now - time_since_last_movement >= 0.1:
                time_since_last_movement = now 
                for monster in model.monsters:
                    monster.move_monster()
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
