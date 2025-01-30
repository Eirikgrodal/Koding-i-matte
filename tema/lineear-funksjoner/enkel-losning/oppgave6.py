# Programmet beregner antall enheter solgt per måned med en lineær økning på 40 enheter.

enheter = 1000  # Startverdi
måned = 1

while måned <= 12:
    enheter *= 1.04  # Øker med 4%
    måned += 1

print(f"Etter ett år selges {round(enheter)} enheter per måned")

# Hvilken strategi ville du valgt?
# Fast økning (40 enheter/mnd) passer for stabile markeder.
# Prosentvis økning (4%) er bedre hvis veksten skal akselerere.