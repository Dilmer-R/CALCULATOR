#!/usr/bin/env python3
import time
import sys
import os

def calc():
    print(
    """
    1] ADICIÓN
    2] SUSTRACCIÓN
    3] MULTIPLICACIÓN
    4] DIVISIÓN
    5] POTENCIACIÓN
    6] SALIR
    """)
    op = int(input("Elija una opción: "))

    while op <= 0 or op >= 7:
        op = int(input("Elija una opción: "))
    
    if op == 1:
        print("ADICIÓN")
        a = int(input("Ingrese el primer valor: "))
        b = int(input("Ingrese el segundo valor: "))
        suma = a + b
        print("La suma de {} y {} es: {}".format(a, b, suma))
    elif op == 2:
        print("SUSTRACCIÓN")
        a = int(input("Ingrese el primer valor: "))
        b = int(input("Ingrese el segundo valor: "))
        resta = a - b
        print("La resta de {} y {} es: {}".format(a, b, resta))
    elif op == 3:
        print("MULTIPLICACIÓN")
        a = int(input("Ingrese el primer valor: "))
        b = int(input("Ingrese el segundo valor: "))
        mult = a * b
        print("La multiplicación de {} y {} es: {}".format(a, b, mult))
    elif op == 4:
        print("DIVISIÓN")
        a = int(input("Ingrese el primer valor: "))
        b = int(input("Ingrese el segundo valor: "))
        div = a / b
        print("La división de {} y {} es: {}".format(a, b, div))
    elif op == 5:
        print("POTENCIACIÓN")
        a = int(input("Ingrese el valor de la base: "))
        b = int(input("Ingrese el valor del exponente: "))
        p = a ** b
        print("Al elevar {} al {} es: {}".format(a, b, p))
    else:
        print("GRACIAS")
calc()