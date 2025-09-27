from typing import Callable

from set import MySet
from queue import Queue
from graph import Graph, T, AdjacentEdge, Edge


def bsf(graph: Graph[T], start: T, walkfunc: Callable[[T], bool]) -> None:
    queue = Queue[T]()
    visited = MySet[T]()
    queue.enqueue(start)

    def __foreach(edge: AdjacentEdge[T]) -> None:
        if not visited.contains(edge.finish_edge):
            queue.enqueue(edge.finish_edge)

    while not queue.is_empty():
        vertex = queue.dequeue()

        if walkfunc(vertex):
            return

        visited.add(vertex)

        graph.for_each_adjacent_edge(vertex, __foreach)
