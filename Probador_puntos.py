from Punto import Punto

puntico1 = Punto(2,3)
puntico2 = Punto(2,3)
print(f'mi punto es {puntico1}')
if puntico1 == puntico2:
    print('El punto',puntico1, 'y el punto',puntico2,'son iguales')
else:
    print('El punto',puntico1, 'y el punto', puntico2, 'son diferentes')

print(puntico1.desplazarX(3))
print(puntico1.desplazarY(7))

print('la pendiente de los puntos es',Punto.hallar_pendiente(puntico1,puntico2))