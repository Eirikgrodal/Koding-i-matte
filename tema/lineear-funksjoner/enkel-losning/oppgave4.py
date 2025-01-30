# Hvor mye har du i banken etter 10 år med 5000 kr innskudd årlig og 5% rente?
saldo = 0
rente = 0.05

for år in range(10):
    saldo = (saldo + 5000) * (1 + rente)

print(f"Etter 10 år har du {round(saldo, 2)} kr")

# Hvor mye med 50 000 kr engangsinnskudd?
saldo = 50000

for _ in range(10):
    saldo *= 1.05

print(f"Saldo etter 10 år: {round(saldo, 2)} kr")

# Hvor mye renter totalt?
totalt_innskudd = 5000 * 10
totalt_opptjent = saldo
renter = totalt_opptjent - totalt_innskudd

print(f"Totalt opptjente renter: {round(renter, 2)} kr")
