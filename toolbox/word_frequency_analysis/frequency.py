#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
from gutenberg.cleanup import strip_headers
import collections

def get_word_list():
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	textfile = open("pg32325.txt")
	full_text = textfile.read()
	no_punctuation = full_text.translate(None, string.punctuation)
	no_intro = strip_headers(no_punctuation).strip()
	convert_ascii = no_intro.encode("ascii")
	convert_lowercase = string.lower(convert_ascii)
	list_split = convert_lowercase.split()
	return list_split

def get_top_n_words(wordlist, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	word_list = collections.Counter(wordlist).most_common(n)
	print word_list
	return word_list

wordlist = get_word_list()
get_top_n_words(wordlist, 100)