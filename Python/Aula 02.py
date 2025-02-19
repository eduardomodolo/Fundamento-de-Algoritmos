"""exercício 1"""
Altura = float(input("Informe sua altura: "))
Peso = float(72.7 * Altura) - 58
print("Seu peso ideal é: ", Peso)

""""exercício 2"""
QtdKm = float(input("Informe a quantidade de quilômetros percorridos: "))
QtdDias = int(input("Informe a quantidade de dias no qual o carro foi alugado: "))
Dias = QtdDias * 60
Quil = QtdKm * float(0.15)
Total = Dias + Quil
print("O total a pagar pelo indivíduo é:", Total)

"""execício 3"""
Dias = int(input("Informe a quantidade de dias: "))
Horas = int(input("Informe a quantidade de horas: " ))
Minutos = int(input("Informe a quantidade de minutos: " ))
Segundos = int(input("Informe a quantidade de segundos: " ))
Total = Dias * 86400 + Horas * 3600 + Minutos * 60 + Segundos
print("O total em segundos é: ", Total)
