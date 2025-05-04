#Muestra 10 repeticiones de números ascendentes desde el 1 al 10.
def contadora(valor):
    '''La consigna dice 10, pero quise modificarlo para ingresar cualquier valor
    el input pasa a ser el argumento de la funcion.'''
    contador = 0
    while contador < valor:
        contador= contador +1
        print(contador)

numero = int(input("Cuantos numeros queres contar?: "))
mostrar = contadora(numero)
