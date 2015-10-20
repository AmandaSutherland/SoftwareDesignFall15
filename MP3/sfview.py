# -*- coding: utf-8 -*-
"""
GUI of interactive video game Swim Little Fish Swim

@author: Amanda Sutherland, Ziyu (Selina) Wang

last modified: 10-18-15
"""

import pygame
from pygame.locals import *
import math

class SwimFishView:
    """ A view of swim little fish swim rendered in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
        
    def draw(self):
        ocean_blue = (100,149,237)
        self.screen.fill(ocean_blue)
        for monster in self.model.monsters:
            pygame.draw.rect(self.screen, pygame.Color(monster.color[0],monster.color[1],monster.color[2]),pygame.Rect(monster.x,monster.y,monster.width,monster.height))
        # Draws the fish
        points = []
        points.append((self.model.fish.x,self.model.fish.y))
        points.append((self.model.fish.x-20,self.model.fish.y+40))
        points.append((self.model.fish.x+20,self.model.fish.y+40))
        pygame.draw.polygon(self.screen, pygame.Color(self.model.fish.color[0],self.model.fish.color[1],self.model.fish.color[2]),points,0)
        pygame.draw.circle(self.screen, pygame.Color(self.model.fish.color[0],self.model.fish.color[1],self.model.fish.color[2]), (int(self.model.fish.x),int(self.model.fish.y)),int(self.model.fish.width)/4,0)
        pygame.draw.circle(self.screen, ocean_blue,(int(self.model.fish.x),int(self.model.fish.y-self.model.fish.width*0.25)),8,0)
        pygame.draw.circle(self.screen, (0,0,0),(int(self.model.fish.x+self.model.fish.width*0.125),int(self.model.fish.y-self.model.fish.width*0.12)),4,0)
        pygame.display.update()