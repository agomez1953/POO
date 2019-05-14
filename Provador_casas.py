from zope.interface.tests.test_odd_declarations import C

from Casa import Casa
mi_casa = Casa('calle 123 carrera 456')
casa_vecino = Casa('calle 124 carrera 456')
casa_Homero = Casa('Evergreen terrace 123, Springfield')

print(f'mi casa es{mi_casa},'' la del vecino es',{casa_vecino},' y la de homero es',{casa_Homero})
#se puede acceder de ambas maneras
mi_casa.banos = 2
mi_casa.ambientes =4
setattr(casa_vecino,"banos",3)
setattr(casa_vecino,"ambientes",5)
print(f'Mi casa tiene {mi_casa.ambientes} ambientes')
print(f'La del vecino tiene {casa_vecino.ambientes} ambientes')
atributos = casa_Homero.__dict__
# este for es para imprimir los atributos
for llave in atributos:
    print(f'atributo {llave} con el valor {atributos[llave]}')