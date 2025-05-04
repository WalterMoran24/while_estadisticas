'''Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los
números ingresados y el promedio de los mismos.'''


contador = 1

suma = 0

maximo =11

minimo = 6

promedio = 0

opcion =""

continuar = "si"

salida = "no"

while minimo > contador:
    numero = int(input(f'Ingrese el numero {contador}: '))
    suma += numero
    contador += 1
    if minimo == contador:
        while opcion != salida:
            opcion = input("Quiere ingresar mas numeros? (si / no): ")
            if opcion == continuar:
                numero = int(input(f'Ingrese el numero {contador}: '))
                suma += numero
                contador += 1
                if contador == maximo:
                    print("Limite alcanzado.")
                    break
            elif opcion == salida:
                print("Fin")
                break
            else:
                print("Error")

total_numeros = contador -1
promedio = suma / total_numeros
print(f'La suma total de los numeros es: {suma}')
print(f'El promedio de la suma es: {promedio}')