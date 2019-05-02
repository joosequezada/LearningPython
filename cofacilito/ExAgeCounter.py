#!/usr/bin/python3

"""
Mostrar en pantalla True o False si la edad 
ingresada por dos usuarios es la misma.
"""
print("///Python3 Script - Calcular edad///\n")

userA	= int(input("Edad usuario A: \n"))
userB	= int(input("Edad usuario B: \n"))

print("Los usuarios A y B tienen la misma edad: [%s]" % (userA == userB))