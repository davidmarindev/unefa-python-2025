# Lista enlazada simple

# Las listas enlazadas son una estructura de datos que permite almacenar elementos de manera dinámica.
# Cada elemento de la lista se llama nodo, y cada nodo contiene un valor y una referencia al siguiente nodo en la lista.
# En una lista enlazada simple, cada nodo apunta solo al siguiente nodo, formando una cadena de nodos.

# head es el primer nodo de la lista, tail es el último nodo y size es el número de nodos en la lista.
# tail es útil para acceder rápidamente al último nodo, y size permite conocer cuántos elementos hay en la lista.

class ListNode:

  def __init__(self, item):
    self.item = item
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def empty(self):
    if self.head == None:
      return True
    else:
      return False

  def show(self):
    tmp = self.head
    stop = False
    while (stop == False):
      print(tmp.item)
      if tmp.next == None:
        stop = True
      tmp = tmp.next

  def push_front(self, item):
    new_node = ListNode(item)
    if self.empty():
      self.tail = new_node
    old_head = self.head
    self.head = new_node
    self.head.next = old_head
    self.size += 1

  def pop_front(self):
    if self.empty():
      print("The list is empty")
    elif self.size == 1:
      self.head = None
      self.size = 0
    else:
      self.head = self.head.next
      self.size -= 1

  def push_back(self):
    new_node = ListNode(item)
    if self.empty():
      self.head = new_node
    else:
      tmp = self.head
      while (tmp.next != None):
        tmp = tmp.next
      tmp.next = new_node
      self.tail = tmp.next
    self.size += 1

  def pop_back(self):
    if self.empty():
      print("The list is empty")
    elif self.size == 1:
      self.head = None
      self.size = 0
    else:
      tmp = self.head
      while (tmp.next.next != None):
        tmp = tmp.next
      tmp.next = None
      self.tail = tmp
      self.size -= 1
      
  def show_all(self):
    current = self.head
    while current is not None:
      print(current.item, end=' ') # Print el nodo, end=' ' para no saltar de línea
      current = current.next
    print()

  def front(self):
    return self.head.item

  def back(self):
    return self.tail.item

  def insert(self, index, item):
    if index < 0 and index > self.size:
      raise "The index is out of the list range"

    if index == 0:
      push_front(item)
    elif index == self.size:
      push_back(item)
    else:
      new_node = ListNode(item)
      current = self.head
      for _ in range(index - 1):
        current = current.next
      new_node.next = current.next
      current.next = new_node


list = LinkedList()
print(list.empty())
print(list.size)
list.push_front(10)
list.push_front(20)
list.push_front(30)
print(list.size)
print(list.pop_back())
print(list.show())
print(list.front())
print(list.tail.item)
print(list.show_all())
