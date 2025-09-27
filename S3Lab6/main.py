# 26 % 15 + 1 == 12
from dxtra import dxtra_algorithm
from graph import Graph
from Shirina import bsf, AdjacentEdge

if __name__ == '__main__':

    # Проверка работоспособности графа =================================================================================
    graph: Graph = Graph[str]()

    graph.add_edge("Новокузнецк", "Томск", 425)
    graph.add_edge("Новокузнецк", "Кемерово", 222)
    graph.add_edge("Новокузнецк", "Барнаул", 348)
    graph.add_edge("Томск", "Кемерово", 213)
    graph.add_edge("Томск", "Новосибирск", 266)
    graph.add_edge("Томск", "Барнаул", 466)
    graph.add_edge("Кемерово", "Новосибирск", 276)
    graph.add_edge("Кемерово", "Барнаул", 409)
    graph.add_edge("Новосибирск", "Барнаул", 229)

    print("Вершин в графе:", graph.amount_vertexes())
    print("---------Вершины-----------")
    graph.print_all_vertexes()
    print("Рёбер в графе", graph.amount_edges())
    print("---------Рёбра каждое ребро печатается дважды, так как имеет 2 направления-----------")
    graph.print_all_edges()
    graph.save_graph("vertex.txt")
    graph2 = Graph()
    graph2.read_graph_from_file('vertex.txt')
    print('_____________________________________________ГРАФ2_считанный из файла______________________________')
    print("---------Вершины-----------")
    graph2.print_all_vertexes()
    print("---------Рёбра каждое ребро печатается дважды, так как имеет 2 направления-----------")
    graph2.print_all_edges()
    print('_____________________________________________КОНЕЦ_ГРАФ2______________________________')

    # Дейкстра =========================================================================================================
    print("____________________________________Алгоритм Дейкстра ___________________________________---")
    path, cost = dxtra_algorithm(graph, "Новосибирск", "Новокузнецк")
    new_path = ""
    for x in path:
        new_path += x + " → "
    print(f"Путь: {path[0]}-{path[len(path)-1]}\nМаршрут: '{new_path[:-3]}'\nРасстояние: {cost}")

    # ширина ===========================================================================================================
    print("____________________________________Проходка по ширине ___________________________________---")

    def bsf_walk(vertex_1: str) -> bool:
        print(vertex_1 + " ", end='')
        return vertex_1 == "Новокузнецк"

    bsf(graph, "Новосибирск", bsf_walk)

    # ----------------Path---------------------
    path: list[str] = []

    def bsf_walk_with_path(vertex_1: str) -> bool:
        path.append(vertex_1)
        return vertex_1 == "Новокузнецк"

    bsf(graph, "Новосибирск", bsf_walk_with_path)

    path.reverse()
    min_path: list[str] = ["Новокузнецк", "Кемерово", "Новосибирск"]
    find: str = "Новокузнецк"
    for vertex in path:
        if graph.vertexes[vertex].contains(AdjacentEdge[str](find)):
            min_path.append(vertex)
            find = vertex
    min_path.reverse()
    print(min_path)
