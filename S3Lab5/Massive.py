import ctypes
from typing import TypeVar, Generic, Union

T = TypeVar("T")


class IndexOutRangeException(Exception):
    pass


class NotSortedException(Exception):
    pass


class DynamicArray(Generic[T]):

    def __init__(self, capacity: int) -> None:
        self._length: int = 0
        self._capacity: int = capacity
        self._arr: ctypes.Array[T] = (capacity * ctypes.py_object)()

    def get_length(self) -> int:
        return self._length

    def get_capacity(self) -> int:
        return self._capacity

    def _resize(self, new_capacity: int) -> None:
        new_array: ctypes.Array[T] = (new_capacity * ctypes.py_object)()
        for it in range(self._length):
            new_array[it] = self._arr[it]

        self._arr = new_array
        self._capacity = new_capacity

    def _check_range(self, index: int) -> bool:
        if index >= self._length or index < 0:
            return False
        return True

    def is_empy(self) -> bool:
        return self._length == 0

    def add(self, element: T) -> None:
        if self._length == self._capacity:
            self._resize(self._capacity * 2)

        self._arr[self._length] = element
        self._length += 1

    def get(self, index: int) -> T:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("-_-")

        return self._arr[index]

    def remove(self, index: int) -> bool:
        ok: bool = self._check_range(index)
        if not ok:
            return False

        for i in range(index, self._length - 1):
            self._arr[i] = self._arr[i + 1]
        self._length -= 1
        return ok

    def __len__(self):
        return self.get_length()

    def put(self, index: int, element: T) -> bool:
        ok: bool = self._check_range(index)
        if not ok:
            return False

        self._arr[index] = element
        return ok

    def __str__(self) -> str:
        my_str: str = "["
        for it in range(self._length):
            if it != self._length - 1:
                my_str += str(self._arr[it]) + " "
            else:
                my_str += str(self._arr[it])
        my_str += "]"
        return my_str

    def __setitem__(self, index: int, value: T) -> None:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("-_-")
        self._arr[index] = value

    def __getitem__(self, index: int) -> T:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("-_-")
        return self._arr[index]

    # ==================================================================================================

    @staticmethod
    def _comparator(a: Union[int, float, str], b: Union[int, float, str], sign: str) -> bool:
        if sign == "<":
            return a < b
        elif sign == ">":
            return a > b

    def gnome_up_author_sort(self):  # ГНОМЬЯ СОРТИРОВКА ПО ПОЛЮ АВТОР ПО ВОЗРАСТАНИЮ

        new_array: DynamicArray = DynamicArray(1)
        for x in range(len(self)):
            new_array.add(self[x])

        if len(new_array) == 0:
            raise ValueError("array is empty")

        def swap(jj: int, j: int):
            new_array[jj], new_array[j] = new_array[j], new_array[jj]

        i = 1
        while i < len(new_array):
            if new_array._comparator(new_array[i].author, new_array[i - 1].author, ">"):
                i += 1
            else:
                swap(i, i - 1)
                if i > 1:
                    i -= 1
        return new_array

    def insertion_up_cost_sort(self):  # сортировка вставками по возрастанию по цене
        new_array: DynamicArray = DynamicArray(1)
        for x in range(len(self)):
            new_array.add(self[x])

        if len(new_array) == 0:
            raise ValueError("array is empty")

        for i in range(1, len(new_array)):
            temp = new_array[i]
            it = i
            while it > 0 and new_array._comparator(new_array[it - 1].cost, temp.cost, "<"):
                new_array[it] = new_array[it - 1]
                it -= 1
            new_array[it] = temp
        return new_array

    def _is_sorted_up_pages(self):
        for x in range(1, len(self)):
            if self[x - 1].pages > self[x].pages:
                return False
        return True

    def interpolation_search(self, x: int) -> int:

        if x < self[0].pages or x > self[len(self) - 1].pages:
            raise ValueError("Not Found")

        if not (self._is_sorted_up_pages()):
            raise NotSortedException("Not sorted!")

        high = len(self) - 1
        low = 0

        while (self[high].pages != self[low].pages and
               self[low].pages <= x <= self[high].pages):
            pos = low + int((high - low) / (self[high].pages - self[low].pages) * (x - self[low].pages))
            if self[pos].pages == x:
                return pos
            elif self[pos].pages < x:
                low = pos + 1
            else:
                high = pos - 1

        raise ValueError("Not Found")

    def gnome_up_pages_sort(self):  # ГНОМЬЯ СОРТИРОВКА ПО ПОЛЮ АВТОР ПО ВОЗРАСТАНИЮ

        new_array: DynamicArray = DynamicArray(1)
        for x in range(len(self)):
            new_array.add(self[x])

        if len(new_array) == 0:
            raise ValueError("array is empty")

        def swap(jj: int, j: int):
            new_array[jj], new_array[j] = new_array[j], new_array[jj]

        i = 1
        while i < len(new_array):
            if new_array._comparator(new_array[i].pages, new_array[i - 1].pages, ">") or new_array[i].pages == \
                    new_array[i - 1].pages:
                i += 1
            else:
                swap(i, i - 1)
                if i > 1:
                    i -= 1
        return new_array
