Hora01 = int(input("Digite o Primeiro Horário: "))
Minuto01 = int(input("Digite os Minutos: "))

Hora02 = int(input("Digite o Segundo Horário: "))
Minuto02 = int(input("Digite os Minutos: "))

HoraTotal = Hora01 + Hora02
MinutoTotal = Minuto01 + Minuto02

if MinutoTotal >= 60:
    HoraTotal =  HoraTotal + 1
    MinutoTotal = MinutoTotal - 60
if HoraTotal >= 12:
    HoraTotal = HoraTotal - 12
if HoraTotal > 24:
    HoraTotal = HoraTotal - 24

print(HoraTotal, MinutoTotal)


