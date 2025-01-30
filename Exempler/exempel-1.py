
belop = 1000
rente = 0.25
ar = 0

while ar < 15:
    belop = belop * ( 1 + rente) 
    ar = ar + 1
    print(belop)
    print(ar)


belop = 1000
rente = 0.25
ar = 0

while ar in range(0,15):
    belop = belop * ( 1 + rente) 
    ar = ar + 1
    print(f"in range {belop}")
    print(ar)
