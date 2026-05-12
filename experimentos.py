# experimentos.py
import time
import random
import math
import matplotlib.pyplot as plt
from mst import prim, kruskal

def generar_grafo(n, m, rango=(1, 100)):
    vertices = list(range(n))
    aristas = set()
    # Asegurar conectividad con un árbol aleatorio
    for i in range(1, n):
        u = random.randint(0, i-1)
        aristas.add(tuple(sorted((u, i)) + [random.randint(*rango)]))
    
    while len(aristas) < m:
        u, v = random.sample(vertices, 2)
        if u != v:
            arista = tuple(sorted((u, v)) + [random.randint(*rango)])
            aristas.add(arista)
            
    lista_aristas = list(aristas)
    dict_ady = {i: [] for i in vertices}
    for u, v, p in lista_aristas:
        dict_ady[u].append((v, p))
        dict_ady[v].append((u, p))
        
    return vertices, lista_aristas, dict_ady

def ejecutar_experimento():
    ns = [100, 200, 500, 1000]
    densidades = ["Dispersa", "Media", "Densa"]
    resultados = {d: {"prim": [], "kruskal": []} for d in densidades}

    print(f"{'V':<6} | {'E':<8} | {'Densidad':<10} | {'Prim (s)':<12} | {'Kruskal (s)':<12}")
    print("-" * 60)

    for n in ns:
        ms = {
            "Dispersa": n + 10,
            "Media": int(n * math.log2(n)),
            "Densa": (n * (n-1)) // 4
        }
        
        for d_nombre, m in ms.items():
            v, e, g_prim = generar_grafo(n, m)
            
            start = time.time()
            prim(g_prim, 0)
            t_prim = time.time() - start
            
            start = time.time()
            kruskal(v, e)
            t_kruskal = time.time() - start
            
            resultados[d_nombre]["prim"].append(t_prim)
            resultados[d_nombre]["kruskal"].append(t_kruskal)
            
            print(f"{n:<6} | {m:<8} | {d_nombre:<10} | {t_prim:<12.5f} | {t_kruskal:<12.5f}")

    # Gráficas
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    for i, d in enumerate(densidades):
        axs[i].plot(ns, resultados[d]["prim"], label="Prim", marker='o')
        axs[i].plot(ns, resultados[d]["kruskal"], label="Kruskal", marker='x')
        axs[i].set_title(f"Densidad {d}")
        axs[i].set_xlabel("Vértices")
        axs[i].set_ylabel("Tiempo (s)")
        axs[i].legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ejecutar_experimento()