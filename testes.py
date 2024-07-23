#Ian Lucca Soares Mesquita - 211045140
#João Pedro Nóbrega Fernandes - 211029361


import math
import numpy as np

x, y = 0, 0


def mdc_recursivo(a, b):
    global x, y

    if (b == 0):
        x = 1
        y = 0
        return a

    else:
        g = mdc_recursivo(b, a % b)
        x1, y1 = x, y
        x = y1
        y = x1 - math.floor(a / b) * y1
        return g


def print_solucao(a, b, c):
    if (a == 0 and b == 0):

        if (c == 0):
            print("Existem infinitas soluçoes")

        else:
            print("Não existem soluções para o problema")
    mdc = mdc_recursivo(a, b)

    if (c % mdc != 0):
        print("Não existem soluções para o problema")
    else:

        print("x =", int(x * (c / mdc)), ", y =", int(y * (c / mdc)))
        print("Proximos valores:\n")
        
        for i in range(1, 10):
            print("x =", int((x * (c / mdc))+i*(b/mdc)), ", y =", int((y * (c / mdc))-i*(a/mdc)))


#Coeficientes da equação 
a = int(input("digite um valor para a :"))
b = int(input("digite um valor para b :"))
c = int(input("digite um valor para c :"))

# Exibe resultados e os dez próximos valores para x e y 
print(a, b, c)
print_solucao(a, b, c)



