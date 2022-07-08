import math

xa = float(input("Digite o valor de XA: "))
ya = float(input("Digite o valor de YA: "))
xb = float(input("Digite o valor XB: "))
yb = float(input("Digite o valor de YB: "))

distanciaX = xb - xa
distanciaY = yb - ya
distancia = math.sqrt(distanciaX * distanciaX + distanciaY * distanciaY)

if distancia >= 10:
    print("longe")
    
else:
    print("perto")




