import collections

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, u, v):
        if u not in self.grafo: self.grafo[u] = []
        if v not in self.grafo: self.grafo[v] = []
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def bfs(self, origen):
        distancias = {nodo: float('inf') for nodo in self.grafo}
        if origen not in distancias: return "El nodo origen no existe."
        
        distancias[origen] = 0
        cola = collections.deque([origen])
        
        while cola:
            u = cola.popleft()
            for v in self.grafo[u]:
                if distancias[v] == float('inf'):
                    distancias[v] = distancias[u] + 1
                    cola.append(v)
        return {k: (v if v != float('inf') else -1) for k, v in distancias.items()}

    def dfs(self, origen):
        if origen not in self.grafo: return "El nodo origen no existe."
        visitados = []
        pila = [origen]
        while pila:
            u = pila.pop()
            if u not in visitados:
                visitados.append(u)
                for v in reversed(self.grafo[u]):
                    if v not in visitados:
                        pila.append(v)
        return visitados

    def tiene_ciclo(self):
        visitados = set()
        def dfs_ciclo(u, padre):
            visitados.add(u)
            for v in self.grafo[u]:
                if v not in visitados:
                    if dfs_ciclo(v, u): return True
                elif v != padre: return True
            return False
        for nodo in self.grafo:
            if nodo not in visitados:
                if dfs_ciclo(nodo, None): return True
        return False

# --- SECCIÓN DE ENTRADA DE DATOS ---

def ejecutar_programa():
    g = Grafo()
    print("*****BFS*****")
    try:
        n_aristas = int(input("Ingresa las aristas del grafo: "))
        
        for i in range(n_aristas):
            u, v = input(f"Ingresa la conexion entre nodos {i+1} (ejemplo: A B): ").split()
            g.agregar_arista(u, v)

        nodo_inicio = input("\n¿Cual es el nodo de incio?: ")

        print("\n--- RESULTADOS ---")
        print(f"1. Ditancia de los nodos desde el origen: {g.bfs(nodo_inicio)}")
        print(f"2. Orden de visita: {g.dfs(nodo_inicio)}")
        print(f"3. ¿Tiene ciclos?: {'Sí' if g.tiene_ciclo() else 'No'}")
        
    except ValueError:
        print("Error: Asegúrate de ingresar los datos en el formato correcto.")

if __name__ == "__main__":
    ejecutar_programa()
