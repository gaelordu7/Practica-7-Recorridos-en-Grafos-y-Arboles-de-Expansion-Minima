import heapq

def prim(grafo, origen):
    mst_edges = []
    total_weight = 0
    visitados = set()
    min_heap = [(0, None, origen)]
    
    while min_heap:
        peso, u, v = heapq.heappop(min_heap)
        if v in visitados:
            continue
        visitados.add(v)
        total_weight += peso
        if u is not None:
            mst_edges.append((u, v, peso))
        for vecino, peso_arista in grafo[v]:
            if vecino not in visitados:
                heapq.heappush(min_heap, (peso_arista, v, vecino))
                
    return total_weight, mst_edges

def solicitar_grafo():
    n_vertices = int(input("Número de vértices: "))
    n_aristas = int(input("Número de aristas: "))
    grafo = {i: [] for i in range(n_vertices + 1)}
    
    print("Ingresa las aristas y su peso en el fomeato (u, v, w):")
    for _ in range(n_aristas):
        u, v, w = map(int, input().split())
        grafo[u].append((v, w))
        grafo[v].append((u, w))
        
    origen_mst = int(input("Vértice de origen: "))
    return grafo, origen_mst

if __name__ == "__main__":
    g, inicio = solicitar_grafo()
    peso_total, aristas_mst = prim(g, inicio)
    
    print("\n--- Prim ---")
    print(f"Peso Total del MST: {peso_total}")
    print(f"Aristas del MST: {aristas_mst}")
