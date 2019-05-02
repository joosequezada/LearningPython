#!/usr/bin/python3

print("<<#Python3 Script to PRINT Sum, Average, Less, Greater#>>\n")

lista = [ 1, 2, 54, 6, 7, 5, 59, 93, 3, 9 ]

def Sum(numbers):
	return sum(numbers)

def Average(numbers):
	return sum(numbers) / len(numbers)

def Greater(numbers):
	return max(numbers)

def Less(numbers):
	return min(numbers)


sxm		= Sum(lista)
avrg	= Average(lista)
mmx 	= Greater(lista)
mmy 	= Less(lista)

print("Numbers list: {}".format(lista),"\n\n\
Sum: [{}]".format(sxm),
"\nAverage: [{}]".format(avrg),
"\nGreater: [{}]".format(mmx),
"\nLess: [{}]".format(mmy))
#print(mean(values))
