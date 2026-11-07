print("Efetuar Pagamento") 
preco = float(input("Digite o valor do produto: ")) 
print("Escolha o número de opção desejado:") 
print("1- À vista em dinheiro - 10% desconto") 
print("2- À vista no cartão de crédito - 5% desconto") 
print("3- Cartão em 3x sem juros") 
print("4- Cartão em 6x com juros + 10% juros") 
opcao = int(input("Digite o número escolhido: ")) 
if opcao == 1: 
x = preco-(preco*10/100) 
print(f"O valor a ser pago é R$ {x:.2f}") 
elif opcao == 2: 
x = preco-(preco*5/100) 
print(f"O valor a ser pago é R$ {x:.2f}") 
elif opcao == 3: 
x = preco/3 
print(f"O valor a ser pago é R$ {x:.2f}") 
else: 
x = preco+(preco*10/100)/6 
print(f"O valor a ser pago é R$ {x:.2f}")