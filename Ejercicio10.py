#Sacar el elemento con mayor y menor longitud de la tabla
lista = ['Anakin', 'Vader', 'Maul', 'R2']
#aqui usamos max o min para saber el valor maximo y el minimo de la tabla usando como referencia la lungitud
print(max(lista, key=len))
print(min(lista, key=len))
