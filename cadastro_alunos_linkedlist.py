class Node():
  def __init__(self, matricula, nome, notas):
    self.matricula = matricula
    self.nome = nome
    self.list_notas = ["Português", "Matemática", "Física", "Biologia", "Gramática"]
    self.notas = {materia: float(nota) for materia, nota in zip(self.list_notas, notas)}
    self.next = None

class LinkedList():
  def __init__(self, head=None):
    self.head = head
  def append(self, matricula, nome, notas):
    newNode = Node(matricula, nome, notas)
    if self.head:
      current = self.head
      while current.next:
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

  def printList(self):
    if self.head:
      current = self.head
      while current:
        print(f"Matrícula: {current.matricula} - Nome: {current.nome} - Notas: {current.notas}")
        current = current.next

  def append_index(self, matricula, nome, notas, index):
    new_node = Node(matricula, nome, notas)
    if index == 0:
      new_node.next = self.head
      self.heead = new_node
    else:
      current = self.head
      for _ in range(index-1):
        if current.next is not None:
          current = current.next
        else:
          break
      new_node.next = current.next
      current.next = new_node
  def remove_index(self, index):
    if index == 0:
      if self.head is not None:
        self.head = self.head.next
    else:
      current = self.head
      for _ in range(index - 1):
        if current is not None:
          current = current.next
        else:
          break
      if current is not None and current.next is not None:
        current.next = current.next.next


lista = LinkedList()
lista.append("12345678900", "Maurício Dévé", [10, 2.5, 3.7, 4.5, 10])
lista.append("32260109123", "John Lennon", [7.8, 6.4, 8.8, 7.0, 8.0])
lista.append("19621963196", "Paul McCartney", [0.5, 0.8, 10.0, 5.0, 6.5])
lista.append_index("40028922", "User123", [1, 2, 3, 4, 5], 1)
lista.printList()
lista.remove_index(1)
lista.printList()
