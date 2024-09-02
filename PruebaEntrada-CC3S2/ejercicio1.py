import sys

class Graph:
    def __init__(self, vertices):
        # Validación para asegurar que el número de vértices es un entero positivo.
        if not isinstance(vertices, int) or vertices <= 0:
            raise ValueError("El número de vértices debe ser un entero positivo.")
        
        # Inicializamos el número de vértices.
        self.V = vertices  
        
        # Inicializamos la matriz de adyacencia (VxV) con ceros.
        # self.graph[i][j] representa el peso de la arista entre el vértice i y j.
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)] 
        
    def print_solution(self, dist):
        # Método para imprimir las distancias mínimas desde el vértice origen.
        try:
            print("Vertice \tDistancia desde el origen")
            for node in range(self.V):
                print(node, "\t\t", dist[node])
        except Exception as e:
            print(f"Error al imprimir la solución: {e}")

    def min_distance(self, dist, spt_set):
        # Encuentra el vértice con la distancia mínima desde el conjunto
        # de vértices que aún no han sido procesados.
        min = sys.maxsize  # Inicializamos la distancia mínima como infinita.
        min_index = -1  # Inicializamos el índice mínimo como -1 (invalido).

        try:
            for v in range(self.V):
                # Si dist[v] es menor que min y el vértice aún no ha sido procesado
                # (es decir, no está en spt_set), actualizamos min y min_index.
                if dist[v] < min and spt_set[v] == False:
                    min = dist[v]
                    min_index = v
        except IndexError:
            # Capturamos cualquier error de índice fuera de los límites.
            raise IndexError("Índice fuera de los límites al buscar la distancia mínima.")
        
        return min_index
    
    def dijkstra(self, src):
        # Implementación del algoritmo de Dijkstra.
        # Calcula las distancias más cortas desde el vértice origen (src) a todos los otros vértices.
        
        # Validación para asegurar que el vértice origen está dentro de los límites.
        if src < 0 or src >= self.V:
            raise ValueError("El vértice de origen está fuera de los límites.")
        
        # Inicializamos las distancias como infinitas y dist[src] como 0.
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        
        # spt_set[i] será verdadero si el vértice i está incluido en el conjunto de
        # vértices cuyo camino más corto desde src ya se ha determinado.
        spt_set = [False] * self.V

        try:
            for _ in range(self.V):
                # Elegimos el vértice de distancia mínima que aún no ha sido procesado.
                u = self.min_distance(dist, spt_set)
                
                # Si min_distance devuelve -1, no hay más vértices alcanzables.
                if u == -1:
                    break

                # Marcamos el vértice 'u' como procesado.
                spt_set[u] = True

                # Actualizamos dist[v] solo si no está en spt_set, hay una arista desde 'u' a 'v',
                # y el camino desde src a v a través de u es más corto que el valor actual en dist[v].
                for v in range(self.V):
                    if (
                        self.graph[u][v] > 0
                        and not spt_set[v]
                        and dist[v] > dist[u] + self.graph[u][v]
                    ):
                        dist[v] = dist[u] + self.graph[u][v]

            # Imprimimos la solución final.
            self.print_solution(dist)
        
        except Exception as e:
            # Capturamos cualquier excepción durante la ejecución del algoritmo.
            print(f"Se ha producido un error durante la ejecución del algoritmo de Dijkstra: {e}")

    def add_edge(self, u, v, weight):
        """Añade una arista entre los vértices 'u' y 'v' con un peso 'weight'."""
        # Validación para asegurar que los índices de los vértices están dentro de los límites.
        if u < 0 or u >= self.V or v < 0 or v >= self.V:
            raise ValueError("Los índices de los vértices deben estar dentro de los límites.")
        # Validación para asegurar que el peso de la arista es un número positivo.
        if weight <= 0:
            raise ValueError("El peso de la arista debe ser un número positivo.")
        
        # Añadimos la arista en ambas direcciones ya que estamos considerando un grafo no dirigido.
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def add_vertex(self):
        """Añade un nuevo vértice al grafo."""
        # Incrementamos el número de vértices.
        self.V += 1
        # Añadimos una nueva fila a la matriz de adyacencia para el nuevo vértice.
        for row in self.graph:
            row.append(0)  # Inicializamos la nueva columna con 0 (sin arista).
        # Añadimos una nueva fila de ceros.
        self.graph.append([0] * self.V)

# Ejemplo de uso:
try:
    # Creamos un grafo inicialmente con 5 vértices.
    g = Graph(5)
    
    # Añadimos aristas entre los vértices con sus respectivos pesos.
    g.add_edge(0, 1, 4)
    g.add_edge(1, 2, 8)
    g.add_edge(2, 3, 7)
    g.add_edge(3, 4, 9)
    g.add_edge(4, 0, 10)

    # Añadimos un nuevo vértice al grafo.
    g.add_vertex()
    
    # Añadimos aristas para el nuevo vértice (vértice 5).
    g.add_edge(5, 0, 8)
    g.add_edge(5, 3, 2)
    
    # Ejecutamos el algoritmo de Dijkstra desde el vértice 0.
    g.dijkstra(0)

except ValueError as ve:
    # Capturamos y mostramos los errores de valor.
    print(f"Error de valor: {ve}")

except Exception as e:
    # Capturamos y mostramos cualquier error inesperado.
    print(f"Se ha producido un error inesperado: {e}")
