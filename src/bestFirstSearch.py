import json
import os
from pathlib import Path
from time import sleep

def savegraph():
    vertex_list = input("Lista de vertices (Separados por espacio):\n").split()
    adyacency_dict = {}
    for vertex in vertex_list:
        lst = []
        ady_vtx = input("Vertices adyacentes a [" + vertex + "] (Separados por espacio):\n").split()
        for i in ady_vtx:
            if i not in vertex_list:
                ady_vtx.remove(i)
            else:
                try:
                    cst = int(input("Costo de [" + vertex + "] a [" + i + "]:\n"))
                except ValueError:
                    print("Costo invalido, se asignara 0")
                    cst = 0
                finally:
                    lst.append((i, cst))
        adyacency_dict[vertex] = lst
        
    adyacency_dict['vertex_list'] = vertex_list
    
    with open('graph1.json', 'w') as f:
        json.dump(adyacency_dict, f)
    print("Grafo guardado en graph1.json")

def loadgraph() -> dict:
    with open('graph1.json') as f:
        graph = json.load(f)
    return graph

def pathCost(graph: dict, path: list) -> int:
    cost = 0
    for i in range(len(path) - 1):
        for vertex in graph[path[i]]:
            if vertex[0] == path[i + 1]:
                cost += vertex[1]
            else:
                continue
    return cost

def bestFirstSearch(graph: dict, start: str, goal: str) -> list:
    path = [start]
    queue = [vertex for vertex in graph[start]]
    while queue:
        queue.sort(key=lambda x: x[1])
        vertex = queue.pop(0)
        path.append(vertex[0])
        if vertex[0] == goal:
            print("Ruta encontrada: " + str(path))
            print("Costo de la ruta: " + str(pathCost(graph, path)))
            return
        else:
            queue.extend([vtx for vtx in graph[vertex[0]] if vtx[0] not in path])
    print("No se encontro un camino")
    print(f"Camino: {path}")
    print(f"Costo: {pathCost(graph, path)}")
    
if __name__ == "__main__":
    path = Path("graph1.json")
    if path.exists():
        print("Ya existe un grafo guardado")
        print("Desea sobreescribirlo? [Y/N]")
        if input() == "Y":
            savegraph()
    else:
        print("No existe un grafo guardado")
        print("Creando nuevo grafo...")
        savegraph()    
    graph = loadgraph()
    while True:
        print("Vertices del grafo: ", graph['vertex_list'])
        start = input("Vertice de inicio:\n")
        goal = input("Vertice de destino:\n")
        if start not in graph['vertex_list'] or goal not in graph['vertex_list']:
            print("Alguno de los vertices no existe en el grafo")
            sleep(5)
            os.system("cls")
            continue
        else :
            break
    bestFirstSearch(graph, start, goal)
    