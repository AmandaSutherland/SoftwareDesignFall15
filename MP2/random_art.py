# -*- coding: utf-8 -*-
"""
Random_art.py

@author: amonmillner, adapted from pruvolo work
"""

from random import randint
import Image

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
        #takes the depths -1 so it can start building from the right level? TODO
        a = build_random_function(min_depth-1, max_depth-1)
        b = build_random_function(min_depth-1, max_depth-1)

    #creating the list of functions
    functions = [["prod", a, b],
              ["cos_pi", a],
              ["sin_pi", a],
              ["x"],
              ["y"]]
    print 'functions'

    #choose which function to go with 
    if min_depth > 1:
        i = randint(0,4)
    else:
        i = randint(0,6)

# def build_random_lambda(min_depth, max_depth):
#   """ Same concept as build_random_function. 
#       No need for evaluate_random_function as the lambda does that already. 
#   """
#     prod = lambda a,b: a*b
#     cos_pi = lambda a: cos(a)
#     sin_pi = lambda a: sin(a)

#     functions = [[prod],
#                 [cos_pi],
#                 [sin_pi],
#                 [x],
#                 [y]]

#     # choose function to return, then return it
#     if max_depth == 1:
#       i = randint() TODO


def evaluate_random_function(functions, x, y):
    """ Evaluates the function created in build_random_function.
        Input: 
        Output: the value of the function, given an x and y
    # """
    print 'evaluate'
    if  functions[0] == "x": #if the product of 
      return x
    elif functions[0] == "y":
      return y 
    elif functions[0] == "prod":
        return evaluate_random_function(f[1],x,y) * evaluate_random_function(f[2],x,y)
    elif functions[0] == "cos_pi":
        return cos(pi * evaluate_random_function(f[1],x,y))
    elif functions[0] == "sin_pi":
        return sin(pi * evaluate_random_function(f[1],x,y))
 
# def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
#     """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
#         to the output interval [output_interval_start, output_interval_end].  The mapping
#         is an affine one (i.e. output = input*c + b).
    
#         TODO: please fill out the rest of this docstring
#     """

def draw_function():
    """ Not using remap_interval because I do not need that complexity. 
        draw_function takes no inputs and draws the functions from build_random_function
    """
    # creates RBG palate 
    red = build_random_function(1,3)
    green = build_random_function(2,4)
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
            # define the scale here 
            xscale = (x / (349 / 2.0)) -1
            yscale = (y / (349 / 2.0)) -1
            #go back and call evaluate_random_function with color and scales
            red_scaled_down = evaluate_random_function(red, xscale, yscale)
            green_scaled_down = evaluate_random_function(green, xscale, yscale)
            blue_scaled_down = evaluate_random_function(blue_scaled, xscale, yscale)
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
    im.save(new_image.png)
    im.show()

build_random_function(0,3)