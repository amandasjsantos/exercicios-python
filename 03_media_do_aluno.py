nome = input("Digite o nome do aluno: ") 
nota1 = float(input("Digite a primeira nota: ")) 
nota2 = float(input("Digite a segunda nota: ")) 
nota3 = float(input("Digite a terceira nota: ")) 
media = (nota1 + nota2 + nota3)/3 
if media >= 7: 
  print(f"A média do aluno {nome} foi de {media:.2f}, ou seja, ele está 
aprovado!") 
elif media <= 5: 
  print(f"A média do aluno {nome} foi de {media:.2f}, ou seja, ele está 
reprovado!") 
else: 
  print(f"A média do aluno {nome} foi de {media:.2f}, ou seja, ele está de 
recuperação!")