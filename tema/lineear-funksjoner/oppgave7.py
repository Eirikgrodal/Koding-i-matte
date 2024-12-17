lengths = [100, 90]  # Lengdene til de to første linjestykkene
total_length = sum(lengths)  # Summen av lengdene til de to første linjestykkene

# Generer de neste linjestykkene og beregn lengdene
while total_length < 900:  # Så lenge total lengde er mindre enn 9 m (900 cm)
    next_length = lengths[-1] * 0.9  # Lengden av det neste linjestykket er 90% av lengden til det forrige linjestykket
    lengths.append(next_length)  # Legg til lengden av det neste linjestykket i listen
    total_length += next_length  # Oppdater total lengde

# Svar på spørsmålene
length_3 = lengths[2]
length_4 = lengths[3]
sum_4 = sum(lengths[:4])
length_10 = lengths[9]
sum_10 = sum(lengths[:10])
num_pieces = len(lengths)

# Skriv ut svarene
print(f"Lengden av linjestykke nummer 3 er {length_3} cm.")
print(f"Lengden av linjestykke nummer 4 er {length_4} cm.")
print(f"Summen av lengden til de fire første linjestykkene er {sum_4} cm.")
print(f"Lengden av linjestykke nummer 10 er {length_10} cm.")
print(f"Summen av lengden til de ti første linjestykkene er {sum_10} cm.")
print(f"Antall linjestykker som trengs for å få til en totallengde på minst 9 m er {num_pieces}.")