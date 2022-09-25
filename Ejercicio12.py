cuenta = {
    "titular":"", 
    "cantidad":0,
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
    cuenta["cantidad"] = cuenta["cantidad"] + int(input(("Escriba la cantidad que desea Ingresar: ")))
    print(cuenta["cantidad"])
elif datos == "2":
    cuenta["cantidad"] = cuenta["cantidad"] - int(input(("Escriba la cantidad que desea Retirar: ")))
    if cuenta["cantidad"] > 0:
        print(cuenta["cantidad"])
    if cuenta["cantidad"] <= 0:
         cuenta["cantidad"] = 0
         print(cuenta["cantidad"])
    
