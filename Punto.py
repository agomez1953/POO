class Punto:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def desplazarX (self, x):
        return self.x+x

    def desplazarY (self, y):
        return self.y + y

    def __repr__(self):
        return f'En {self.x,self.y}'

