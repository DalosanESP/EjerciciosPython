#Dale la vuelta a la frase
frase = input('Introduce una frase: ')

def reordenar_frase(frase):
    #Aqui lo que se hace es separar las letras y poniendo la primera en la ultima posicion, ya que empiezas separando por el final (e, s, a, r, f) //creo
    return frase[::-1]

print(reordenar_frase(frase))