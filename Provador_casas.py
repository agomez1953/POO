from zope.interface.tests.test_odd_declarations import C

from Casa import Casa
mi_casa = Casa('calle 123 carrera 456')
casa_vecino = Casa('calle 124 carrera 456')
casa_Homero = Casa('Evergreen terrace 123, Springfield')

print(f'mi casa es{mi_casa},''la del vecino es',{casa_vecino},'y la de homero es',{casa_Homero})