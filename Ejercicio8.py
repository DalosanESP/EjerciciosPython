numero = int(input('Escribe 5 numeros: '))
tabla = []

for i in range (5) :
    #append se utiliza para añadir un elemento a una tabla
    tabla.append(numero)
    numero = int(input('Escribe 5 numeros: '))
Suma = sum(tabla)
print (f"Suma de la lista = ", Suma)
