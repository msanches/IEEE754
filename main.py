import ieee754
import os
def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

print('Ponto Flutuante - Precisão simples 32 bits')

#Entrada de dados requer um número decimal
while True:
  cls()
  num = float(input('Digite um número decimal: '))
  ieee754.converte(num)
  resp = input('\nDeseja continuar? ') 
  if resp in 'nN': break