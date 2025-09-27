from dataclasses import dataclass
from typing import TypeVar, Generic, Callable

from set import MySet

T = TypeVar("T")


@dataclass
class Edge(Generic[T]):
    start_edge: T
    finish_edge: T
    weight: int = 0


@dataclass
class AdjacentEdge(Generic[T]):
    finish_edge: T
    weight: int = 0

    def __hash__(self) -> int:
        return hash((self.finish_edge, self.weight))


class Graph(Generic[T]):
    def __init__(self, is_directed: bool = False) -> None:
        self.vertexes: dict[T, MySet[AdjacentEdge[T]]] = {}
        self.is_not_directed: bool = not is_directed

    def add_vertex(self, vertex: T) -> None:
        if vertex not in self.vertexes:
            self.vertexes[vertex] = MySet[AdjacentEdge[T]]()

    def add_edge(self, vertex1: T, vertex2: T, weight: int) -> None:
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.vertexes[vertex1].add(AdjacentEdge[T](vertex2, weight))
        if self.is_not_directed:
            self.vertexes[vertex2].add(AdjacentEdge[T](vertex1, weight))

    def add_edge_without_weight(self, vertex1: T, vertex2: T) -> None:
        self.add_edge(vertex1, vertex2, 0)

    def for_each_vertex(self, func: Callable[[T], None]) -> None:
        for v, _ in self.vertexes.items():
            func(v)

    def for_each_edge(self, func: Callable[[Edge[T]], None]) -> None:
        for vertex1, edges in self.vertexes.items():
            def edge_creator(value: AdjacentEdge[T]) -> None:
                func(Edge[T](vertex1, value.finish_edge, value.weight))

            edges.for_each(edge_creator)

    def for_each_adjacent_edge(self, vertex: T, func: Callable[[AdjacentEdge[T]], None]):
        if vertex in self.vertexes:
            edges = self.vertexes[vertex]
            edges.for_each(lambda x: func(x))

    def amount_edges(self) -> int:
        count: int = 0
        for _, edges in self.vertexes.items():
            count += edges.size()

        if self.is_not_directed:
            count //= 2

        return count

    def amount_vertexes(self) -> int:
        return len(self.vertexes)

    def print_all_edges(self) -> None:
        def print_edge(edge: Edge[T]) -> None:
            print(f"Ребро(Из {edge.start_edge} в {edge.finish_edge}, Расстояние: {edge.weight})")
        self.for_each_edge(print_edge)

    def print_all_vertexes(self) -> None:
        def print_vertex(vertex: T) -> None:
            print(f"Вершина: {vertex}")
        self.for_each_vertex(print_vertex)

    def save_graph(self, file_name: str) -> None:
        file = open(file_name, 'w')
        for vertex1, edges in self.vertexes.items():
            def edge_creator(value: AdjacentEdge[T]):
                mas = [vertex1, value.finish_edge, value.weight]
                vertex_line = str(mas[0]) + " " + str(mas[1]) + " " + str(mas[2]) + "\n"
                file.write(vertex_line)

            edges.for_each(edge_creator)

        file.close()

        file = open(file_name, 'r')
        mas = []
        for x in file:
            x = x[:-1].split()
            if len(mas) == 0:
                mas.append(x)
            else:
                m = 0
                for y in mas:
                    if y[0] == x[1] and y[1] == x[0]:
                        m += 1
                if m == 0:
                    mas.append(x)
                else:
                    pass
        file.close()

        file = open(file_name, 'w')
        for x in mas:
            x = str(x[0]) + " " + str(x[1]) + " " + str(x[2]) + "\n"
            file.write(x)
        file.close()

    def read_graph_from_file(self, file_name) -> None:
        file = open(file_name, 'r')
        lines = file.readlines()
        for x in lines:
            x = x.split()
            self.add_edge(str(x[0]), str(x[1]), int(x[2]))
        file.close()
