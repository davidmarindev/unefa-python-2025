# Funciones
# Ciclos
# Estructuras compuestas

# Funciones

# Partes de una función en python

# 1. Palabra reservada def
# 2. Nombre de la función
# 3. Parámetros de entrada que van entre paréntesis (a,b)
# 4. Dos puntos : - Para indicar que empieza el bloque de código
# 5. Indentación
# 6. Código de la función - Bloque de código
# 7. return - Valor de salida(Si se requiere)
# 8. Llamada a la función

PI = 3.14

def imprimir_linea(n=1):
    """
    Esta función imprime una línea en la consola.
    """
    # match n:
    #     case 1:
    #         print()
    #     case 2:
    #         print()
    #         print()
    #     case 3:
    #         print()
    #         print()
    #         print()
    #     case _:
    #         print("Opción no válida")
      
    for i in range(n):
      print()

def suma(a, b):
    """
    Esta función recibe dos números y retorna la suma de ambos.
    """
    return (a + b) * PI
  
resultado = suma(10, 20)

print("Bienvenido a la calculadora")
imprimir_linea()
print("Resultado de suma", resultado)
imprimir_linea(2)
print("Fin de la calculadora")

# def imprimir_nombre_completo(nombre, apellido):
#     """
#     Esta función imprime el nombre completo.
#     """
#     nombre_completo = nombre + " " + apellido
#     print("Nombre completo:", nombre_completo)

# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")

# imprimir_nombre_completo(nombre, apellido)

# tupla = (10, 20, 30)
# lista = [10, 20, 30]

# lista[2] = 40

# tupla_compuesta = (10, 20, 30, [40, 50])
# print(tupla_compuesta[3][1])

# Ciclos

# For: Itera sobre una secuencia (lista, tupla, diccionario, 
# conjunto o cadena de caracteres)

# while: Ejecuta un bloque de código mientras una 
# condición sea verdadera

# for(i=0; i < 10; i++):

# def fizz_buzz(n):
#   for i in range(1, n + 1):
#     if i % 3 == 0 and i % 5 == 0:
#       print("FizzBuzz")
#     elif i % 3 == 0:
#       print("Fizz")
#     elif i % 5 == 0:
#       print("Buzz")
#     else:
#       print(i)

# fizz_buzz(100)

# def imprimir_linea_nuevo(n=1):
#     """
#     Esta función imprime una línea en la consola.
#     """
#     i = 0
#     while i < n:
#       print()
#       i += 1
      
# Elementos compuestos

# Cadena de caracteres
# Lista
# Tupla
# Diccionario
# Conjunto

cadena = "Universidad"

print(cadena[0]) # U
print(cadena[5])

for letra in cadena:
    print(letra)
    
# Listas 

lista = [10, 20, 30, 40, 50]

length = len(lista)
print("Longitud de la lista", length)

# append
lista.append(60)
print("Lista después de append", lista)

# insert
lista.insert(2, 25)
print("Lista después de insert", lista)

# pop
lista.pop(3)
print("Lista después de pop", lista)

# remove
lista.remove(60)
print("Lista después de remove", lista)

# index
index = lista.index(40)
print("Índice de 40", index)

lista.append(40)
print("Lista después de append", lista)

# count
count = lista.count(40)
print("Cantidad de 40", count)

# sort 

lista.sort()
print("Lista después de sort", lista)

print(type(lista))


# Diccionarios

# Utilizados para almacenar datos en pares clave-valor
# Se definen entre llaves {}
# Se pueden acceder a los valores utilizando la clave
# Se pueden modificar los valores utilizando la clave
# Se pueden eliminar los valores utilizando la clave
# Se pueden agregar nuevos valores utilizando la clave
# Se pueden recorrer utilizando un ciclo for

persona = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 25,
    "estudiante": True,
    "altura": 1.75,
    "direccion": {
        "calle": "Av. Siempre Viva",
        "numero": 742,
        "codigo_postal": 12345
    }
}

print("Keys:", persona.keys())
print("Values:", persona.values())
print("Items:", persona.items())

print("Nombre:", persona["nombre"])
print("Apellido:", persona["apellido"])
print("Edad:", persona["edad"])
print("Estudiante:", persona["estudiante"])
print("Altura:", persona["altura"])
print("Dirección:", persona["direccion"]["calle"], persona["direccion"]["numero"])

productos =[
  { "nombre": "Laptop", "precio": 1000, "cantidad": 5},
  { "nombre": "Celular", "precio": 500, "cantidad": 10},
  { "nombre": "Tablet", "precio": 300, "cantidad": 15},
  { "nombre": "Monitor", "precio": 200, "cantidad": 20},
]

# keys

