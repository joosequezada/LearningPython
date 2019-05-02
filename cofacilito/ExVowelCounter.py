#!/usr/bin/python3

print("<<#Python3 Script to PRINT Vowel Counter#>>\nIt will Count vowel you typed.\n")

input_word  = input("Type a WORD/PHRASE: ")

def VowelCounter(word): 
	vowel = "aeiouAEIOU" #["a","e","i","o","u"]
	voinword = []
	for w in word:
		if w in vowel:
			voinword.append(w)
	return len(voinword)

vowelCounter = VowelCounter(input_word)
print("\nThis typed has {} vowel.".format(vowelCounter))
