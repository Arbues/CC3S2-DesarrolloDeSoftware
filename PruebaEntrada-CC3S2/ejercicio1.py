import sys

## Definimos una clase que representa un grafo con sus vértices y aristas
class Graph:
    ## Inicializamos los atributos del grafo.
    def __init__(self, vertices):
        # El número de vértices del grafo.
        self.V = vertices 
        
        # Inicializamos la matriz de adyacencia que representa las aristas y sus pesos.
        # Aquí, 'self.graph' es una matriz VxV donde cada elemento representa el peso de la arista.
        # Si no hay arista entre dos vértices, se representa con un 0.
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 
        
    ## Método para imprimir la solución final.
    def print_solution(self, dist):
        print("Vertice \tDistancia desde el origen")
        # Imprime la distancia mínima desde el vértice origen a cada vértice.
        for node in range(self.V):
            print(node, "\t\t", dist[node])
    
    ## Método que encuentra el vértice con la distancia mínima desde el conjunto de vértices
    ## que aún no han sido procesados.
    def min_distance(self, dist, spt_set):
        # Inicializamos la variable 'min' con un valor muy alto (infinito) para encontrar la distancia mínima.
        min = sys.maxsize
        
        # Iteramos sobre todos los vértices para encontrar el vértice con la distancia mínima.
        for v in range(self.V):
            # Si la distancia del vértice 'v' es menor que 'min' y 'v' aún no ha sido procesado,
            # actualizamos 'min' y 'min_index'.
            if dist[v] < min and spt_set[v] == False:
                min = dist[v]
                min_index = v
        
        # Retornamos el índice del vértice con la distancia mínima.
        return min_index
    
    ## Implementación del algoritmo de Dijkstra.
    ## Encuentra las distancias más cortas desde el vértice origen a todos los otros vértices.
    def dijkstra(self, src):
        # Inicializamos el array de distancias. Todas las distancias se inicializan como infinitas (sys.maxsize),
        # excepto la distancia desde el vértice origen a sí mismo, que es 0.
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        
        # Inicializamos el array 'spt_set'. Este array mantiene el registro de los vértices
        # para los cuales ya se ha encontrado la distancia mínima desde el origen.
        spt_set = [False] * self.V

        # Iteramos para encontrar el camino más corto para todos los vértices.
        for _ in range(self.V):
            # En cada iteración, seleccionamos el vértice con la distancia mínima del conjunto
            # de vértices que aún no han sido procesados.
            u = self.min_distance(dist, spt_set)
            
            # Marcamos el vértice 'u' como procesado.
            spt_set[u] = True

            # Actualizamos el valor de dist[] para los vértices adyacentes del vértice seleccionado.
            for v in range(self.V):
                # Las condiciones para actualizar dist[v] son:
                # 1. Hay una arista desde 'u' a 'v'.
                # 2. 'v' no ha sido procesado aún.
                # 3. La distancia total desde el origen hasta 'v' a través de 'u' es menor
                #    que la distancia actual almacenada en dist[v].
                if (
                    self.graph[u][v] > 0
                    and not spt_set[v]
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        # Llamamos al método print_solution para mostrar las distancias calculadas.
        self.print_solution(dist)

# Ejemplo de uso:
# Creamos un grafo con 9 vértices.
g = Graph(9)

# Definimos la matriz de adyacencia para representar el grafo.
# Los valores distintos de cero indican el peso de la arista entre dos vértices.
g.graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]

# Ejecutamos el algoritmo de Dijkstra desde el vértice 0.
g.dijkstra(0)
