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
        self.scale = pygame.transform.scale(self.img, (int(width), int(height)))
        self.x = x
        self.y = y
        #Adjust the positions of rectangles surrounding the monsters to give a smoother game play experience
        self.rect = pygame.Rect(x+35,y+20,width-15,height)

    def move_monster(self):
        """This describes how the monsters move, which is then called in swim_little_fish_swim.py.
        """
  
        #size of the screen. should be better defined, since it's currently in two places
        size = [640,480] 
        
        ##code for byte method
        # ##setting up to make them move
        # #choose a random interger within the bounds of those lists
        # choose_byte = random.randint(0,7)
        # #choosing a starting position for monsters
        # monster_start_pose = 2**choose_byte
        # ##moving left or right
        # #choose to move right or left
        # new_pose = random.randint(-1,1)
        # #move the byte 1 right or left 
        # byte_updated = choose_byte + new_pose
        # #get width of pixels
        # width_pixel = size[0]/16
        # #monster position on screen (horizontal)
        # monster_pose = byte_updated*width_pixel
        # # put into the screen 
        # self.x = monster_pose 
        # ##moving monster down
        # #height of pixels
        # height_pixel = size[1]/20 
        # #move monsters down
        # self.y = height_pixel + 1

        ##setting up to make them move
        choose_byte = self.x
        ##moving left or right
        #choose to move right or left
        new_pose = randint(-1,1)
        #how many sections the width should be split into
        screen_width_sections = 10
        #move the byte 1 right or left 
        byte_updated = choose_byte + (new_pose*screen_width_sections)
        #get width of pixels
        # width_pixel = size[0]/16
        #monster position on screen (horizontal)
        monster_pose = byte_updated
        # put into the screen 
        self.x = monster_pose 
        ##moving monster down
        #how many sections the height should be split into
        screen_height_sections = 30 
        #height of pixels
        height_pixel = size[1]/screen_height_sections 
        #move monsters down 10 pixels at a time
        self.y = self.y + height_pixel    

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
