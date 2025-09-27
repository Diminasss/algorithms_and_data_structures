from typing import Generic, TypeVar, Optional
from dataclasses import dataclass


class IndexOutOfRangeException(Exception):  # Класс исключения
    pass


T = TypeVar('T')


@dataclass
class DoublyNode(Generic[T]):  # Нода
    data: T
    next_data: Optional['DoublyNode[T]'] = None
    prev_data: Optional['DoublyNode[T]'] = None


class DoublyLinkedList(Generic[T]):  # Класс двусвязного списка

    def __init__(self) -> None:  # Инициализация переменных
        self._length: int = 0
        self._head: Optional[DoublyNode[T]] = None
        self._tail: Optional[DoublyNode[T]] = None

    def __str__(self) -> str:  # Как будет выводиться класс при печати через print
        my_str: str = "["
        node = self._head
        while node is not None:
            if node.next_data is not None:
                my_str += str(node.data) + ", "
                node = node.next_data
            else:
                my_str += str(node.data)
                node = node.next_data
        my_str += "]"
        return my_str

    def __getitem__(self, index: int) -> T:  # Получить элемент через квадратные скобки [x]
        if self._length <= 0 or index >= self._length or index < 0:  # если за пределами списка
            raise IndexOutOfRangeException
        un_index = self._length - index
        if index <= un_index:  # если ближе с начала
            node = self._head
            for x in range(index):
                node = node.next_data
            return node.data
        else:  # если ближе с конца
            node = self._tail
            for x in range(un_index - 1):
                node = node.prev_data
            return node.data

    def __contains__(self, item: T) -> bool:  # получение сведений о наличии определённых значений через in
        node = self._head
        for x in range(self._length):
            if node.data == item:
                return True
            node = node.next_data
        return False

    def contains(self, item: T) -> bool:  # получение сведений о наличии определённых значений через точку
        node = self._head
        for x in range(self._length):
            if node.data == item:
                return True
            node = node.next_data
        return False

    def reverse(self) -> None:  # разворот списка
        temp = None
        current = self._head
        while current is not None:
            temp = current.prev_data
            current.prev_data = current.next_data
            current.next_data = temp
            current = current.prev_data
        if temp is not None:
            self._head = temp.prev_data

    def len(self) -> int:  # возвращает длину списка
        return self._length

    def is_empty(self) -> bool:  # возвращает, пустой ли список
        return self._length == 0

    def push_back(self, data: T) -> None:  # добавляет элемент в конец списка
        node = DoublyNode[T](data)
        if self._length <= 0:
            self._head = node
            self._tail = node
            self._length += 1
            return
        old_data = self._tail
        self._tail.next_data = node
        self._tail = node
        self._tail.prev_data = old_data
        self._length += 1
        return

    def push_beginning(self, data: T) -> None:  # добавляет элемент в начало
        node = DoublyNode[T](data)
        if self._length <= 0:
            self._head = node
            self._tail = node
            self._length += 1
            return
        old_data = self._head
        self._head.prev_data = node
        self._head = node
        self._head.next_data = old_data
        self._length += 1
        return

    @staticmethod
    def _insertion(data: T, node: DoublyNode[T]) -> None:  # вспомогательная функция для вставки по индексу
        new_node = DoublyNode[T](data)
        prev_node = node.prev_data
        prev_node.next_data = new_node
        new_node.prev_data = prev_node
        new_node.next_data = node
        node.prev_data = new_node
        return

    def insert(self, index: int, data: T) -> None:  # вставка по индексу
        if index > self._length or index < 0:  # можно вставить на первое место(0), на последнее место(length) и центр
            raise IndexOutOfRangeException
        if index == 0:
            self.push_beginning(data)
            return
        elif index == self._length:
            self.push_back(data)
            return
        else:
            un_index = self._length - index
            if index <= un_index:  # если ближе с начала
                node = self._head
                for x in range(index):
                    node = node.next_data
                self._insertion(data, node)
                self._length += 1
                return
            else:  # если ближе с конца
                node = self._tail
                for x in range(un_index - 1):
                    node = node.prev_data
                self._insertion(data, node)
                self._length += 1
                return

    @staticmethod
    def _deleting(node: DoublyNode[T]):  # дополнительная функция для удаления по индексу
        prev_node = node.prev_data
        next_node = node.next_data
        prev_node.next_data = next_node
        next_node.prev_data = prev_node

    def delete(self, index: int) -> None:  # функция для удаления по индексу
        if index >= self._length or index < 0:  # можно удалить первое место(0), на последнее место(length - 1) и центр
            raise IndexOutOfRangeException
        if index == 0:
            node = self._head.next_data
            node.prev_data = None
            self._head = node
            self._length -= 1
            return
        elif index == self._length - 1:
            node = self._tail.prev_data
            node.next_data = None
            self._tail = node
            self._length -= 1
            return
        else:
            un_index = self._length - index
            if index <= un_index:  # если ближе с начала
                node = self._head
                for x in range(index):
                    node = node.next_data
                self._deleting(node)
                self._length -= 1
                return
            else:  # если ближе с конца
                node = self._tail
                for x in range(un_index - 1):
                    node = node.prev_data
                self._deleting(node)
                self._length -= 1
                return

    def instead(self, index, data):
        self.delete(index)
        self.insert(index, data)
