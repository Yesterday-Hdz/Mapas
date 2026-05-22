# Viaje por carretera con búsqueda A*
from arbol import Nodo
from math import sin, cos, acos
from functools import cmp_to_key

def compara(x, y):
    # g(n) + h(n) para la ciudad x
    lat1 = coord[x.get_datos()][0]
    lon1 = coord[x.get_datos()][1]
    lat2 = coord[solucion][0]
    lon2 = coord[solucion][1]

    d1 = int(geodist(lat1, lon1, lat2, lon2))
    c1 = x.get_costo() + d1
    
    # g(n) + h(n) para la ciudad y
    lat1_y = coord[y.get_datos()][0]
    lon1_y = coord[y.get_datos()][1]
    
    d2 = int(geodist(lat1_y, lon1_y, lat2, lon2))
    c2 = y.get_costo() + d2

    return c1 - c2 

def geodist(lat1, lon1, lat2, lon2):
    grad_rad = 0.0174539
    rad_grad = 57.29577951
    longitud = lon1 - lon2
    val = (sin(lat1 * grad_rad) * sin(lat2 * grad_rad)) \
           + (cos(lat1 * grad_rad) * cos(lat2 * grad_rad) * cos(longitud * grad_rad))
    return (acos(val) * rad_grad) * 11.32

def buscar_solucion_USC(conexiones, estado_inicial, solucion):
    solucionado = False 
    nodos_visitados = []
    nodos_frontera = []
    
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_costo(0)
    
    nodos_frontera.append(nodo_inicial)
    
    while (not solucionado) and len(nodos_frontera) != 0:
        nodos_frontera = sorted(nodos_frontera, key=cmp_to_key(compara))
        nodo = nodos_frontera[0]
        
        # Extraer el nodo y añadir a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        
        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                
                # Calcular el costo acumulado g(n)
                costo = int(conexiones[dato_nodo][un_hijo]) 
                hijo.set_costo(nodo.get_costo() + costo)
                hijo.set_padre(nodo) 
                lista_hijos.append(hijo)
                
                if not hijo.en_lista(nodos_visitados):
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_costo() > hijo.get_costo():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
                        
            nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    conexiones = {
        'Jiloyork':{'CDMX': 125, 'QRO':513},
        'MORELOS':{'QRO':524},
        'CDMX':{'Jiloyork': 125, 'QRO':423, 'HGO':491},
        'HGO':{'CDMX':491, 'QRO':356, 'MEXICALI':309, 'MTY':346}, # Corregido: '309' a número 309
        'QRO':{'SLP':203, 'MORELOS':514, 'Jiloyork':513, 'CDMX':423, 'MTY':603, 'SONORA':437, 'HGO':356, 'MEXICALI':313, 'AGS':599},
        'SLP':{'AGS':390, 'QRO':203},
        'AGS':{'SLP':390, 'QRO':599},
        'SONORA':{'QRO':437, 'MEXICALI':394},
        'MEXICALI':{'MTY':296, 'HGO':309, 'QRO':313},
        'MTY':{'MEXICALI':296, 'QRO':603, 'HGO':346}
    }

    coord = {
        'Jiloyork':(19.952408902750292, -99.53304570197712),
        'CDMX':(19.432684900517486, -99.13333701698),
        'QRO':(20.587956563302367, -100.38793290667115),
        'MORELOS':(18.930555912984644, -99.22237799899486),
        'HGO':(20.127000042049925, -98.73156416258126),
        'AGS':(21.856150731885958, -102.28915655184271),
        'SLP':(22.151749211629454, -100.97643458591887),
        'SONORA':(29.07865856228773, -110.94760761628041),
        'MEXICALI':(29.07865856228773, -110.94760761628041),
        'MTY':(25.66616067388393, -100.32880810205152)
    }

    estado_inicial = 'Jiloyork'
    solucion = 'MTY'
    nodo_solucion = buscar_solucion_USC(conexiones, estado_inicial, solucion)
    
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.reverse()
        print("Ruta encontrada:", resultado)
        print('Costo Total:: ', str(nodo_solucion.get_costo()))
    else:
        print("No se pudo encontrar una ruta de solución.")