cuenta = {
    "titular": 0, 
    "cantidad":0
}

while cuenta["titular"] == 0:
    cuenta["titular"] = input("Ingrese un titular: ")
    if cuenta["titular"] == "":
        cuenta["titular"] = input("Por favor, ingrese un titular: ")
        while cuenta["titular"] == "":
            cuenta["titular"] = input("Por favor, ingrese un titular: ")

print("Escriba la cantidad que desea Ingresar: ")
cuenta["cantidad"] = input()
datos = input("¿Que operacion desea realizar?\n 1-Ingresar Dinero\n 2-Extraer Dinero\n")
if datos == 1:
    cuenta["cantidad"] = cuenta["cantidad"] + input ("Escriba la cantidad que desea Ingresar: ") 
    CUENTA = cuenta["cantidad"]
    print(CUENTA)
else:
   print(0)
    
