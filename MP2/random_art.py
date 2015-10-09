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
    a = no_input[randint(0,2)] #
    b = no_input[randint(0,2)]

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

  #choose which function to go with 
  if min_depth > 1:
    i = randint(0,2)
  else:
    i = randint(0,4)

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


def evaluate_random_function(f, x, y):
    """ Evaluates the function created in build_random_function.
    """
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """
    # your code goes here

  #how should I make build_random_function go through three times, once for each color?
  #creates blank image with a given length and width of pixels
  from PIL import Image
  length = 350 
  width = 350
  image = Image.new("RGB",(length,width))
    


#your additional code and functions go here
