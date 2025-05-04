'''Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
Calcular la suma de los números positivos y el producto de los negativos.'''
def producto_suma():

    positivos =  0

    negativos = 1

    opcion = ""

    continuar = "si"

    salida = "no"

    numero = int(input("Ingrese un numero: "))
    if numero >=0:
        positivos += numero
    else:
        negativos += numero


    while opcion != salida:
        opcion = input("Desea continuar? (si / no): ")
        if opcion == continuar:
            numero = int(input("Ingrese un numero: "))
            if numero >=0:
                positivos += numero
            else:
                negativos *= numero
        elif opcion == salida:
            print("Fin del programa.")
            break
        else:
            print("Ingrese una opcion valida.")

    print(f'Numeros positivos: {positivos}')
    print(f'Numeros negativos: {negativos}')


producto_suma()