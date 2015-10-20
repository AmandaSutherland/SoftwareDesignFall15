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
            monster = Monster(10,10,'images/octopus1_png.png',10,x,120)
            self.monsters.append(monster)
        for x in range(200,400,310):
            monster = Monster(10,10,'images/crab1.png',10,x,60)
            self.monsters.append(monster)
        self.fish = Fish((209,95,238),60,50,200,450)
        self.leftWall = Wall((205,133,63),480,50,0,0)
        self.rightWall = Wall((205,133,63),480,50,640-64,0)


class Monster:
    """ Encodes the state of a monster in the game """
    # def scaling(self,height,width,factor):
    	# img_scaled = pygame.transform.scale(self.surface_oct1, (int(factor*width), int(factor*height)))

    def __init__(self,height,width,img,factor,x,y):	
        self.img = pygame.image.load(img)
        self.height = height
        self.width = width
        # self.scale = self.scaling(height,width,factor)
        self.scale = pygame.transform.scale(self.img, (int(factor*width), int(factor*height)))
        # self.scale = pygame.transform.scale(surface_oct1, (width, height)) 
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
