def anula(lista):
  i = len(lista) - 1
  
  while i > 0:
    if len(lista) != 1:
        if lista[i] + lista[i-1] == 0:
          lista.pop(i)
          lista.pop(i-1)      
    i -= 1
  print lista

while 1:
  anula(map(int, raw_input().split()))