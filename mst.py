# mst.py
import heapq

def prim(grafo_dict, origen):
    """Algoritmo de Prim para MST usando un min-heap."""
    mst_aristas = []
    peso_total = 0
    visitados = {origen}
    aristas_candidatas = []
    
    for vecino, peso in grafo_dict.get(origen, []):
        heapq.heappush(aristas_candidatas, (peso, origen, vecino))
        
    while aristas_candidatas:
        peso, u, v = heapq.heappop(aristas_candidatas)
        if v not in visitados:
            visitados.add(v)
            peso_total += peso
            mst_aristas.append((u, v, peso))
            for siguiente, p in grafo_dict.get(v, []):
                if siguiente not in visitados:
                    heapq.heappush(aristas_candidatas, (p, v, siguiente))
    return peso_total, mst_aristas

class UnionFind:
    def __init__(self, vertices):
        self.padre = {v: v for v in vertices}
        self.rango = {v: 0 for v in vertices}
        
    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]
        
    def union(self, x, y):
        raiz_x = self.find(x)
        raiz_y = self.find(y)
        if raiz_x != raiz_y:
            if self.rango[raiz_x] < self.rango[raiz_y]:
                self.padre[raiz_x] = raiz_y
            elif self.rango[raiz_x] > self.rango[raiz_y]:
                self.padre[raiz_y] = raiz_x
            else:
                self.padre[raiz_y] = raiz_x
                self.rango[raiz_x] += 1
            return True
        return False

def kruskal(vertices, aristas):
    """Algoritmo de Kruskal para MST usando Union-Find."""
    uf = UnionFind(vertices)
    mst_aristas = []
    peso_total = 0
    # Ordenar aristas por peso
    aristas_ordenadas = sorted(aristas, key=lambda x: x[2])
    
    for u, v, peso in aristas_ordenadas:
        if uf.union(u, v):
            peso_total += peso
            mst_aristas.append((u, v, peso))
    return peso_total, mst_aristas

if __name__ == "__main__":
    print("--- PRUEBA 1: Grafo K4 Completo ---")
    vertices_k4 = [0, 1, 2, 3]
    aristas_k4 = [(0,1,1), (0,2,2), (0,3,3), (1,2,4), (1,3,5), (2,3,6)]
    # Formato para Prim
    grafo_prim = {v: [] for v in vertices_k4}
    for u, v, p in aristas_k4:
        grafo_prim[u].append((v, p))
        grafo_prim[v].append((u, p))
    
    p_peso, _ = prim(grafo_prim, 0)
    k_peso, _ = kruskal(vertices_k4, aristas_k4)
    print(f"Peso Prim: {p_peso}, Peso Kruskal: {k_peso}")

    print("\n--- PRUEBA 2: Grafo 5 vértices ---")
    v2 = ['A', 'B', 'C', 'D', 'E']
    e2 = [('A','B',2), ('A','C',3), ('B','C',1), ('B','D',4), ('C','D',5), ('C','E',6), ('D','E',2)]
    g2_prim = {v: [] for v in v2}
    for u, v, p in e2:
        g2_prim[u].append((v, p))
        g2_prim[v].append((u, p))
    
    p2, _ = prim(g2_prim, 'A')
    k2, _ = kruskal(v2, e2)
    print(f"Peso Prim: {p2}, Peso Kruskal: {k2}")