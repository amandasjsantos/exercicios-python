num = int(input("Digite o número do mês: ")) 
meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto", 
"Setembro","Outubro","Novembro","Dezembro"] 
if 1 <= num <= 12: 
  print(meses[num-1]) 
else: 
  print("O mês é inválido.")