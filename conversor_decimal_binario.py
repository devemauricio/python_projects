
class Pilha ():
  def __init__(self, number):
    self.lista = []
    self.number = number
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

  def converter(self):
    numero = self.number
    binario = ""
    while numero >= 2:
      
      num = numero % 2
      self.push(num)
      numero = numero // 2
    self.push(numero)
    while not self.is_empty():
      binario += str(self.pop())
    return binario
      
