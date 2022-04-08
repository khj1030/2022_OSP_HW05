#!/usr/bin/python

import sys
import re

file = open(sys.argv[1], 'r')
lines = file.readlines()

word_dict = {}
for line in lines:
	for word in line.split():
		word = re.sub(r"[^a-zA-Z0-9]", "", word).lower()
		if word!="":
			count = word_dict.get(word,0)
			word_dict[word] = count + 1


print(word_dict)


file.close()




