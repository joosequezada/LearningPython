#!/usr/bin/python3

print("<<#Python3 Script to PRINT Best Grade#>>\n")

subjects = { "calculus": 10, "art": 10, "accounting": 9.6, "history": 9.6 }

def BestGrade(values):
	return max(zip(subjects.values(), subjects.keys()))

bestgrd = BestGrade(subjects)

print("Best grade and subjects: {}".format(bestgrd))
#print(mean(values))

