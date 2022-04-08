#!/usr/bin/python

import sys
import re

file = open(sys.argv[1], 'r')
lines = file.readlines()

word_dict = {}
for line in lines:
	for word in line.split():
		word = re.sub(r"[^a-zA-Z]", "", word).lower()
		if word!="":
			count = word_dict.get(word,0)
			word_dict[word] = count + 1

word_list = word_dict.keys()

rank = 0
for word in word_list:
	if rank == int(sys.argv[2]):
		break
	print(word, word_dict[word])
	rank = rank + 1

file.close()




