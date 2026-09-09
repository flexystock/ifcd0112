
n = 10
x = 0
par = 0
impar = 0

while x < n:
    num = int(input("Introduce un numero: "))

    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1

    x = x + 1

print("Numero de pares:", par)
print("Numero de impares:", impar)
