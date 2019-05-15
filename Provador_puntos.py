from Punto import Punto

puntico1 = Punto(2,3)
puntico2 = Punto(3,4)
print(f'mi punto es {puntico1}')
if puntico1 == puntico2:
    print('El punto',puntico1, 'y el punto',puntico2,'son iguales')
else:
    print('El punto',puntico1, 'y el punto', puntico2, 'son diferentes')


print ('el punto al desplazarse es (',puntico1.desplazarX(1),',',puntico1.y,')')
print ('el punto al desplazarse es (',puntico1.y,',',puntico1.desplazarY(1),')')