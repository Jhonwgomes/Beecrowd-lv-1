valores = input().split()

A = int(valores[0])
B = int(valores[1])
C = int(valores[2])

maiorAB=(A+B+abs(A-B))/2
maior = (maiorAB+C+abs(maiorAB-C))/2
print(f"{maior:.0f} eh o maior")