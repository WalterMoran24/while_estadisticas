'''Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio.
Mostrar la suma y el promedio por pantalla.'''

def sumar_numeros(cantidad):
    
    acumulador = 0
    contador = 0
    promedio = 0

    while contador < cantidad:
        numero = int(input(f"Ingrese el número {contador + 1}: "))
        acumulador += numero
        contador += 1
    promedio = acumulador / contador
    print(f'El promedio de la suma total es: {promedio}')

    return acumulador, promedio

cantidad_numeros = int(input("¿Cuántos números deseas sumar?: "))
resultado = sumar_numeros(cantidad_numeros)
print(f"La suma total de los números ingresados es: {resultado}")