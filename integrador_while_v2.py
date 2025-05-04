'''Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada
la carga determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El número positivo más grande.
El porcentaje de números negativos ingresados, respecto del total de ingresos.
'''

promedio_positivos = 0

positivos = 0

negativos = 0

contador_negativos = 0

contador_positivos = 0

maximo = 0

opcion = ""

opcion_Seguir = "si"

opcion_salir = "no"


numero = int(input("Ingrese un numero: "))
if numero < 0:
    negativos += numero
    contador_negativos += 1
if numero >= 0:
    positivos += numero
    if numero > maximo:
        maximo =numero
    contador_positivos +=1
    while opcion != opcion_salir:
        opcion = input("Quiere ingresar mas numeros? (si / no): ")
        if opcion == opcion_Seguir:
            numero = int(input("Ingrese otro numero: "))
            if numero < 0:
                negativos += numero
                contador_negativos += 1
            if numero >= 0:
                positivos += numero
                contador_positivos +=1
                if numero > maximo:
                    maximo =numero
        elif opcion == opcion_salir:
            print("Nos vemos.")
            break


if contador_positivos > 0: 
    promedio_positivos = positivos / contador_positivos
else:
    promedio_positivos = 0


total_ingresos = contador_negativos + contador_positivos
if total_ingresos > 0:
    porcentaje_negativos = (contador_negativos / total_ingresos) * 100
else:
    porcentaje_negativos = 0


print(f'La suma total de los numeros positivos: {positivos}')
print(f'La suma total de los numeros negativos: {negativos}')
print(f'La cantidad de numeros negativos fue de: {contador_negativos}')
print(f'El promedio de los numeros positivos es de : {promedio_positivos}')
print(f'El mayor de los positivos es el: {maximo}')
print(f'El porcentaje de numeros negativos es: {porcentaje_negativos}%')
