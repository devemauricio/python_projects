class Node():
  def __init__(self, matricula, nome, notas):
    self.matricula = matricula
    self.nome = nome
    self.list_notas = ["Português", "Matemática", "Física", "Biologia", "Gramática"]
    self.notas = {materia: float(nota) for materia in self.list_notas for nota in notas}
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

lista = LinkedList()
lista.append("12345678900", "Maurício Dévé", [10, 2.5, 3.7, 4.5, 10])
lista.append("32260109123", "John Lennon", [7.8, 6.4, 8.8, 7.0, 8.0])
lista.append("19621963196", "Paul McCartney", [0.5, 0.8, 10.0, 5.0, 6.5])
lista.printList()
