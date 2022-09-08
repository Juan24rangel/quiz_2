#   Quiz


from math import trunc


print("-------------------------------------------")
print("-----DEMOSTRAR SI EL NUMERO ES CAPICUA-----")
print("-------------------------------------------")

#input

n = int(input("Digite el numero:"))

#processing
C1 = trunc (n/10000)
R1 = n % 10000
C2 = trunc (R1/1000)
R2 = R1 % 1000
C3 = trunc (R2/100)
R3 = R2 %100
C4 = trunc (R3/10)
C5 = R3 % 10

if C5==C1:
    x = ("si es capicua")
else:
    if C5!=C1:
        x = ("no es capicua")
if C4==C2:
    x = ("si es capicua")
else:
    if C4!=C2:
        x = ("no es capicua")

    

#output
print("¿cumple la condición?: " +str(x))