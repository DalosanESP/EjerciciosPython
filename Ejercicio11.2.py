salarios = ( [700, 900, 1300] , [1000, 950, 1080], [1300, 930, 1200] )
empleados = ('Javier María', 'Antonio Muñoz', 'Isabel Allende')
nombre = '' #creamos la variable nombre que almacenara el nombre de los empleados
salario= 0  #esta variable almacenara los salarios
dinero = '' #intentar con un print
for i in range(len(empleados)): #este bucle tendra la longitud de la lista de empleados
    nombre = empleados[i] #aqui guardamos el primer nombre, que ira avanzando cada vez que el bucle se repita
    for j in range(len(salarios)): #este bucle tendra la longitud de salarios
        dinero = salarios[i][j]
        salario = salario + salarios[i][j] #aqui utiliza el valor de la posicion del nombre y una nueva variable j que avanzara la 
                                        #longitud de los salarios, luego el bucle se repetira y cambiara el valor de i
        
    print(f"{nombre} {dinero} {salario}")
    salario = 0 #volvemos a poner el salario a 0 para que no se sumen los salarios anteriores
        
