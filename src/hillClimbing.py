# Funcion f(x)= 2x^2*cos(x)-5x
# f'(x)= 2(2x*cos(x)-x^2*sen(x))-5
import math
import random

def f(value):
    return ((2*value)**2)*(math.cos(value)-(5*value))

def hillClimbing():
    num = random.uniform(-5, 5)
    actual = num
    print("Initial value: ", actual)
    valor = f(actual)
    print("f(value): ", valor)
    cont = 0
    while True:
        v_izq = actual-0.01
        v_der = actual+0.01
        if f(v_izq) < valor and f(v_der) < valor:
            break
        elif f(v_izq) > valor:
            actual = v_izq
            valor = f(v_izq)
        elif f(v_der) > valor:
            actual = v_der
            valor = f(v_der)
        print("Iteration: ", cont)
        print("Actual Value: ", actual)
        print("f(value): ", actual)
        print("\n")
        cont += 1
        
    print("Final value: ", actual)
    print( "f(value): ", valor)

if __name__ == "__main__":
    hillClimbing()