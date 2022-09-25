archivo = open("Ejercicio15.txt")
texto = archivo.readlines()
for i in range(len(texto)):
    limpio = texto[i]
    sinEspacios = limpio.replace(" ","")
    print(sinEspacios)