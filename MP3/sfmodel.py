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
            monster = Monster(100,100,'images/octopus1_png.png',x,120)
            self.monsters.append(monster)
        for x in range(200,400,310):
            monster = Monster(100,100,'images/crab1.png',x,60)
            self.monsters.append(monster)
        self.fish = Fish((209,95,238),60,50,200,450)
        self.leftWall = Wall((205,133,63),480,50,0,0)
        self.rightWall = Wall((205,133,63),480,50,640-64,0)

        # for monster in self.monsters:
        #     if self.fish.rect.colliderect(monster.rect):
        #         raise SystemExit, "You lose!"

class Monster:
    """ Encodes the state of a monster in the game """
    # def scaling(self,height,width,factor):
    	# img_scaled = pygame.transform.scale(self.surface_oct1, (int(factor*width), int(factor*height)))

    def __init__(self,height,width,img,x,y):
        self.height = height
        self.width = width
        self.img = pygame.image.load(img)
        # self.scale = self.scaling(height,width,factor)
        self.scale = pygame.transform.scale(self.img, (int(width), int(height)))
        # self.scale = pygame.transform.scale(surface_oct1, (width, height)) 
        self.x = x
        self.y = y
        #Adjust the positions of rectangles surrounding the monsters to give a smoother game play experience
        self.rect = pygame.Rect(x+35,y+20,width-15,height)


class Fish:
    """ Encodes the state of the fish in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x+20,y+20,width,height)
        

class Wall:
   """ Encodes the state of the wall in the game """
   def __init__(self,color,height,width,x,y):
       self.color = color
       self.height = height
       self.width = width
       self.x = x
       self.y = y
