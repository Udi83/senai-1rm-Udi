valor = int(input('Entre com um número para saber o fatorial:'))  
fatorial = 1  
for count in range (1,valor+1):  
  fatorial = fatorial * count
  
print('O fatorial é {}.'.format(fatorial))