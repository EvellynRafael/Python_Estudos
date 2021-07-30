import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2-4*a*c

if delta < 0:
    print("Não há raizes")
elif delta == 0:
    raiz = (-1*b + math.sqrt(delta)) / (2*a)
else:
    print("x1: ",(-1*b+math.sqrt(delta))/2*a)
    print("x2: ",(-1*b-math.sqrt(delta))/2*a)