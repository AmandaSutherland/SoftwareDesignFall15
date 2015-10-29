# -*- coding: utf-8 -*-
"""
Model of interactive video game Swim Little Fish Swim

@author: Amanda Sutherland, Ziyu (Selina) Wang

last modified: 10-18-15
"""


import pygame
from pygame.locals import *
from random import randint
import time


class SwimFishModel:

    """ Encodes the game state """
    def __init__(self):
        now = time.time()
        now = time.time()
        self.fish = Fish((209, 95, 238), 60, 50, 200, 450)
        self.leftWall = Wall((205,133,63),480,50,0,0)
        self.rightWall = Wall((205,133,63),480,50,640-64,0)
        self.monsters = []
        self.choices = ['images/octopus1_png.png', 'images/crab1.png', 'images/jellyfish.png', 'images/shark.png', 'images/stingray.png']

class Monster:
    """ Encodes the state of a monster in the game 
    """
    
    def __init__(self,height,width,img,x,y):
        self.height = height
        self.width = width
        self.img = pygame.image.load(img)
        self.scale = pygame.transform.scale(self.img, (int(width), int(height)))
        self.x = x
        self.y = y
        #Adjust the positions of rectangles surrounding the monsters to give a smoother game play experience
        self.rect = pygame.Rect(x+60,y+10,width-15,height-15)
        
    def move_monster(self):
        """This describes how the monsters move, which is then called in swim_little_fish_swim.py.
        """
  
        #size of the screen. should be better defined, since it's currently in two places
        size = [640,480] 

        ##setting up to make them move
        choose_byte = self.x
        ##moving left or right
        #choose to move right or left
        new_pose = randint(-2,2)
        screen_width_sections = 10
        byte_updated = choose_byte + (new_pose*screen_width_sections)
        #monster position on screen (horizontal)
        monster_pose = byte_updated
        self.x = monster_pose 
        #showing monsters' rectangle
        self.rect.x = monster_pose
        ##moving monster down
        screen_height_sections = 60 
        #height of pixels
        height_pixel = size[1]/screen_height_sections 
        self.y = self.y + height_pixel    
        self.rect.y = self.rect.y+height_pixel

class Fish:
    """ Encodes the state of the fish in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,width,height+15)

class Wall:
   """ Encodes the state of the wall in the game """
   def __init__(self,color,height,width,x,y):
       self.color = color
       self.height = height
       self.width = width
       self.x = x
       self.y = y
