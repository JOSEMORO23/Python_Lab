# ------------------------------------------------------------
# Rutas entre ciudades de Ecuador: BFS y DFS
# Al ejecutar:
#   1) Pregunta ciudad de origen y destino (o usa argumentos --from / --to)
#   2) Calcula la ruta con *Búsqueda por Anchura* (BFS) y *Búsqueda en Profundidad* (DFS)
#   3) Muestra ambas rutas (y distancias) en consola
#   4) Dibuja el grafo resaltando la ruta BFS en rojo
# ------------------------------------------------------------

# ------------- importaciones estándar -------------
import json                  # leer / escribir el grafo en disco
import argparse              # analizar argumentos de línea de comandos
import sys                   # finalizar el programa con errores cuando sea necesario
import heapq                 # sólo se usa para BFS con cola (pop(0) podría evitarse, lo conservamos)
import networkx as nx        # librería para grafos y visualización
import matplotlib.pyplot as plt  # dibujar el grafo

GRAPH_FILE = "ecuador.json"   # nombre del archivo que persiste el grafo

# -------------------------------------------------- 1. Cargar / guardar grafo
def load_graph():
    """
    Intenta cargar un grafo {ciudad: {vecina: distancia_km}} desde JSON.
    Si el archivo no existe, devuelve un grafo base ‘quemado’ en el código.
    """
    try:
        with open(GRAPH_FILE, "r", encoding="utf-8") as f:
            return json.load(f)               # ← grafo persistenteFo
    except FileNotFoundError:
        # -------------- grafo por defecto (24 capitales + enlaces básicos) --------------
        return {
            "Tulcán": {"Ibarra": 120},
            "Ibarra": {"Tulcán": 120, "Quito": 115, "Esmeraldas": 170},
            "Esmeraldas": {"Ibarra": 170, "Santo Domingo": 190},
            "Quito": {"Ibarra": 115, "Latacunga": 90, "Santo Domingo": 140},
            "Latacunga": {"Quito": 90, "Ambato": 40},
            "Ambato": {"Latacunga": 40, "Riobamba": 55},
            "Riobamba": {"Ambato": 55, "Guaranda": 60, "Cuenca": 190},
            "Guaranda": {"Riobamba": 60, "Babahoyo": 120},
            "Santo Domingo": {"Quito": 140, "Esmeraldas": 190, "Portoviejo": 160},
            "Portoviejo": {"Santo Domingo": 160, "Guayaquil": 200},
            "Babahoyo": {"Guaranda": 120, "Guayaquil": 70},
            "Guayaquil": {"Babahoyo": 70, "Portoviejo": 200, "Santa Elena": 140, "Machala": 180},
            "Santa Elena": {"Guayaquil": 140},
            "Machala": {"Guayaquil": 180, "Loja": 210},
            "Cuenca": {"Riobamba": 190, "Azogues": 30, "Loja": 210, "Macas": 220},
            "Azogues": {"Cuenca": 30},
            "Loja": {"Cuenca": 210, "Machala": 210, "Zamora": 60},
            "Zamora": {"Loja": 60, "Macas": 130},
            "Macas": {"Cuenca": 220, "Puyo": 180, "Zamora": 130},
            "Puyo": {"Macas": 180, "Tena": 110, "Ambato": 100},
            "Tena": {"Puyo": 110, "Orellana": 160},
            "Orellana": {"Tena": 160, "Nueva Loja": 240},
            "Nueva Loja": {"Orellana": 240, "Francisco de Orellana": 60},
            "Francisco de Orellana": {"Nueva Loja": 60},
        }

def save_graph(g):
    """Guarda el grafo en disco para conservar conexiones añadidas."""
    with open(GRAPH_FILE, "w", encoding="utf-8") as f:
        json.dump(g, f, ensure_ascii=False, indent=2)

# -------------------------------------------------- 2. Algoritmos de búsqueda
def bfs(g, s, t):
    """
    Búsqueda por Anchura (Breadth‑First Search).
    Devuelve (ruta, distancia) donde distancia es la suma de km de la ruta hallada.
    """
    if s == t:                              # caso trivial
        return [s], 0
    q, vis = [[s]], {s}                     # cola de rutas y conjunto visitado
    while q:
        p = q.pop(0)                        # saca la ruta más antigua (FIFO)
        v = p[-1]                           # ciudad actual
        for nb in g.get(v, {}):             # vecinos de la ciudad
            if nb not in vis:
                np = p + [nb]               # nueva ruta extendida
                if nb == t:                 # destino hallado
                    dist = sum(g[np[i]][np[i+1]] for i in range(len(np)-1)) #Aquí np es la lista de ciudades del camino encontrado.
                                                                            #a expresión accede a la distancia entre dos ciudades consecutivas en el camino.
                    return np, dist
                q.append(np)                # encolar nueva ruta
                vis.add(nb)                 # marcar visitado
    return None, float("inf")               # sin ruta

def dfs(g, s, t):
    """
    Búsqueda en Profundidad (Depth‑First Search).
    Devuelve la primera ruta encontrada (no garantiza mínima en aristas).
    """
    st, vis = [[s]], set()                  # pila de rutas y visitados
    while st:
        p = st.pop()                        # pop LIFO
        v = p[-1]
        if v == t:
            dist = sum(g[p[i]][p[i+1]] for i in range(len(p)-1))   #Aquí np es la lista de ciudades del camino encontrado.
                                                                   #La expresión accede a la distancia entre dos ciudades consecutivas en el camino.
            return p, dist
        if v not in vis:
            vis.add(v)
            for nb in g.get(v, {}):
                if nb not in vis:
                    st.append(p + [nb])     # apilar ruta extendida
    return None, float("inf")

# -------------------------------------------------- 3. Visualización con networkx
def draw_graph(g, path=None):
    """
    Dibuja el grafo completo.
    Si 'path' se pasa, resalta esa ruta con aristas rojas.
    """
    G = nx.Graph()
    # Añadimos todos los nodos y aristas con pesos
    for c, nbs in g.items():
        for n, w in nbs.items():
            G.add_edge(c, n, weight=w)

    pos = nx.spring_layout(G, seed=42)      # layout reproducible
    # nodos y aristas base
    nx.draw(G, pos, with_labels=True, node_color="skyblue",
            node_size=1500, font_size=8, edge_color="lightgray")
    # etiquetas de pesos (km)
    nx.draw_networkx_edge_labels(G, pos,
        edge_labels=nx.get_edge_attributes(G,"weight"), font_size=7)

    # si hay ruta → resaltamos en rojo
    if path and len(path) > 1:
        edges = [(path[i], path[i+1]) if G.has_edge(path[i], path[i+1])
                 else (path[i+1], path[i]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges,
                               width=3, edge_color="red")
        plt.title("Ruta BFS resaltada en rojo")
    else:
        plt.title("Mapa de ciudades conectadas (Ecuador)")
    plt.show()

# -------------------------------------------------- 4. Lógica de línea de comandos
def main():
    # --- definir argumentos ----
    p = argparse.ArgumentParser()
    p.add_argument("--add", nargs=3, metavar=("CIUDAD1","CIUDAD2","DIST"),
                   help="Agregar conexión entre ciudades")
    p.add_argument("--from", dest="origen", help="Ciudad origen")
    p.add_argument("--to",   dest="destino", help="Ciudad destino")
    args = p.parse_args()

    g = load_graph()        # cargamos o creamos el grafo

  
    if args.add:
        c1, c2, dist = args.add
        dist = int(dist)
        g.setdefault(c1, {})[c2] = dist     # añadimos arista c1→c2
        g.setdefault(c2, {})[c1] = dist     # añadimos arista c2→c1
        save_graph(g)                       # persistimos cambios
        print(f"Conexión {c1}↔{c2} añadida ({dist} km)")
        draw_graph(g)                       # mostramos grafo actualizado
        return                              # terminamos ejecución

    # 4.2 Obtener origen y destino ----------------------------------------
    o, d = args.origen, args.destino
    if not o or not d:                      # si faltan → pedir por teclado
        print("\nCiudades disponibles:\n" + ", ".join(sorted(g)))
        try:
            o = input("\nCiudad origen: ").strip()
            d = input("Ciudad destino: ").strip()
        except EOFError:                   
            print("[Error] sin entrada interactiva.")
            sys.exit(1)

    if o not in g or d not in g:            # validamos que existan
        print("[Error] Ciudad no encontrada.")
        sys.exit(1)

    # 4.3 Ejecutar BFS y DFS ----------------------------------------------
    ruta_bfs, dist_bfs = bfs(g, o, d)
    ruta_dfs, dist_dfs = dfs(g, o, d)

    # 4.4 Mostrar resultados en consola -----------------------------------
    if ruta_bfs:
        print("\n=== Resultado BFS (anchura) ===")
        print(" -> ".join(ruta_bfs))
        print(f"Distancia (aprox): {dist_bfs} km")
    else:
        print("\nBFS: no existe ruta.")

    if ruta_dfs:
        print("\n=== Resultado DFS (profundidad) ===")
        print(" -> ".join(ruta_dfs))
        print(f"Distancia (aprox): {dist_dfs} km")
    else:
        print("\nDFS: no existe ruta.")

    # 4.5 Dibujar grafo resaltando ruta BFS (si la hubo) -------------------
    draw_graph(g, ruta_bfs if ruta_bfs else None)

# -------------------------------------------------- punto de entrada
if __name__ == "__main__":
    main()     # ← lanza toda la lógica si el archivo se ejecuta directamente
