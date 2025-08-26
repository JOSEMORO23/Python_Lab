grafo = {
    'Ecuador': ['Pichincha', 'Guayas', 'Azuay', 'Manabi', 'El Oro', 'Loja', 'Tungurahua', 'Imbabura', 'Chimborazo', 'Esmeraldas'],
    'Pichincha': ['Quito'],
    'Guayas': ['Guayaquil', 'Daule', 'Samborondon'],
    'Azuay': ['Cuenca', 'Gualaceo', 'Chordeleg'],
    'Manabi': ['Portoviejo', 'Manta', 'Bahia de Caraquez'],
    'El Oro': ['Machala', 'Huaquillas', 'Pasaje'],
    'Loja': ['Loja', 'Vilcabamba', 'Catamayo'],
    'Tungurahua': ['Ambato', 'Baños', 'Pelileo'],
    'Imbabura': ['Ibarra', 'Otavalo', 'Cotacachi'],
    'Chimborazo': ['Riobamba', 'Guano', 'Penipe'],
    'Esmeraldas': ['Esmeraldas', 'Atacames', 'Quininde'],
    'Quito': ['Mitad del Mundo', 'Hornado', 'Cumbaya', 'Empanadas de viento'],
    'Guayaquil': ['Encebollado', 'Ceviche'],
    'Daule': [],
    'Samborondon': [],
    'Cuenca': ['Cuy asado', 'Mote pillo'],
    'Gualaceo': [],
    'Chordeleg': [],
    'Portoviejo': ['Viche'],
    'Manta': [],
    'Bahia de Caraquez': ['Bolon de verde'],
    'Machala': ['Cangrejo criollo'],
    'Huaquillas': [],
    'Pasaje': ['Seco de chivo'],
    'Loja': ['Repe lojano'],
    'Vilcabamba': [],
    'Catamayo': ['Tamales lojanos'],
    'Ambato': ['Melocha'],
    'Baños': [],
    'Pelileo': ['Colada morada'],
    'Ibarra': ['Fritada'],
    'Otavalo': ['Yahuarcocha'],
    'Cotacachi': [],
    'Riobamba': ['Chimborazo hornado'],
    'Guano': [],
    'Penipe': ['Llapingachos'],
    'Esmeraldas': [],
    'Atacames': ['Encocado de camaron'],
    'Quininde': ['Tapao de pescado']
}

def dfs_pila(inicio, destino):
    pila_abierta = [(inicio, [inicio])]  # (nodo, camino hasta aquí)
    visitados = set()

    while pila_abierta:
        nodo_actual, camino = pila_abierta.pop()

        if nodo_actual == destino:
            return camino

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            for hijo in grafo.get(nodo_actual, []):
                pila_abierta.append((hijo, camino + [hijo]))

    return None

# Entrada interactiva
print("Nodos disponibles:", ", ".join(grafo.keys()))
inicio = input("Ingresa el nodo de inicio: ").strip()
destino = input("Ingresa el nodo de destino: ").strip()

if inicio not in grafo or destino not in grafo:
    print("Uno de los nodos no es válido.")
else:
    camino = dfs_pila(inicio, destino)
    if camino:
        print("Camino encontrado (DFS -):", " -> ".join(camino))
    else:
        print("No se encontró un camino entre esos nodos.")
