#!/usr/bin/python3

print("<<#Python3 Script to PRINT Alphabet position of a WORD#>>\n")

alphat = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
    'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}

inputword = input("Escribir una palabra/frase: ")

def AlphaPosition(word):
	"""Replace each letter of a word for its alphabet position.
	"""
	result = ''
	for r in word.lower():
		result += alphat.get(r, r)	
	return result
	
AP = AlphaPosition(inputword)


print("Posicion en el abecedario: ", AP)