#Programa de Conversao Segundos em Horas, Minutos, Segundos

SegundosInput = int(input("Por favor, entre com o número de segundos que deseja converter: "))

DiasOutput = SegundosInput // (3600*24)

HorasOutput = (SegundosInput % (3600*24)) // 3600

MinutosOutput = ((SegundosInput % (3600*24)) % 3600) // 60

SegundosOutput = ((SegundosInput % (3600*24)) % 3600) % 60


print(DiasOutput,"dias,",HorasOutput,"horas,",MinutosOutput,"minutos e",SegundosOutput,"segundos.")
