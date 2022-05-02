def converte(num):
  #O sinal será representado por 0 se positivo 1 se negativo
  sinal = 0 if num > 0 else 1
  
  #Se o número é negativo, pego o módulo
  num = num if num > 0 else num * -1
  temp = num
  expoente = 0
  
  #Temp é um número parecido com 1,### x 2###
  if num > 1:
    while num != 1:
      temp = temp/2
      num = num//2
      expoente +=1
  else:
    while num < 1:
      temp = temp*2
      num = temp
      expoente -=1
      
  #Cálculo da mantissa baseado na parte fracionária
  temp = temp - 1
  mantissa= ''
  if temp < 0:
    while temp != 1:
      temp = temp * 2
      if temp > 1: 
        temp = temp - 1
        mantissa = mantissa + str(1)
      elif temp == 1: mantissa = mantissa + str(1)
      else: mantissa = mantissa + str(0)

  #Expoente polarizado x = e + 127
  expoente = '{0:08b}'.format(expoente+127)
  
  #Completa a mantissa com 23 bits
  while len(mantissa) < 23:
    mantissa = mantissa + str(0)
  
  #Imprime o número no formato IEEE 754
  iee = str(sinal) + ' ' + str(expoente) + ' ' + str(mantissa)
  print('\nPadrão IEEE754:', iee)
  #print(sinal, expoente, mantissa)
