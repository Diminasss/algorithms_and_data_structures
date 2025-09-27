from typing import Generic, TypeVar, Optional
from copy import deepcopy
from dataclasses import dataclass


class NotSortedException(Exception):
    pass


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
        self._element: Optional[DoublyNode[T]] = None
        self._element_number: Optional[int] = None

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

    def __len__(self) -> int:
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
    def _deleting(node: DoublyNode[T]) -> None:  # дополнительная функция для удаления по индексу
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

    def __setitem__(self, index: int, value: T) -> None:
        self.delete(index)
        self.insert(index, value)

    def __iter__(self):
        self._element_number = 0
        self._element = self._head
        return self

    def __next__(self) -> DoublyNode:
        if self._element_number == 0:
            self._element_number += 1
            return self._head
        elif self._element_number < self._length:
            self._element = self._element.next_data
            self._element_number += 1
            return self._element
        else:
            raise StopIteration

    def instead(self, index: int, data: DoublyNode):  # заменить одно значение на другое трудозатратый, но простой метод
        self.delete(index)
        self.insert(index, data)

    def _min_max(self) -> tuple[int, int]:  # найти максмальное и минимальное значение
        if len(self) == 0:
            raise ValueError("Лист пуст")

        a_min = float("inf")
        a_max = float("-inf")
        for v in self:
            v = v.data.pages
            if a_max < v:
                a_max = v
            if a_min > v:
                a_min = v
        return a_min, a_max

    def counting_down_pages_sort(self):  # сортировка подсчётом ПО УБЫВАНИЮ ПО СТРАНИЦАМ
        if len(self) == 0:
            raise ValueError("List is empty")

        a_min, a_max = self._min_max()

        list_counts = [list() for _ in range(a_max - a_min + 1)]

        for it in self:
            x = it.data.pages
            list_counts[x - a_min].append(it.data)

        new_list = DoublyLinkedList()
        for x in list_counts[-1::-1]:
            if len(x) == 0:
                pass
            else:
                for y in x:
                    new_list.push_back(y)

        return new_list

    def counting_up_pages_sort(self):  # сортировка подсчётом ПО УБЫВАНИЮ ПО СТРАНИЦАМ
        if len(self) == 0:
            raise ValueError("List is empty")

        a_min, a_max = self._min_max()

        list_counts = [list() for _ in range(a_max - a_min + 1)]

        for it in self:
            x = it.data.pages
            list_counts[a_max - x].append(it.data)

        new_list = DoublyLinkedList()
        for x in list_counts[-1::-1]:
            if len(x) == 0:
                pass
            else:
                for y in x:
                    new_list.push_back(y)

        return new_list

    def _merge_sort_impl(self, buffer: list[T], left: int, right: int) -> None:
        if left < right:
            m = (left + right) // 2

            self._merge_sort_impl(buffer, left, m)
            self._merge_sort_impl(buffer, m + 1, right)

            k, j = left, m + 1
            i = left
            while i <= m or j <= right:
                if j > right or (i <= m and self._comparator(self[i].author, self[j].author, ">")):
                    buffer[k] = self[i]
                    i += 1
                else:
                    buffer[k] = self[j]
                    j += 1
                k += 1
            for i in range(left, right + 1):
                self[i] = buffer[i]

    def merge_down_author_sort(self):  # СОРТИРОВКА СЛИЯНИЕМ ПО ПОЛЮ АВТОР ПО УБЫВАНИЮ

        if len(self) == 0:
            raise ValueError("array is empty")
        storage = deepcopy(self)
        buffer = [None for _ in range(len(self))]
        storage._merge_sort_impl(buffer, 0, len(self) - 1)
        return storage

    @staticmethod
    def _comparator(a, b, sign) -> bool:
        if sign == "<":
            return a < b
        elif sign == ">":
            return a > b

    # =========================================================================================

    def _is_sorted_up_pages(self) -> bool:
        for x in range(1, len(self)):
            if self[x - 1].pages > self[x].pages:
                return False
        return True

    def fibonacci_search(self, x: int) -> None | int:

        if not self._is_sorted_up_pages():
            raise NotSortedException("List is not sorted")

        if x < self[0].pages or x > self[len(self) - 1].pages:
            raise ValueError("Not Found")

        fm2 = 0
        fm1 = 1
        fm = fm1 + fm2
        offset = -1

        while fm < len(self):
            fm2 = fm1
            fm1 = fm
            fm = fm1 + fm2

        while fm > 1:
            i = min(offset + fm2, len(self) - 1)
            if self[i].pages < x:
                fm = fm1
                fm1 = fm2
                fm2 = fm - fm1
                offset = i
            elif self[i].pages > x:
                fm = fm2
                fm1 = fm1 - fm2
                fm2 = fm - fm1
            else:
                return i

        if fm1 == 1:
            if self[offset + 1].pages == x:
                return offset + 1

        raise ValueError("Not Found")
