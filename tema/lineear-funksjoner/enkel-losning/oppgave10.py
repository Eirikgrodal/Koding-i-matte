# Finn utslippet for de tre første årene.

utslipp = 40

for år in range(3):
    utslipp *= 0.95
    print(f"År {år + 1}: {round(utslipp, 2)} tonn")

# Vis at totalutslippet er 114.1 tonn.
# Bruk summen av en geometrisk rekke.

# Lag program for utslipp etter 30 år.

utslipp = 40
total_utslipp = 0

for _ in range(30):
    total_utslipp += utslipp
    utslipp *= 0.95

print(f"Totalt utslipp etter 30 år: {round(total_utslipp, 2)} tonn")
