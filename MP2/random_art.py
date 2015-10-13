# -*- coding: utf-8 -*-
"""
Random_art.py

@author: asutherland, adapted from amonmillner and pruvolo work
"""

from random import randint
import Image
import math
from math import sin, cos, pi

def build_random_function(min_depth, max_depth):
    """ Recursion!
        Creates a string that represents a function comprised of simple functions.
    """
    # Describe the depths of functions
    # Determines the case where a random function should not be built
    if max_depth == 1:
        # list of input strings
        no_input = [["x"], ["y"]] 
        
        # describes function inputs a and b
        # randint(0,2) gives you an interger from 0 to 2
        a = no_input[randint(0,1)] 
        b = no_input[randint(0,1)]

    # Determines the case in which to create a random function 
    else:
        #desribes function inputs a and b
        a = build_random_function(min_depth-1, max_depth-1)
        b = build_random_function(min_depth-1, max_depth-1)

    #creating the list of functions
    functions = [["x"],
                ["y"],
                ["prod", a, b],
                ["cos_pi", a],
                ["sin_pi", a],
                ["square", a],
                ["cube", a]]
       
    #choose which function to go with 
    if min_depth > 1:
        i = randint(1,3)
    else:
        i = randint(0,6)
    return functions[i]

def evaluate_random_function(functions, x, y):
    """ Evaluates the function created in build_random_function.
        Input: 
        Output: the value of the function, given an x and y
    # """
    if  functions[0] == "x": 
        return x
    elif functions[0] == "y":
        return y 
    elif functions[0] == "prod":
        return evaluate_random_function(functions[1],x,y) * evaluate_random_function(functions[2],x,y)
    elif functions[0] == "cos_pi":
        return cos(pi * evaluate_random_function(functions[1],x,y))
    elif functions[0] == "sin_pi":
        return sin(pi * evaluate_random_function(functions[1],x,y))
    elif functions[0] == "square":
        return math.pow(evaluate_random_function(functions[1],x,y) , 2)
    elif functions[0] == "cube":
        return math.pow(evaluate_random_function(functions[1],x,y) ,3)


def draw_function(image_name):
    """ Not using remap_interval because I do not need that complexity. 
        draw_function takes no inputs and draws the functions from build_random_function
    """
    # creates RBG palate 
    red = build_random_function(1,3)
    green = build_random_function(2,8)
    blue = build_random_function(3,5)

    #setting up image
    from PIL import Image
    length = 350
    width = 350 
    im = Image.new("RGB",(length,width))
    pixels = im.load()

    #go through and color ALL THE PIXELS (0- 349)
    for x in range(0,349):
        for y in range(0,349):
            # define the scale here (-1 to 1)
            xscale_down = (2*x / 349.0) -1 
            yscale_down = (2*y / 349.0) -1 

            #go back and call evaluate_random_function with color and scales
            red_scaled_down = evaluate_random_function(red, xscale_down, yscale_down)
            green_scaled_down = evaluate_random_function(green, xscale_down, yscale_down)
            blue_scaled_down = evaluate_random_function(blue, xscale_down, yscale_down)
            
            #scale back up again (reverse from xscale and yscale)
            red_rescaled = ((red_scaled_down +1) * 349) / 2.0
            green_rescaled = ((green_scaled_down +1) * 349) / 2.0
            blue_rescaled = ((blue_scaled_down +1) * 349) / 2.0
            
            #changing to interger from float so it can be plotted
            r = int(red_rescaled)
            g = int(green_rescaled)
            b = int(blue_rescaled)
            #creating the pixels
            pixels[x,y] = (r,g,b)

    #plotting time! image saved and shown
    im.save(image_name)
    im.show()

if __name__ == '__main__':
    # build_random_function(0,3)
    # evaluate_random_function(f,a,b)
    draw_function("figure12.png")