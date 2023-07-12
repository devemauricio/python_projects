class Node():
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    self.next = None

class LinkedList():
  def __init__(self):
    self.head = None
  '''
  APEND
  '''
  def append(self, nome, idade):

    newNode = Node(nome, idade)

    if self.head is None:

    # Se a cabeça da lista estiver com o parâmetro default None,
    # isto é, ela (a lista) estiver vazia, então a cabeça irá
    # receber o novo nó criado, e este nó irá receber por parâmetro
    # next a própria cabeça, por tratar-se de uma lista circular

      self.head = newNode
      newNode.next = self.head

    elif self.head.idade >= newNode.idade:

    # Se o valor do novo nó for menor ou igual ao valor do primeiro nó (que é a cabeça)...
    # O novo nó se torna a nova cabeça e o restante da lista é mantido

      current = self.head
      while current.next != self.head:
        current = current.next
      current.next = newNode
      newNode.next = self.head
      self.head = newNode


    else:
    # Agora se o valor do novo nó for maior do que o valor to primeiro nó...
    # Nesse caso a gente percorre a lista do mesmo jeito, só que dessa vez até encontrar a posição correta onde a idade do current.next é maior ou igual à idade do novo nó.
    # Depois de encontrada essa posição, basta colocar o novo nó em sua devida posição.

      current = self.head
      while current.next != self.head and current.next.idade < newNode.idade:
        current = current.next
      newNode.next = current.next
      current.next = newNode
  '''
  PRINTLIST
  '''
  def printList(self):
    lista = []
    if self.head:
      current = self.head
      while True:
        lista.append([current.nome, current.idade])
        current = current.next
        if current == self.head:
          break
        
    return lista

lista = LinkedList()
lista.append('Marcos', 15)
lista.append('Larissa', 13)
lista.append('Maurício', 21)
lista.append('Humberto', 16)

lista.printList()
