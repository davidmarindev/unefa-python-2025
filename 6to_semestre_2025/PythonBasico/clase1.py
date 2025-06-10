
# Variables en Python

# Declaracion
# Inicializacion
# Uso

a = 10
b = 20

# Tipos de datos

# Datos Basicos

# Entero - int
# Decimal - float
# Texto - str
# Booleano - bool
# Nullo - NoneType

# Datos Compuestos

# Listas - list
# Tuplas - tuple
# Diccionarios - dict
# Conjuntos - set

name = "Juan"
lastname = "Pérez"
age = "25"
is_student = True
height = 1.75

print("Nombre:", name)
print(type(age))
print(type(is_student))
print(type(height))

full_name = name + " " + lastname

# Concatenar
print("Forma 1:", full_name)
print(f"Forma 2,Nombre: {name} {lastname}")

# Operadores

# Asignacion
# Aritmeticos
# Comparacion
# Logicos

# Asignacion

a = 10
b = 20
c = 1
d = 2

c += a + b
c -= a
c *= a
c /= a
c %= a

print(c)

# Aritmeticos

# suma +
# resta -
# multiplicacion *
# division /
# division entera //
# modulo %

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b

print("Division", 7 / 2)
print("Division entera:", 7 // 2)
print("Division entera 2:", 7 // 4)

# Comparacion
# igual ==
# diferente !=
# mayor que >
# menor que <
# mayor o igual que >=
# menor o igual que <=

print("Comparacion")

print("a == b", a == b) 
print("a != b", a != b)
print("a > b", a > b)
print("a < b", a < b)
print("a >= b", a >= b)
print("a <= b", a <= b)

n = 10
print("Es o no par?", n % 2 == 0)

# Logicos

# and
# or
# not

a = 10
b = 20
c = 1
d = 2

op1 = a > b and c > d
op2 = a < b or c < d
op3 = a < b or c > d
op4 = a > b or c < d
op5 = not (a < b and c > d)

print("op1", op1)
print("op2", op2)
print("op3", op3)
print("op4", op4)
print("op5", op5)

# Condicionales

if a > b:
  print("a es mayor que b")
else:
  print("a es menor que b")
  
nombre_persona = "Juan"
edad_persona = 55
sexo_persona = "M"

if edad_persona >= 55 and sexo_persona == "F":
  print("Puede jubilarse")
elif edad_persona >= 60 and sexo_persona == "M": 
  print("Puede jubilarse")
else:
  print("No puede jubilarse")
  
  
print(100 * 0.10)

product_name = "Ps5"
product_price = 500
descount = 0

if product_price >= 100 and product_price < 500:
  descount = 0.10
elif product_price >= 500 and product_price < 1000:
  descount = 0.15
elif product_price >= 1000:
  descount = 0.20
else: 
  print("No hay descuento")
  
total_price = product_price - (product_price * descount)  

print("El precio total es:", total_price, "para el producto:", product_name)

nombre = input("Ingrese su nombre: ")

print("Hola", nombre)

edad = int(input("Ingrese su edad: "))
print("Su edad es:", type(edad))