# -*- coding: utf-8 -*-
"""
Model of interactive video game Swim Little Fish Swim

@author: Amanda Sutherland, Ziyu (Selina) Wang

last modified: 10-18-15
"""


import pygame
from pygame.locals import *
from random import randint


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

	def move_monsters(self,speed): 
		#play with bitwise operators

		#size of the screen. should be better defined, since it's currently in two places
		size = [640,480] 
		
		##setting up to make them move
		#create two bytes for monster position. probably not necessary
		# right_byte = [0,0,0,0,0,0,0,0]
		# left_byte = [0,0,0,0,0,0,0,0]
		#choose a random interger within the bounds of those lists
		right_byte = random.randint(0,7)
		left_byte = random.randint(0,7)
		#choosing a starting position for monsters
		monster_start_pose_right = 2**right_byte
		monster_start_pose_left = 2**left_byte

		##start making them move. perhaps should be a second function? will need loop
		#choose to move right or left 
		new_pose = random.randint(-1,1)
		#move the right/left_byte 1 right or left 
		right_byte_updated = right_byte + new_pose
		left_byte_updated = left_byte + new_pose
		#get width of pixels
		size_pixel = size[0]/16
		#monster position on screen 
		monster_pose_right = right_byte_updated*size_pixel
		monster_pose_left = left_byte_updated*size_pixel

	
# 
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
