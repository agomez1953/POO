    #Para crear una clase utilizo la palabra reservada class

class Casa:
    banos=0
    ambientes=0

    def __init__(self, direccion):
        self.direccion = direccion
    def __repr__(self):
        return f'Casa ubicada en{self.direccion}'

