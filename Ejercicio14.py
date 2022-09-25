import os
numero = 0
listaNumeros = []
Menu = input("¿Que operacion desea realizar?\n 1-Escribir\n 2-Mostrar\n 3-Salir del Programa\n")

if Menu == "1":
    while numero < 101:
        listaNumeros.append(numero)
        numero = numero + 1
    file = open("numeros.txt", "w")
    file.write(str(listaNumeros))
    file.close()

if Menu == "2":
    archivo = open("numeros.txt")
    print (archivo.read())

if Menu == "3":
    print(quit())