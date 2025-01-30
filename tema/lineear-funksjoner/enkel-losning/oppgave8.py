# Forklar hva koden gjør.
# Den beregner et innskudd over flere år med rente.

saldo = 0
rente = 0.05

for år in range(10):
    if år < 5:
        saldo += 5000
    saldo *= 1.05

print(f"Saldo etter 10 år: {round(saldo, 2)} kr")
