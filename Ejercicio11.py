salarios = ( [700, 900, 1300] , [1000, 950, 1080], [1300, 930, 1200] )
empleados = ('Javier María', 'Antonio Muñoz', 'Isabel Allende')
total = 0  #esta variable almacenara la suma de los salrios

for i in range(len(empleados)): #un bucle que se repetira el mismo numero de veces que la lista empleados sea de larga
    print(empleados[i], "-> ",end="") #el end ="" sirve para que se escriba en la siguiente linea que el proximo print

    for j in range(len(salarios)): #un bucle que se repetira el mismo numero de veces que la lista salarios sea de larga
        total = total + salarios[i][j]#aqui sumamos salarios al total, el valor de total va guardando las cantidades cada vez que cambia la posicion de salarios0

        if j < len(salarios)-1:#aqyi le decimos que si la posicion de salarios no es menor que la ultima
            print(salarios[i][j], " + ",end="")#nos imprima el salario de esa posicion seguido de un +
        else:
             print(salarios[i][j], " = ",end="")#pero que si es la ultima, nos cambie el + por un =
    print ((total))#aqui simplemente imprimimos el total de la suma 
    total = 0 #volvemos a poner el salario a 0 para que no se sumen los salarios anteriores