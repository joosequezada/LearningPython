#!/usr/bin/python3

"""
Dado de los valores ingresados por el usuario 
(base, altura) calcular y 
mostrar en pantalla el área de un triángulo.
"""
print("///Python3 Script - Calcular área de triángulo///\n")

base_triang		= int(input("Escribir base de triángulo: \n"))
altura_triang	= int(input("Escribir altura de triángulo: \n"))
area_triang		= base_triang * altura_triang / 2


print("Área: ", area_triang)
