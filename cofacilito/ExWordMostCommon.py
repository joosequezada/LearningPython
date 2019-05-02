#!/usr/bin/python3

from collections import Counter

print("<<#Python3 Script to PRINT Most popular WORD and how many#>>\n")

with open("chapter1.txt", "r") as f:
	text	= f.read().lower()
	counter   = Counter(text.split()).most_common(1)
	closed	= f.close()
	print("Most common WORD: {} ".format(dict(counter)))