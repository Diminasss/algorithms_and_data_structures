from typing import Generic, TypeVar, Optional, Union, IO
from dataclasses import dataclass
from Student import Student

T = TypeVar('T')


class EmptyTreeException(Exception):
    pass


class KeyIsAlreadyExistException(Exception):
    pass


class KeyNotFoundException(Exception):
    pass


# Нода бинарного дерева поиска
@dataclass
class BinarySearchTreeNode(Generic[T]):
    data: T
    right: Optional['BinarySearchTreeNode[T]'] = None
    left: Optional['BinarySearchTreeNode[T]'] = None

    # Получить ключ из класса
    def key(self) -> Union[int, float]:
        return self.data.key


# Класс бинарного дерева поиска
def _get_successor(del_node: BinarySearchTreeNode[T]) -> BinarySearchTreeNode[T]:
    # Метод возвращает узел со следующим значением после удаляемого
    # сначала осуществляется переход к правому потомку, а затем
    # отслеживается цепочка левых потомков данного узла
    successor_parent = del_node
    successor = del_node
    current_node = del_node.right
    # Переход к правому потомку
    while current_node is not None:  # Пока остаются левые потомки
        successor_parent = successor
        successor = current_node
        current_node = current_node.left

    if successor != del_node.right:
        # Если преемник не является правым потомком создаются связи между узлами
        successor_parent.left = successor.right
        successor.right = del_node.right

    return successor


class BinarySearchTree(Generic[T]):
    # конструктор бинарного дерева поиска
    def __init__(self) -> None:
        self._length: int = 0
        self._root: Optional['BinarySearchTreeNode[T]'] = None

    # узнать, пустое ли дерево поиска
    def is_empty(self) -> bool:  # протестировано
        return self._length == 0

    # узнать размер дерева поиска
    def get_size(self) -> int:  # протестировано
        return self._length

    # добавить элемент в дерево поиска
    def add(self, value: T) -> None:
        new_node: BinarySearchTreeNode[T] = BinarySearchTreeNode(data=value)
        if self._length == 0:
            self._root = new_node
            self._length += 1
        else:
            current_node = self._root
            while True:
                parent: Optional[BinarySearchTreeNode[T]] = current_node
                # сдвиг влево
                if new_node.key() < current_node.key():
                    current_node = current_node.left
                    if current_node is None:
                        if parent.key() != new_node.key():
                            parent.left = new_node
                            self._length += 1
                            return
                        else:
                            raise KeyIsAlreadyExistException(f'''KeyIsAlreadyExist "{parent.key()}"''')
                # сдвиг вправо
                else:
                    current_node = current_node.right
                    if current_node is None:
                        if parent.key() != new_node.key():
                            parent.right = new_node
                            self._length += 1
                            return
                        else:
                            raise KeyIsAlreadyExistException(f'''KeyIsAlreadyExist "{parent.key()}"''')

    # dunder метод печати дерева бинарного поиска
    def __str__(self) -> str:
        result: list[str] = ["Дерево бинарного поиска\n"]
        if not self.is_empty():
            self.__create_str_tree(result, "", self._root, True)
        else:
            result = ['Пустое дерево']
        return "".join(result)

    # вспомогательная функция для получения функционального программирования и сокращения кода методом рекурсии
    def __create_str_tree(self, result: list[str], prefix: str, node: Optional[BinarySearchTreeNode[T]], is_tail: bool):
        if node.right is not None:
            new_prefix = prefix
            if is_tail:
                new_prefix += "│   "
            else:
                new_prefix += "    "
            self.__create_str_tree(result, new_prefix, node.right, False)

        result.append(prefix)
        if is_tail:
            result.append("└── ")
        else:
            result.append("┌── ")
        result.append(str(node.key()) + "\n")

        if node.left is not None:
            new_prefix = prefix
            if is_tail:
                new_prefix += "    "
            else:
                new_prefix += "│   "
            self.__create_str_tree(result, new_prefix, node.left, True)

    # Функция находит значение по ключу, если ключа нет, то возвращает None. Наводится на корень дерева, далее
    # сравнивает значение искомого значения со значением узла, если искомое больше значения, то движемся вправо,
    # меньше - влево. Когда искомое равно значению узла, возвращаются данные, записанные в узел.
    def find(self, key: Union[int, float]) -> Optional[T]:
        if self.is_empty():
            raise EmptyTreeException
        current_node: Optional['BinarySearchTreeNode'] = self._root
        while current_node.key() != key:
            if current_node.key() > key:
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node is None:
                return None
        return current_node.data

    # Делает то же самое, что и предыдущая функция, только возвращает False и True
    def __contains__(self, key: Union[int, float]) -> bool:
        if self.is_empty():
            raise EmptyTreeException
        current_node: Optional['BinarySearchTreeNode'] = self._root
        while current_node.key() != key:
            if current_node.key() > key:
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node is None:
                return False
        return True

    # Удаление по ключу.
    def remove(self, key: int | float) -> None:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")

        current_node = self._root
        parent_node = self._root
        is_left_node: bool = True
        while current_node.key() != key:
            parent_node = current_node
            if key < current_node.key():
                is_left_node = True
                current_node = current_node.left
            else:
                is_left_node = False
                current_node = current_node.right
            if current_node is None:
                raise KeyNotFoundException(f"KeyNotFoundException: {key}")

        # Если узел не имеет потомков, он просто удаляется
        if current_node.left is None and current_node.right is None:
            if current_node == self._root:
                self._root = None
            elif is_left_node:
                parent_node.left = None
            else:
                parent_node.right = None
        elif current_node.right is None:
            # Если нет правого потомка, узел заменяется левым поддеревом
            if current_node == self._root:
                self._root = current_node.left
            elif is_left_node:
                parent_node.left = current_node.left
            else:
                parent_node.right = current_node.left
        elif current_node.left is None:
            # Если нет левого потомка, узел заменяется правым поддеревом
            if current_node == self._root:
                self._root = current_node.right
            elif is_left_node:
                parent_node.left = current_node.right
            else:
                parent_node.right = current_node.right
        else:
            # Два потомка, узел заменяется преемником
            successor = _get_successor(current_node)
            # Родитель currentNode связывается с посредником
            if current_node == self._root:
                self._root = successor
            elif is_left_node:
                parent_node.left = successor
            else:
                parent_node.right = successor
            successor.left = current_node.left
        self._length -= 1

    # Получает на вход имя файла, производит симметричный обход с помощью рекурсии, создаёт файл с расширением
    # txt в папке с main.py
    def save_to_txt(self, file_name: str) -> None:
        if self.is_empty():
            raise EmptyTreeException("EmptyTreeException")
        file: IO[str] = open(f"{file_name}.txt", mode='w', encoding="utf-8")
        self._symmetric_save(self._root, file)
        file.close()
        print("Дерево успешно сохранено в файл")

    # вспомогательная функция для предыдущей
    def _symmetric_save(self, local_root: Optional[BinarySearchTreeNode[T]], file_to_save: IO[str]) -> None:
        if local_root is not None:
            data: str = (f'{local_root.data.key}\n{local_root.data.fio}\n{local_root.data.group_number}\n'
                         f'{local_root.data.course}\n{local_root.data.age}\n')
            file_to_save.write(data)
            self._symmetric_save(local_root.left, file_to_save)
            self._symmetric_save(local_root.right, file_to_save)

    # Получает на вход путь к файлу, считывает из него значения и создаёт бинарное дерево поиска, заполненное данными,
    # дозапись невозможна
    def read_txt(self, file_path: str):
        file: IO[str] = open(file_path, 'r')
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
                self.add(Student(fio, group_number, course, age, key))
                k = -1
        file.close()
