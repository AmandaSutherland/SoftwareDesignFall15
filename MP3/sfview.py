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
        # ocean_blue = (100,149,237)
        # self.screen.fill(ocean_blue)
        img=pygame.image.load('images/ocean.jpg') 
        self.screen.blit(img,(0,0))
        # Draws the fish
        points = []
        points.append((self.model.fish.x,self.model.fish.y))
        points.append((self.model.fish.x-20,self.model.fish.y+45))
        points.append((self.model.fish.x+20,self.model.fish.y+45))
        pygame.draw.polygon(self.screen, pygame.Color(self.model.fish.color[0],self.model.fish.color[1],self.model.fish.color[2]),points,0)
        pygame.draw.ellipse(self.screen, pygame.Color(self.model.fish.color[0],self.model.fish.color[1],self.model.fish.color[2]),pygame.Rect(self.model.fish.x-self.model.fish.width/2,self.model.fish.y-self.model.fish.height/2,self.model.fish.width,self.model.fish.height),0)
        # pygame.draw.circle(self.screen, pygame.Color(self.model.fish.color[0],self.model.fish.color[1],self.model.fish.color[2]), (int(self.model.fish.x),int(self.model.fish.y)),int(self.model.fish.width)/4,0)
        # pygame.draw.circle(self.screen, ocean_blue,(int(self.model.fish.x),int(self.model.fish.y-self.model.fish.width*0.6)),7,0) # Draws the mouth
        pygame.draw.circle(self.screen, (0,20,20),(int(self.model.fish.x+self.model.fish.width*0.25),int(self.model.fish.y-self.model.fish.width*0.25)),4,0) # Draws the eye

        for monster in self.model.monsters:
            pygame.draw.rect(self.screen, pygame.Color(monster.color[0],monster.color[1],monster.color[2]),pygame.Rect(monster.x,monster.y,monster.width,monster.height))

        # Draws the ocean beds
        img1=pygame.image.load('images/beach.jpg') 
        self.screen.blit(img1,(self.model.leftWall.x,self.model.leftWall.y))
        self.screen.blit(img1,(self.model.rightWall.x,self.model.rightWall.y))
        # pygame.draw.rect(self.screen, pygame.Color(self.model.leftWall.color[0],self.model.leftWall.color[1],self.model.leftWall.color[2]),pygame.Rect(self.model.leftWall.x,self.model.leftWall.y,self.model.leftWall.width,self.model.leftWall.height),0)
        # pygame.draw.rect(self.screen, pygame.Color(self.model.rightWall.color[0],self.model.rightWall.color[1],self.model.rightWall.color[2]),pygame.Rect(self.model.rightWall.x,self.model.rightWall.y,self.model.rightWall.width,self.model.rightWall.height),0) 
        pygame.display.update()