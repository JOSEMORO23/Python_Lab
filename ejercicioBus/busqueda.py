from collections import deque

# Representación del grafo
grafo = {
    'Frankfurt': ['Mannheim', 'Wurzburg', 'Kassel'],
    'Mannheim': ['Frankfurt', 'Karlsruhe'],
    'Karlsruhe': ['Mannheim', 'Erfurt'],
    'Erfurt': ['Karlsruhe', 'Wurzburg', 'Augsburg'],
    'Augsburg': ['Erfurt', 'Munchen'],
    'Munchen': ['Augsburg', 'Nurnberg'],
    'Nurnberg': ['München', 'Wurzburg', 'Stuttgart'],
    'Wurzburg': ['Frankfurt', 'Nurnberg', 'Erfurt'],
    'Stuttgart': ['Nurnberg', 'Kassel'],
    'Kassel': ['Stuttgart', 'Frankfurt']
}

def buscar_cam(inicio, destino):
    visitados = set()
    cola = deque([[inicio]])

    while cola:
        camino = cola.popleft()
        ciudad_act = camino[-1]

        if ciudad_act == destino:
            return camino

        if ciudad_act not in visitados:
            visitados.add(ciudad_act)
            for vecino in grafo.get(ciudad_act, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
    return None

# Interfaz de entrada
print("Ciudades disponibles:", ", ".join(grafo.keys()))
inicio = input("Ingresa la ciudad en la se encuentra: ").strip()
destino = input("Ingresa la ciudad de destino: ").strip()

if inicio not in grafo or destino not in grafo:
    print("Una de las ciudades no es válida. Verifica los nombres.")
else:
    camino = buscar_cam(inicio, destino)
    if camino:
        print("Camino encontrado:", " -> ".join(camino))
    else:
        print("No hay camino disponible entre esas ciudades.")
