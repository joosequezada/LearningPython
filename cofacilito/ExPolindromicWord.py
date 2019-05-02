#!/usr/bin/python3

print("<<#Python3 Script to PRINT Palindromic WORD#>>\n")

awords	= [ "malayalam", "strangh", "sun", "noon", "love", "did", "mom", "honey" ]
pwords	= []

for word in awords:
	if word == ''.join(reversed(word)):
		pwords.append(word)

print("All words:\n {}\n".format(awords),"\nPolindromic words: \n{}".format(pwords))