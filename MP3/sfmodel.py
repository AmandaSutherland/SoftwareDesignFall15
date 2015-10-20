# -*- coding: utf-8 -*-
"""
Model of interactive video game Swim Little Fish Swim

@author: Amanda Sutherland, Ziyu (Selina) Wang

last modified: 10-18-15
"""


import pygame
from pygame.locals import *


class SwimFishModel:
    """ Encodes the game state """
    def __init__(self):
        self.monsters = []
        for x in range(100,620,310):
            monster = Monster((205,79,57),15,10,x,120)
            self.monsters.append(monster)
        self.fish = Fish((209,95,238),60,50,200,450)
        self.leftWall = Wall((205,133,63),480,50,0,0)
        self.rightWall = Wall((205,133,63),480,50,590,0)


class Monster:
    """ Encodes the state of a monster in the game """
    def __init__(self,img,height,width,x,y):
        self.img = pygame.image.load('images/octopus1_png.png')
        # self.scale = scale('images/octopus1_png.png', (0.2, 0.2), DestSurface = None) 
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class Fish:
    """ Encodes the state of the fish in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class Wall:
   """ Encodes the state of the wall in the game """
   def __init__(self,color,height,width,x,y):
       self.color = color
       self.height = height
       self.width = width
       self.x = x
       self.y = y
