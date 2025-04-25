# Programación Orientada a Objetos

# Clase
# Metodos
# Atributos
# Constructor
# Objeto

class Producto:
  def __init__(self, nombre, precio, stock=0):
    self.nombre = nombre
    self.precio = precio
    self.__stock = stock
    
  def mostrar(self):
    print(f"Nombre: {self.nombre}")
    print(f"Precio: {self.precio}")
    print(f"Stock: {self.__stock}")
    print("--------------")
  
  def agregar_stock(self, cantidad):
    self.__stock += cantidad
    print(f"Se han agregado {cantidad} unidades al stock de {self.nombre}.")
  
  def venta(self, cantidad):
    if self.__stock >= cantidad:
      self.__stock -= cantidad
      print(f"Se han vendido {cantidad} unidades de {self.nombre}.")
    else:
      print(f"No hay suficiente stock de {self.nombre}. Solo quedan {self.__stock} unidades.")
  
producto1 = Producto("Laptop", 1500, 10)
producto2 = Producto("Celular", 800, 5)
producto3 = Producto("Tablet", 600, 0)

producto3.agregar_stock(20)
producto2.venta(3)
producto1.venta(12)

productos = [producto1, producto2, producto3]
for producto in productos:
  producto.mostrar()
  
producto2.__stock = 10
producto2.mostrar()
  
# Tipo de dato

print(type(producto1))

# Pilares Fundamentales de la POO

# 1. Abstracción
# 2. Encapsulamiento
# 3. Herencia
# 4. Polimorfismo

cuentas_bancarias = []

# Encapsulamiento
# El encapsulamiento es el proceso de ocultar los detalles internos de una clase y exponer solo lo necesario.

class CuentaBancaria():
  def __init__(self, titular, numero, saldo=0):
    self.titular = titular
    self.numero = numero
    self.__saldo = saldo
    
  def mostrar(self):
    print(f"Titular: {self.titular}")
    print(f"Numero: {self.numero}")
    print(f"Saldo: {self.__saldo}")
    print("--------------")
    
  def __agregar_saldo(self, cantidad):
    self.__saldo += cantidad
    print(f"Se han agregado {cantidad} a la cuenta {self.numero}.")
  
  def transferencia(self, cuenta_destino, cantidad):
    if self.__saldo >= cantidad:
      self.__saldo -= cantidad
      cuenta_destino.__agregar_saldo(cantidad)
      print(f"Se han transferido {cantidad} a la cuenta {cuenta_destino.numero}.")
    else:
      print(f"No hay suficiente saldo en la cuenta {self.numero}. Solo quedan {self.__saldo}.")
      
cuenta1 = CuentaBancaria("Juan", 123456, 1000)
cuenta2 = CuentaBancaria("Maria", 654321, 500)

cuenta1.transferencia(cuenta2, 200)

# cuenta2.__agregar_saldo(100)
      
cuenta1.mostrar()
cuenta2.mostrar()

# Herencia
# La herencia es el proceso de crear una nueva clase a 
# partir de una clase existente, heredando sus atributos y métodos.

class Animal:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    
  def hablar(self):
    print(f"{self.nombre} hace un sonido.")
    
  def moverse(self):
    print(f"{self.nombre} se mueve.")

class Perro(Animal):
  def __init__(self, nombre, edad, raza):
    super().__init__(nombre, edad)
    self.raza = raza
  
  def hablar(self):
    print(f"{self.nombre} ladra.")
    
  def moverse(self):
    print(f"{self.nombre} corre.")
    
class Gato(Animal):
  def __init__(self, nombre, edad, color):
    super().__init__(nombre, edad)
    self.color = color
  
  def hablar(self):
    print(f"{self.nombre} maulla.")
    
  def moverse(self):
    print(f"{self.nombre} salta.")
    
  def caer_de_pie(self):
    print(f"{self.nombre} cae de pie.")
    
class Pajaro(Animal):
  def __init__(self, nombre, edad, especie):
    super().__init__(nombre, edad)
    self.especie = especie
  
  def hablar(self):
    print(f"{self.nombre} canta.")
    
  # def moverse(self):
  #   print(f"{self.nombre} vuela.")
    
perro1 = Perro("Firulais", 3, "Labrador")
perro2 = Perro("Rex", 5, "Pastor Aleman")
gato1 = Gato("Miau", 2, "Blanco")
gato2 = Gato("Gato", 4, "Azul")
pajaro1 = Pajaro("Pajaro", 1, "Canario")
pajaro2 = Pajaro("Pajaro", 2, "Loro")

print("Perroooo", type(perro1))

animales = [perro1, perro2, gato1, gato2, pajaro1, pajaro2]

for animal in animales:
  animal.hablar()
  animal.moverse()
  if isinstance(animal, Gato):
    animal.caer_de_pie()
  print("--------------")

print(Animal.__subclasses__())
print(Perro.__bases__)