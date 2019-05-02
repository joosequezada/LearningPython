#!/usr/bin/python3

print("<<#Python3 Script to PRINT word WITHOUT Vowel#>>\n\
It will SHOW Word you typed but Vowel.\n")

input_word  = input("Type a WORD/PHRASE: ")

def DeleteVowel(word): 
	vowel = "aeiouAEIOU" #["a","e","i","o","u"]
	voinword = []
	for w in word:
		if w not in vowel:
			voinword.append(w)		
	return ("".join(voinword))

deleteVowel = DeleteVowel(input_word)
print("\nThis typed has {} vowel.".format(deleteVowel))
