# Arreglos: Son estructuras de datos que almacenan elementos del mismo tipo en una secuencia contigua en memoria.
# Se accede a los elementos mediante un índice, que es un número entero que indica la posición del elemento en el arreglo.
# RAM (Acceso aleatorio a memoria) permite acceder a cualquier elemento del arreglo en tiempo constante O(1).
class Array:
    def __init__(self, capacity = 8):
        self.capacity = capacity  # Capacidad inicial del arreglo
        self.size = 0  # Tamaño actual del arreglo (número de elementos)
        self.data = [None] * capacity  # Inicializa el arreglo con un valor None por cada elemento

    # __getitem__ y __setitem__ permiten acceder y modificar los elementos del arreglo usando la sintaxis de corchetes.
    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Índice fuera de rango")

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Índice fuera de rango")
          
    # __str__ permite representar el objeto como una cadena de texto.
    # Esto es útil para imprimir el contenido del arreglo de manera legible.
    def __str__(self):
        return str(self.data)
    # __repr__ devuelve una representación más detallada del objeto, útil para depuración.
    def __repr__(self):
        return f"Array({self.size}) with elements: {self.data}"
      
    def __len__(self):
        return self.size
      
    def is_empty(self):
      if self.size == 0:
        return True
      else:
        return False
    
    def size():
        return self.size
      
    def push(self, value):
        if self.size == self.capacity:
          self.resize()
        self.data[self.size] = value
        self.size += 1
    
    def pop(self):
        if self.is_empty():
          raise IndexError("Array Empty")
        self.data[self.size -1] = None
        self.size -=1

    def resize(self):
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity
        for i in range(self.size):
          new_data[i] = self.data[i]
        self.capacity = new_capacity
        self.data = new_data
    
    def find(self, item):
      if self.is_empty():
        raise IndexError("Array Empty")
      item_index = None
      for i in range(self.size):
        if self.data[i] == item:
          item_index = i
          break
      if item_index == None:
        return -1
      else:
        return item_index
        
      
# Ejemplo de uso

# Este bloque se ejecuta solo si el script se ejecuta directamente, no si se importa como un módulo.
# __name__ es una variable especial que contiene el nombre del módulo actual.
if __name__ == "__main__":
    arr = Array()
    arr.push(1)
    arr.push(2)
    arr.push(3)
    print(arr)  # Imprime el arreglo actual
    print(arr[1])  # Accede al segundo elemento (índice 1)
    
    arr[1] = 5  # Modifica el segundo elemento
    print(arr)  # Imprime el arreglo modificado
    
    print("Size:", len(arr))  # Imprime el tamaño del arreglo
    
    arr.pop()  # Elimina el último elemento
    print(arr)  # Imprime el arreglo después de eliminar un elemento
    
    print("Find 5:", arr.find(5))  # Busca el elemento 5 en el arreglo
    print("Find 10:", arr.find(10))  # Busca un elemento que no está en el arreglo
    
    arr.push(4)
    arr.push(5)
    arr.push(6)
    print(arr)  # Imprime el arreglo después de agregar más elementos
    
    arr.push(7)
    arr.push(8)
    arr.push(9)  # Esto hará que se redimensione el arreglo
    arr.push(10)
    print(arr)  # Imprime el arreglo después de redimensionar