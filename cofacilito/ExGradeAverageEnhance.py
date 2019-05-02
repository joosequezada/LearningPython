#!/usr/bin/python3

subjects = {}

print("<<#>>Python3 Script to PRINT Average's Grades<<#>>\n\
<<Type retire subjects grade as number 0>>\n")
""" Adding values to variasbles
"""
ca = input("Calculus grade: ") 
ar = input("Art grade: ")
ac = input("Accouting grade: ")
hi = input("History grade: ")
""" Adding values to dictionary
"""

subjects["calculus"] = float(ca)
subjects["art"] = float(ar)
subjects["accounting"] = float(ac)
subjects["history"] = float(hi)
  
grades = subjects.values()

def Average(values):
	return sum(values) / len(values)

average = Average(grades)

print("\nAverage's Grades: [{}]".format(round(average, 2)))
#print(mean(values))