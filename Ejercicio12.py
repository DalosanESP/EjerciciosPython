cuenta = {
    "titular":"", 
    "cantidad":"",
}

while cuenta["titular"] == "":
    cuenta["titular"] = input("Ingrese un titular: ")
    if cuenta["titular"] == "":
        cuenta["titular"] = input()
        while cuenta["titular"] == "":
            cuenta["titular"] = input("Por favor, ingrese un titular: ")

print("Escriba la cantidad que desea Ingresar: ")
cuenta["cantidad"] = int(input())
datos = input("¿Que operacion desea realizar?\n 1-Ingresar Dinero\n 2-Extraer Dinero\n")
if datos == "1":
    cuenta["cantidad"] = cuenta.get("cantidad") + int(input(("Escriba la cantidad que desea Ingresar: ")))
    print(cuenta["cantidad"])
else:
    print(cuenta["titular"])
    
