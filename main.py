import ieee754
print('Ponto Flutuante - Precisão simples 32 bits')

#Entrada de dados requer um número decimal
while True:
  num = float(input('\nDigite um número decimal: '))
  ieee754.converte(num)
  resp = input('\nDeseja continuar? ') 
  if resp in 'nN': break