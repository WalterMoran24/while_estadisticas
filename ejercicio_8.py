#Ingresar 10 números enteros. Determinar el máximo y el mínimo.

def max_min():
    ""
    contador = 1

    mayor = 11

    maximo = float('-inf')
    minimo = float('inf')

    while contador < mayor:
        numero = int(input(f'Ingrese el numero {contador}: '))
        contador += 1
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")

max_min( )