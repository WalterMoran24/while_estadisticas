'''Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y
el promedio de los mismos.'''

contador = 1

suma = 0

maximo =6

promedio = 0

opcion =""

continuar = "si"

salida = "no"

while maximo > contador:
    numero = int(input(f'Ingrese el numero {contador}: '))
    suma += numero
    contador += 1
    if maximo == contador:
        while opcion != salida:
            opcion = input("Quiere ingresar mas numeros? (si / no): ")
            if opcion == continuar:
                numero = int(input(f'Ingrese el numero {contador}: '))
                suma += numero
                contador += 1
            elif opcion == salida:
                print("Fin")
                break
            else:
                print("Error")

total_numeros = contador -1
promedio = suma / total_numeros
print(suma)
print(promedio)