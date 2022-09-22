#Escribir 10 numeros y decir cuales de ellos son mayores, menores, o iguales a 0
Ceros = 0
MayoresdeCero = 0
MenoresdeCero = 0
numero = int(input("Escribe un numero "))

for i in range(10) :
    if numero > 0:
        MayoresdeCero = MayoresdeCero + 1
        i = i + 1
    elif numero < 0:
        MenoresdeCero = MenoresdeCero + 1
        i = i + 1
    else:
        Ceros = Ceros + 1
        i = i + 1

    numero = int(input("Escribe un numero "))

print ("Total mayores que cero ", MayoresdeCero)
print ("Total menos que cero ", MenoresdeCero)
print ("Iguales que cero ", Ceros)
    