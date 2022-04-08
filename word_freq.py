#!/usr/bin/python

import sys
import re
import operator

file = open(sys.argv[1], 'r')
lines = file.readlines()

word_dict = {}
for line in lines:
	for word in line.split():
		word = re.sub(r"[^a-zA-Z]", "", word).lower()
		if word!="":
			count = word_dict.get(word,0)
			word_dict[word] = count + 1

sorted_word_dict = dict(sorted(word_dict.items(), key = lambda item: item[1], reverse = True))

word_list = sorted_word_dict.keys()

rank = 0
for word in word_list:
	if rank == int(sys.argv[2]):
		break
	print("{:<7} {:>4}".format(word, sorted_word_dict[word]))
	rank = rank + 1

file.close()




