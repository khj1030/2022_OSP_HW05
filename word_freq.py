#!/usr/bin/python

import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

for line in lines:
	print(line)


file.close()




