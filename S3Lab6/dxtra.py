import math
from dataclasses import dataclass
from typing import Generic, Optional

from heap import Heap, IKey
from graph import Graph, T, AdjacentEdge


@dataclass
class _dxtraNode(Generic[T], IKey):
    vertex: T
    distance: int
    predecessor: Optional['_dxtraNode[T]'] = None

    def key(self) -> int:
        return self.distance

    def name(self) -> str:
        return f"{self.vertex}"


def dxtra_algorithm(funk_graph: Graph[T], start: T, end: T) -> tuple[list[T], int]:
    heap = Heap[_dxtraNode[T]](funk_graph.amount_vertexes(), True)
    nodes: dict[T, _dxtraNode[T]] = {}

    def foreach_init(vertex: T):
        node = _dxtraNode[T](vertex, math.inf)
        heap.insert(node)
        nodes[vertex] = node

    funk_graph.for_each_vertex(foreach_init)

    nodes[start].distance = 0
    heap.change(nodes[start])

    while not heap.is_empty():
        v: _dxtraNode[T] = heap.remove()

        def calc(edge: AdjacentEdge[T]):
            node = nodes[edge.finish_edge]

            if node is None:
                return

            if v.distance + edge.weight < node.distance:
                node.distance = v.distance + edge.weight
                node.predecessor = v
                heap.change(node)
        funk_graph.for_each_adjacent_edge(v.vertex, calc)

        if v.vertex == end:
            dxtra_path: list[T] = []
            dxtra_cost = v.distance
            dxtra_iterator = v
            while dxtra_iterator is not None:
                dxtra_path.append(dxtra_iterator.vertex)
                dxtra_iterator = dxtra_iterator.predecessor
            return dxtra_path, dxtra_cost
    return [], 0
