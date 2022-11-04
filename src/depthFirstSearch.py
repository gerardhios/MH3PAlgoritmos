import json
import os
from pathlib import Path
from random import randint
from time import sleep

def savegraph():
    vertex_list = input("Lista de vertices (Separados por espacio):\n").split()
    adyacency_dict = {}
    for vertex in vertex_list:
        lst = input("Vertices adyacentes a [" + vertex + "] (Separados por espacio):\n").split()
        for i in lst:
            if i not in vertex_list:
                lst.remove(i)
        adyacency_dict[vertex] = lst
        
    adyacency_dict['vertex_list'] = vertex_list
    
    with open('graph.json', 'w') as f:
        json.dump(adyacency_dict, f)
    print("Grafo guardado en graph.json")

def loadgraph() -> dict:
    with open('graph.json') as f:
        graph = json.load(f)
    return graph
    
def depth_first_search(graph:dict, actual:str, goal:str, visited:list, adyacents:list) -> list:
    if actual == goal:
        print(f"Se encontro el vertice {goal}\nCamino:", end=" ")
        for i in visited:
            print(i, end=" ")
        return
    if goal in visited:
        return
    for adyacent in adyacents:
        if adyacent not in visited:
            visited.append(adyacent)
            depth_first_search(graph, adyacent, goal, visited, graph[adyacent])

if __name__ == "__main__":
    path = Path("graph.json")
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
    depth_first_search(graph, start, goal, [start], graph[start])
        
    