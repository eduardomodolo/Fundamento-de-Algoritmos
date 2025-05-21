#digitar uma sequencia de numeros de 1 até 10
for n in range(1, 11):
    print(n)
    


print("Tabuada")
while True:
    num = int(input("Digite o número: "))
    for n in range(0, 11):
        result = num * n
        print(f"{num} X {n} = {result}")
    opcao = int(input("Digite 1 para fazer outra tabuada ou digite 2 para sair do programa."))
    if opcao == 2:
        break









































while True:
    tabuada = int(input("Digite o valor"))
    for num in range(1, 11):
        result = tabuada * num
        print(result)
        break


