#!/usr/bin/python3

print("<<#Python3 Script to PRINT EVEN Numbers#>>\nInput number in form of 1, 50 (Example).\n")


a = int(input("Start Range Numbers: "))
b = int(input("End Range Numbers: "))

def EvenNum(x, y):
	even = []
	for i in range(x, y + 1):
		if i % 2 == 0:
			even.append(i)
	return even
evenNum = EvenNum(a, b)

print("\nEven Numbers in this Range:\n{}".format(evenNum))
