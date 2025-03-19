# Sannsynligvis beregner den verdien av en sum med renter over tid.
startbeløp = 50000  # Sett inn ønsket startbeløp
rente = 0.057  # 5,7% rente

år = 15

for _ in range(år):
    startbeløp *= (1 + rente)

print(f"Etter {år} år er beløpet {round(startbeløp, 2)} kr")
