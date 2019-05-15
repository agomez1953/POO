class Punto:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def desplazarX (self, x):
        return Punto(self.x + x, self.y)

    def desplazarY (self, y):
        return Punto(self.x ,self.y + y)

    def hallar_pendiente(self,other):
        return (self.y-other.y)/(self.x-other.x)

    def __repr__(self):
        return f'En {self.x,self.y}'

