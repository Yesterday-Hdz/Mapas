class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = 0
        if hijos:
            self.set_hijos(hijos)

    def set_hijos(self, hijos):
        self.hijos = hijos or []
        for h in self.hijos:
            # Asegurar que el hijo tiene el atributo set_padre
            try:
                h.set_padre(self)
            except AttributeError:
                h.padre = self

    def get_hijos(self):
        return self.hijos

    def get_padre(self):
        return self.padre
    
    def set_padre(self, padre):
        self.padre = padre

    def set_datos(self, datos):
        self.datos = datos 

    def get_datos(self):
        return self.datos
    
    def set_costo(self, costo):
        self.costo = costo
        
    def get_costo(self):
        return self.costo
    
    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()
        
    def en_lista(self, lista_nodos):
        for n in lista_nodos:
            if self.igual(n):
                return True
        return False
    
    def __str__(self):
        return str(self.get_datos())

# Alias lowercase por compatibilidad
nodo = Nodo