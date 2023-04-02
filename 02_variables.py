#Variables:
#Declaración = Definición

nombre = "Pepe"
nombre = "Bruno" #Variable redefinida.
bienvenida = "Hola " + nombre + ", cómo estás?" #Concatenar.

#Definir con camelCase:
nombreCompleto = "Bruno"
#Definir con snake_case: (Recomendada)
nombre_completo = "Bruno"

a = 1
b = 4
b += 1 #Agregar un signo antes del igual modifica el valor previamente definido. (4+1=5)
del b #Con "del" se borra la definición de la variable.
b = 5
c = a*5+b

print(bienvenida)
print(f"Tu edad es {c*3+a*2}.")
#El fString sirve para introducir otros tipo de datos colocados entre llaves {}.

#Operadores de pertenencia: "in" y "not in".
print("Pepe" in bienvenida) #Busca el string en la variable arrojando "True" o "False".
print("bruno" in bienvenida) #El lenguaje es Case Sensitive.
print("Bru" in bienvenida) #Puede buscar cualquier fragmento del string
