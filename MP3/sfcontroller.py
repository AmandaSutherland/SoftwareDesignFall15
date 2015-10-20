# -*- coding: utf-8 -*-
"""
Controller of interactive video game Swim Little Fish Swim

@author: Amanda Sutherland, Ziyu (Selina) Wang

last modified: 10-18-15
"""


import pygame
from pygame.locals import *

class SwimFishMouseController:
    def __init__(self,model):
        self.model = model
    
    def handle_mouse_event(self,event):
        if event.type == MOUSEMOTION:
            self.model.fish.x = event.pos[0] #- self.model.fish.width/2.0
            self.model.fish.y = event.pos[1] #- self.model.fish.height/2.0


class SwimFishKeyboardController:
    def __init__(self,model):
        self.model = model

    def handle_key_event(self, event):
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            self.model.fish.x += -10
        if event.key == pygame.K_RIGHT:
            self.model.fish.x += 10
        if event.key == pygame.K_UP:
            self.model.fish.y += -10
        if event.key == pygame.K_DOWN:
            self.model.fish.y += 10


