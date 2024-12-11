import math
import random

# Dette er et eksempel på Python-kode som viser forskjellige matematiske operasjoner

# Legg til to tall
a = 5
b = 3
summen = a + b
print("Summen av", a, "og", b, "er", summen)

# Subtraher to tall
x = 10
y = 7
differanse = x - y
print("Differansen mellom", x, "og", y, "er", differanse)

# Multipliser to tall
m = 4
n = 6
produktet = m * n
print("Produktet av", m, "og", n, "er", produktet)

# Divider to tall
p = 15
q = 3
kvotienten = p / q
print("Kvotienten mellom", p, "og", q, "er", kvotienten)

# Beregn resten av en divisjon
r = 17
s = 5
resten = r % s
print("Resten av", r, "delt på", s, "er", resten)

# Opphøyning i en potens
base = 2
eksponent = 3
resultat = base ** eksponent
print(base, "opphøyd i", eksponent, "er", resultat)

# Eksempel på å finne kvadratroten av et tall

tall = 9
kvadratroten = math.sqrt(tall)
print("Kvadratroten av", tall, "er", kvadratroten)

# Eksempel på å runde av et desimaltall
desimaltall = 3.14159
avrundet_tall = round(desimaltall, 2)
print("Avrundet tall:", avrundet_tall)

# Eksempel på å generere tilfeldige tall

tilfeldig_tall = random.randint(1, 10)
print("Tilfeldig tall mellom 1 og 10:", tilfeldig_tall)

# Eksempel på å konvertere mellom datatyper
tekst = "42"
tall = int(tekst)
print("Konvertert tall:", tall)

# Eksempel på å bruke en matematisk funksjon
vinkel = 45
radians = math.radians(vinkel)
sinus_verdi = math.sin(radians)
print("Sinus av", vinkel, "grader:", sinus_verdi)

