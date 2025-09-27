from typing import Generic, TypeVar, Callable, IO
from DubblyLinkedList import DoublyLinkedList
from Student import Student
# добавить сохранение в файл и 2 варианта проверки вхождения
T = TypeVar('T')


class EmptyHeapException(Exception):
    pass


class IndexOutOfRangeException(Exception):
    pass


class MaxHeap(Generic[T]):
    def __init__(self, comp: Callable[[T, T], bool] = lambda a, b: a.key < b.key) -> None:
        self._length: int = 0
        self.comp: Callable[[T, T], bool] = comp
        self._list: DoublyLinkedList[T] = DoublyLinkedList()

    # Функция вывода структуры через print
    def __str__(self) -> str:
        if self.is_empty():
            return 'Пустая куча'
        result: str = '['
        for x in range(self._length):
            result += f'{self._list[x].key}, '
            if x == self._length - 1:
                result = result[:-2]
                result += ']'
        print(result)
        result = ''

        n_blanks, items_per_row, column, j = (32, 1, 0, 0)
        dots: str = 32 * "."
        result += f"{dots * 2}\n"
        while self._length > 0:
            if column == 0:
                for it in range(0, n_blanks):
                    result += " "

            result += f"{self._list[j].key} "
            j += 1
            if j >= self._length:
                break

            column += 1
            if column == items_per_row:
                # Конец строки
                n_blanks //= 2  # Половина пробелов
                items_per_row *= 2  # Вдвое больше элементов
                column = 0  # Начать заново
                result += "\n"  # Переход на новую строку
            else:
                for it in range(0, n_blanks * 2 - 2):
                    result += " "
        result += f"\n{dots * 2}\n"
        return result

    # функция создания кучи из списка
    def create_heap_from_list(self, doubly_linked_list: DoublyLinkedList[T] | list[T]) -> None:
        for x in range(0, doubly_linked_list.len()):
            self.insert(doubly_linked_list[x])

    # статичный метод для сравнения двух ключей
    @staticmethod
    def _comparator(a: T, b: T) -> bool:
        return a.key < b.key

    # добавление в кучу
    def insert(self, value: T) -> None:
        self._list.insert(self._length, value)
        self._trickle_up(self._length)
        self._length += 1

    # продолжение добавления в кучу
    def _trickle_up(self, index: int) -> None:
        if (index - 1) // 2 >= 0:
            parent: int = (index - 1) // 2
            bottom: T = self._list[index]
            while index > 0 and self._comparator(self._list[parent], bottom) and parent >= 0:
                self._list.instead(index, self._list[parent])
                index = parent
                parent = (parent - 1) // 2
            self._list.instead(index, bottom)

    # удаление предмета из кучи по ключу
    def delete(self, index: float | int) -> int:
        how_many_was_deleted: int = self.how_much_is_in_heap(index)
        for x in range(how_many_was_deleted):
            self._delete(index)
        return how_many_was_deleted

    def _delete(self, index: float | int) -> None:
        if self.is_empty():
            raise EmptyHeapException("EmptyHeapException")
        for x in range(self._length):
            if self._list[x].key == index:
                self._list.delete(x)
                self._trickle_down(0)
                self._length -= 1
                return
        return

    # продолжение удаления предмета из кучи по ключу
    def _trickle_down(self, index: int):
        large_child: int = 0
        top: T = self._list[index]
        while index < self._length // 2:
            left_child: int = 2 * index + 1
            right_child: int = left_child + 1
            if right_child < self._length and self._comparator(self._list[large_child], self._list[right_child]):
                large_child = right_child
            else:
                large_child = left_child
            if not self._comparator(top, self._list[large_child]):
                break
            self._list.instead(index, self._list[large_child])
            index = large_child
        self._list.instead(index, top)

    # найти все совпадающие с введённым подходящие ключи в куче
    def find(self, index: int | float) -> DoublyLinkedList:
        mas: DoublyLinkedList = DoublyLinkedList()
        for x in range(self._length):
            if self._list[x].key == index:
                mas.push_back(self._list[x])
        if mas.is_empty():
            raise IndexOutOfRangeException('IndexOutOfRangeException')
        else:
            return mas

    # если в куче есть хоть один совпадающий элемент с введённым, то возвращается True
    def __contains__(self, index: int | float) -> bool:
        for x in range(self._length):
            if self._list[x].key == index:
                return True
        return False

    # сколько в куче ключей, совпадающих с введённым
    def how_much_is_in_heap(self, index: int | float) -> int:
        k: int = 0
        for x in range(self._length):
            if self._list[x].key == index:
                k += 1
        return k

    # возвращает, пустая ли куча
    def is_empty(self) -> bool:
        return self._length == 0

    # позволяет получить максимальное значение в куче за O(1)
    def get_max(self) -> T:
        if self.is_empty():
            raise EmptyHeapException('EmptyHeapException')
        return self._list[0]

    # возвращает размер кучи
    def get_size(self) -> int:
        return self._length

    # получает название файла, создаёт txt файл в папке с main.py, записывает туда содержание кучи
    def save_to_txt(self, file_name: str) -> None:
        if self.is_empty():
            raise EmptyHeapException("EmptyHeapException")
        file: IO[str] = open(f"{file_name}.txt", mode='w', encoding="utf-8")
        for x in range(self._length):
            data: str = (f'{self._list[x].key}\n{self._list[x].fio}\n{self._list[x].group_number}\n'
                         f'{self._list[x].course}\n{self._list[x].age}\n')
            file.write(data)
        file.close()
        print("Куча успешно сохранена в файл")

    # получает путь к файлу, считывает из файла и создаёт кучу
    def read_txt(self, file_path: str):
        file: IO[str] = open(file_path, 'r', encoding="utf-8")
        k: int = -1
        for line in file:
            k += 1
            if k == 0:
                if "." in line:
                    key: float = float(line)
                else:
                    key: int = int(line)
            elif k == 1:
                fio: str = str(line)
            elif k == 2:
                group_number: int = int(line)
            elif k == 3:
                course: int = int(line)
            elif k == 4:
                age: int = int(line)
                self.insert(Student(fio, group_number, course, age, key))
                k = -1
        file.close()
