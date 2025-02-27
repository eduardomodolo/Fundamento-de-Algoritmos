salario= float(input("Digite o valor do seu salário atual: "))
if salario < 1800:
    salario = salario * 1.1
    print("O funcionário tem direito a um aumento de 10%")
    print(f"O novo salário é de {salario:.2f}")
    print("Parábens pelo novo salário")
   


a = int(input("Primeiro valor: "))
b = int(input("Digite o segundo valor: "))
if a > b:
    print("O primeiro valor é maior")
if a < b:
    print("O segundo valor é maior")    
if a == b:
    print("Os dois valores são iguais")



n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))
n4 = float(input("Digite sua quarta nota: "))
média = (n1 + n2 + n3 + n4) / 4
if média>5:
    print("Parábens você foi aprovado")
else:
    print("Infelizmente você não foi aprovado")

