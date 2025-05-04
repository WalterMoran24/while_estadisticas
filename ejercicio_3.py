#Mostrar la suma de los números desde el 1 hasta el 10.
#La guia dice hasta del 1 al 10, pero quise plantearlo de otra manera

def suma_hasta(valor):
    "Suma los números del 0 hasta el valor que ingresemos."
    acumulador = 0
    for indice in range(valor + 1): #incluye el ultimo valor
        acumulador += indice
    return acumulador

numero = int(input("Introduce un número hasta donde quieres sumar: "))

resultado = suma_hasta(numero) #variable igualada a la funcion con el input como argumento
print(f"La suma desde 0 hasta {numero} es: {resultado}")
