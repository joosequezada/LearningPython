#!/usr/bin/python3

print("<<#Python3 Script to PRINT Average's Grades#>>\n")

subjects = { "calculus": 10, "art": 10, "accounting": 9.6, "history": 9.6 }
grades = subjects.values()

def Average(values):
	return sum(values) / len(values)

average = Average(grades)

print("Average's Grades: ", round(average, 2))
#print(mean(values))

