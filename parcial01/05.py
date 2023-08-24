a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

for i in range(a, b + 1):
  if i % 2 == 0:
    print(i)