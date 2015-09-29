#!/usr/bin/env python

#Software Design - Fall 2015
#This script will import a Project Gutenberg book and do ____
from pattern.web import*
from pattern.en import parse
import nltk
from nltk import tokenize
from nltk.probability import ConditionalFreqDist
from nltk.tokenize import word_tokenize
import re
import pprint
import networkx as nx 
import matplotlib as mpl 
import matplotlib.pyplot as mplp

def get_book():
# this function downloads the book
	#Peter_Pan_full_text = URL('http://www.gutenberg.org/cache/epub/16/pg16.txt').download()
	textfile = open("Peter_Pan_direct_text.txt")
	Peter_Pan_full_text = textfile.read()
	print'got book!'
	return Peter_Pan_full_text
	
def delete_introduction_ending(full_text):
# this function deletes extranious text from Peter_Pan_full_text
	from gutenberg.cleanup import strip_headers
	no_intro = strip_headers(full_text).strip()
	# print no_intro
	print'headers are gone'
	return no_intro

def find_chapter(stripped_text):
#finds the chapter titles in the book 
	indices = [m.start() for m in re.finditer('Chapter', stripped_text)]
	for i in range(17):
		m = stripped_text[indices[i]:indices[i]+len("Chapter xx")] 
		# print m 

def chapter_split(Peter_Pan_full_text):
# divides the book by chapters so we know where we are
	chapter = Peter_Pan_full_text.split('Chapter')
	print'split into chapters!'
	# print chapter
	# print chapter[1]
	print len(chapter)
	return chapter

	
def parts_of_speech(chapters):
#tags all words (probably bad!) with their parts of speech 
#comes from nltkEnd of the Project Gutenberg EBook
	# for i in range(len(chapters)):

	full_text_parts_speech = word_tokenize(chapters)
	Peter_Pan_parsed_nltk = nltk.pos_tag(full_text_parts_speech)
	print'text tagged!'
	print type(Peter_Pan_parsed_nltk)
	# print len(Peter_Pan_parsed_nltk)
	# print Peter_Pan_parsed_nltk 
	return Peter_Pan_parsed_nltk
	
def find_common_nouns(parsed_text):
# finds the 5 most common nouns in the book and gives them in order of frequency
#most common of three types: NNS, NN, NNP	
	cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in parsed_text
	                                  if tag.startswith('NN'))
	common_nouns = dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())
	# print len(parsed_text)
	print common_nouns
	print 'found common nouns'
	return common_nouns

# def visualization(chapter_list):
# 	text_dict = {chapter_list[i]: chapter_list[i+1] for i in range(0, len(chapter_list))}
# 	graph = nx.Graph(text_dict)
# 	# nx.draw_networkx(graph, cmap)
# 	# mplp.show()
# 	vusual = nx.to_dict_of_dicts(graph)
# 	print visual

Peter_Pan_full_text = get_book()
no_intro = delete_introduction_ending(Peter_Pan_full_text)	
# no_intro_ending = find_delete_ending(no_intro)
chapter_find = find_chapter(no_intro)
# find_chapter_fullname(Peter_Pan_full_text)
split_chapters = chapter_split(no_intro)
POS = parts_of_speech(no_intro)
find_nouns = find_common_nouns(POS)
# visualization(POS)