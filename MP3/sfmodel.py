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
        for x in range(20,620,150):
            monster = Monster((0,255,0),20,100,x,120)
            self.monsters.append(monster)
        self.fish = Fish((255,255,255),20,100,200,450)

class Monster:
    """ Encodes the state of a monster in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
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

class Walls:
   """ Encodes the state of the walls in the game """
   def __init__(self,color,height,width,x,y):
       self.color = color
       self.height = height
       self.width = width
       self.x = x
       self.y = y
