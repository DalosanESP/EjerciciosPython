#Generar un numero random e intentar adivinarlo
import random

numero = random.randint(0,20)
numeroUsuario = int(input("Escribe un numero "))
intentos = 1


if numeroUsuario == numero :
    print ('HAS ACERTADO !!!')
    print ('Numero de intentos ', intentos)
    
while numeroUsuario != numero :
    if numeroUsuario > numero :
        print ("Prueba un numero mas bajo")
        intentos = intentos + 1
    elif numeroUsuario < numero :
        print ("Prueba un numero mas Alto")
        intentos = intentos + 1
    else:
        intentos = intentos + 1
        break

    numeroUsuario = int(input("Escribe un numero "))


print ('HAS ACERTADO !!!')
print ('Numero de intentos ', intentos)