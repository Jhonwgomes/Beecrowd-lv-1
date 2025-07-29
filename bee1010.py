LINE1 = input().split()
CODE1 = LINE1[0]
UNITS1 = int(LINE1[1])
PRICE1 = float(LINE1[2])

LINE2 = input().split()
CODE2 = LINE2[0]
UNITS2 = int(LINE2[1])
PRICE2 = float(LINE2[2])

VALOR = (UNITS1*PRICE1)+(UNITS2*PRICE2)
print(f"VALOR A PAGAR: R$ {VALOR:.2f}")