# -*- coding: utf-8 -*-
"""
GUI of interactive video game Swim Little Fish Swim

@author: Amanda Sutherland, Ziyu (Selina) Wang

last modified: 10-18-15
"""

import pygame
from pygame.locals import *

class SwimFishView:
    """ A view of swim little fish swim rendered in a Pygame window """
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
        
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        for monster in self.model.monsters:
            pygame.draw.rect(self.screen, pygame.Color(monster.color[0],monster.color[1],monster.color[2]),pygame.Rect(monster.x,monster.y,monster.width,monster.height))
        pygame.draw.rect(self.screen, pygame.Color(self.model.fish.color[0],self.model.fish.color[1],self.model.fish.color[2]),pygame.Rect(self.model.fish.x,self.model.fish.y,self.model.fish.width,self.model.fish.height))     
#        pygame.draw.rect(self.screen, pygame.Color(self.model.ball.color[0],self.model.ball.color[1],self.model.ball.color[2]),pygame.Rect(self.model.ball.x,self.model.ball.y,self.model.ball.width,self.model.ball.height))
        pygame.display.update()