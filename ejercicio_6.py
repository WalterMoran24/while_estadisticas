'''Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los
números ingresados y el promedio de los mismos.'''
def pedir_numero():

    acumulador = 0

    contador = 0

    promedio = 0

    OPCION = ""

    OPCION_SALIDA = "no"

    CONTINUAR = "si"

    numero = int(input("Ingrese un numero: "))
    acumulador += numero
    contador +=1

    while OPCION != OPCION_SALIDA:
        OPCION = input("Quiere ingresar otro numero?: ")
        if OPCION == CONTINUAR:
            numero = int(input("Ingrese otro numero: "))
            acumulador += numero
            contador +=1
        elif OPCION == OPCION_SALIDA:
            break
        else:
            print("ingrese una opcion valida")
    promedio = acumulador /contador
    print(f'La suma total es de: {acumulador} y el promedio es de: {promedio}')

    return acumulador


pedir_numero()

