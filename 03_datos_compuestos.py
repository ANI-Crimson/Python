#Matrices: Conjunto de datos ordenados como índices (0, 1, 2, 3, etc.)

#Lista (List): Se pueden modificar los elementos.
lista = ["Bruno", "Jorge", True, 1.70]

#Tupla (Tuple): No se pueden modificar los elementos.
tupla = ("Bruno", "Jorge", True, 1.70) #Se define con () pero se muestra con [].

#Conjunto (Set): No se pueden modificar los elementos. Datos desordenados. No se accede por índice. No almacena duplicados.
conjunto = {"Bruno", "Jorge", True, 1.70}

#Diccionario (Dict): Se accede por texto ingresado y no por índice. (clave:valor,)
diccionario = {
    'Nombre': "Bruno",
    'Nombre Falso': "Jorge",
    'Está practicando?': True,
    'Altura': 1.70
}

#--------------------------------------------------------------------------------------
#Ejemplos:

print(lista[1]) #Arroja "Jorge".
print(tupla[1]) #Arroja "Jorge".

lista[1] = "Pepe" #Cambia "Jorge" por "Pepe".
print(lista[1]) #Arroja "Pepe".
print(diccionario['Altura']) #Arroja "1.7"

#tupla[1] = "Pepe" #Ésto no es válido. Arroja error.
#print(conjunto[3]) #No puede acceder al elemento. Arroja Error.
