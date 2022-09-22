#Implementa un programa Java que solicite al usuario una cadena de caracteres (String) y muestre por pantalla dicha cadena, pero con el primer y último carácter cambiados de posición.
frase = input('Escriba una frase:' )

def intercambiar(frase):
    #frase -1 se utiliza para sacar el ultimo caracter de la frase
    #frase[1:-1] para partir desde el segundo caracter hasta el ultimo (como si fuera un desde a hasta d) 
    #frase 0 es el primer caracter
    return frase[-1] + frase[1:-1] + frase[0]
    

print (intercambiar(frase))

