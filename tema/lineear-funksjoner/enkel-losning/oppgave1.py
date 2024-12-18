
# Be brukeren om å oppgi alderen sin
alder = int(input("Hvor gammel er du? "))

# Definer rabattprosentene for ulike aldersgrupper
rabatt_barn = 100  # Rabattprosent for barn
rabatt_ungdom = 50  # Rabattprosent for ungdom
rabatt_senior = 50  # Rabattprosent for eldre

# Definer grunnprisen for billetten
billettpris = 500

# Beregn billettprisen basert på alderen
if alder < 6: # Sjekk om brukeren er yngre enn 6
    pris = billettpris * (1 - rabatt_barn/100)  # Beregn billettpris med rabatt for barn
elif alder < 16: # Sjekk om brukeren er yngre enn 16
    pris = billettpris * (1 - rabatt_ungdom/100)  # Beregn billettpris med rabatt for ungdom
elif alder < 66: # Sjekk om brukeren er yngre enn 66
    pris = billettpris  # Ingen rabatt for eldre
else: # Hvis ingen av de overnevnte betingelsene er oppfylt, må brukeren være 66 år eller eldre
    pris = billettpris * (1 - rabatt_senior/100)  # Beregn billettpris med rabatt for andre aldersgrupper

# Skriv ut den beregnede billettprisen
print(f"Du må betale {pris} kr.")


