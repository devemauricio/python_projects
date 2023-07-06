
class Pilha ():
  def __init__(self, lista=[]):
    self.lista = lista
  def pop(self):
    if not self.is_empty():
      return self.lista.pop()

  def push(self, char):
    self.lista.append(char)
    return self.lista
  def top(self):
    if not self.is_empty():
      return self.lista[len(self.lista - 1)]

  def seek(self):
    if not self.is_empty():
      return self.lista[0]

  def is_empty(self):
    return True if len(self.lista) == 0 else False

  def lenght(self):
    return len(self.lista)

  def pegar_pilha(self):
    return self.lista

  def inverter(self):
    nova_pilha = Pilha()
    for i in range(self.lenght()):
      nova_pilha.push(self.pop())
    self = nova_pilha
    del nova_pilha
    return self.lista
