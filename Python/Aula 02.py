
#exercício 1#
Altura = float(input("Informe sua altura: "))
Peso = float(72.7 * Altura) - 58
print(f"Seu peso ideal é: {Peso:.2f}")

#exercício 2#
QtdKm = int(input("Informe a quantidade de quilômetros percorridos: "))
QtdDias = int(input("Informe a quantidade de dias no qual o carro foi alugado: "))
Dias = QtdDias * 60
Quil = QtdKm * float(0.15)
Total = Dias + Quil
print(f"O total a pagar pelo indivíduo é: {Total:.2f}")

#execício 3#
Dias = int(input("Informe a quantidade de dias: "))
Horas = int(input("Informe a quantidade de horas: " ))
Minutos = int(input("Informe a quantidade de minutos: " ))
Segundos = int(input("Informe a quantidade de segundos: " ))
Total = Dias * 86400 + Horas * 3600 + Minutos * 60 + Segundos
print(f"O total em segundos é: {Total:.2f}")
#outro jeito de fazer o total#
print(f"O total em segundos é: {Dias * 86400 + Horas * 3600 + Minutos * 60 + Segundos:.2f}")
#e so substituir o total pela conta direto#

#exercicio 4#
Valor_hora =float(input("Digite o valor da hora de trabalho: "))
horas_mes = int(input("Digite o numero de horas trabalhada no mes: "))
Salario_bruto = Valor_hora * horas_mes
IR = 11/100 * Salario_bruto
INSS = 8/100 * Salario_bruto
Sindicato = 5/100 * Salario_bruto
salario_liquido = Salario_bruto - IR - INSS - Sindicato
print(f"+Salario_bruto: R${Salario_bruto:.2f}")
print(f"-IR: R${IR:.2f}")
print(f"-INSS: R${INSS:.2f}")
print(f"-Sindicato: R${Sindicato:.2f}")
print(f"=Salario_liquido: R${salario_liquido:.2f}")