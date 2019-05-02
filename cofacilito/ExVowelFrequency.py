#!/usr/bin/python3

print("<<#Python3 Script to PRINT Vowel Counter#>>\nIt will SHOW \
Frequency of vowels in a word.\n")

input_word  = input("Type a WORD/PHRASE: ")

def VowelCounter(word): 
	vowel = "aeiou" #["a","e","i","o","u"]
	voinword = {}
	for key in word.lower():
		if key in vowel:
			voinword[key] = voinword.get(key, 0) + 1
	return voinword

vowelCounter = VowelCounter(input_word)

print("\nNumber of vowel 'A' in WORD: {}.".format(vowelCounter.get("a")))
print("Number of vowel 'E' in WORD: {}.".format(vowelCounter.get("e")))
print("Number of vowel 'I' in WORD: {}.".format(vowelCounter.get("i")))
print("Number of vowel 'O' in WORD: {}.".format(vowelCounter.get("o")))
print("Number of vowel 'U' in WORD: {}.".format(vowelCounter.get("u")))