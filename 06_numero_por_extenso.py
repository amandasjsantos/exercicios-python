num = int(input("Digite um número de 1 a 5: ")) 
lista = ["Um","Dois","Três","Quatro","Cinco"] 
if num >= 1 and num <= 5: 
  print(lista[num-1]) 
else: 
  print("Número inválido.")