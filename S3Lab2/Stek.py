from typing import Generic, TypeVar, Optional
from dataclasses import dataclass

T = TypeVar('T')


class StakOverFlowExemption(Exception):
    pass


@dataclass
class StekNode(Generic[T]):  # Нода
    data: T
    prev_data: Optional['StekNode[T]'] = None


class Stek(Generic[T]):  # Класс стека
    def __init__(self) -> None:  # Инициализация переменных
        self._tail: Optional[StekNode[T]] = None
        self._length: int = 0

    def __str__(self) -> str:  # Вывод стека в функции print
        if self._length == 0:
            return "None"
        my_str = "("
        node = self._tail
        while node is not None:
            my_str += str(node.data) + ", "
            node = node.prev_data
        my_str = my_str[:-2]
        my_str += ")"
        return my_str

    def push(self, data: T) -> None:  # добавление в стек
        node = StekNode[T](data)
        if self._length == 0:
            self._tail = node
            self._length += 1
            return
        last_node = self._tail
        node.prev_data = last_node
        self._tail = node
        self._length += 1
        return

    def get_data(self) -> T:  # получение данных о значении последнего элемента в стеке
        if self._length > 0:
            return self._tail.data
        return None

    def len(self) -> int:  # Выдаёт длину стека
        return self._length

    def pop(self) -> T:  # Выдаёт последний элемент и удаляет его из стека
        if self._length <= 0:
            raise StakOverFlowExemption
        last_node = self._tail
        self._tail = last_node.prev_data
        last_node.prev_data = None
        self._length -= 1
        return last_node.data
