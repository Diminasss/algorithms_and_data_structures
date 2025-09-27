#  29 % 20 + 1 = 10 - задания 3, 11 (двоичное дерево поиска, максимальная куча)
from Student import Student
from BinarySearchTree import BinarySearchTree
from DubblyLinkedList import DoublyLinkedList
from MaxHeap import MaxHeap
from time import time
from random import randint


def a(b: str) -> str:
    return f'_____ ----- {b} ----- _____'


if __name__ == '__main__':
    print(a('Тестирование дерева'))
    print(a('Тестирование функции __str__, is_empty, get_size и add'))
    Tree = BinarySearchTree()
    print("__str__", Tree)
    print('is_empty', Tree.is_empty())  # вывод до заполнения
    print("get_size", Tree.get_size())  # вывод до заполнения
    Tree.add(Student('Никитин Дмитрий Михайлович', 4217, 2, 18, 4))
    Tree.add(Student('Медянкина Анастасия Николаевна', 4217, 2, 19, 4.5))
    Tree.add(Student('Лебедев Владислав Альбертович', 4217, 2, 25, 4.2))
    Tree.add(Student('Наташа Македонова', 4217, 2, 19, 3))
    Tree.add(Student('Наташа Петрова', 4217, 2, 19, 4.6))
    Tree.add(Student("Маслов Андрей", 4217, 2, 19, 5))
    Tree.add(Student('Муравьёв Александр', 4217, 2, 19, 2))
    Tree.add(Student('Мазориев Умар', 4217, 2, 19, 3.3))
    Tree.add(Student('Даниил Кутергин', 4217, 2, 19, 3.7))
    try:
        Tree.add(Student('Даниил Кутергин', 4217, 2, 19, 3.7))  # добавить в дерево существующий ключ
    except:
        print('Добавить не получилось')
    Tree.add(Student('Ярошенко Михаил', 4217, 2, 19, 4.9))
    Tree.add(Student('Лавелина Алёна', 4217, 2, 19, 4.4))
    print('__str__', Tree)
    print('is_empty', Tree.is_empty())  # вывод после заполнения
    print('get_size', Tree.get_size())  # вывод после заполнения

    print(a('Тестирование __contains__ и find'))
    print("find", Tree.find(5))  # есть в дереве
    print('find', Tree.find(1))  # нет в дереве
    print('__contains__', 4.2 in Tree)  # есть в дереве
    print('__contains__', 1 in Tree)  # нет в дереве

    print(a('Тестирование remove'))
    Tree.remove(5)  # Удаление из середины
    Tree.remove(4)  # Удаление корня
    Tree.remove(3.7)  # Удаление конца ветки
    try:
        Tree.remove(1)  # удаление несуществующего
    except:
        print('Удаление не получилось')
    print(Tree)
    print(Tree.get_size())  # проверяем размер

    print(a('Тестирование save_to_txt и read_txt'))
    print(Tree)
    Tree.save_to_txt('Tree')  # сохраняем в файл
    Tree2 = BinarySearchTree()
    Tree2.read_txt('Tree.txt')  # считывание
    print(a('Второе дерево'))
    print(Tree2)
    try:
        Tree2.read_txt('Tree.txt')  # дозапись
    except:
        print('Дозапись не удалась')

    # создание массива со студентами
    mas = DoublyLinkedList()
    mas.push_back(Student('Никитин Дмитрий Михайлович', 4217, 2, 18, 4))
    mas.push_back(Student('Медянкина Анастасия Николаевна', 4217, 2, 19, 4.5))
    mas.push_back(Student('Лебедев Владислав Альбертович', 4217, 2, 25, 4.2))
    mas.push_back(Student('Наташа Македонова', 4217, 2, 19, 3))
    mas.push_back(Student('Наташа Петрова', 4217, 2, 19, 4.6))
    mas.push_back(Student("Маслов Андрей", 4217, 2, 19, 5))
    mas.push_back(Student('Муравьёв Александр', 4217, 2, 19, 2))
    mas.push_back(Student('Мазориев Умар', 4217, 2, 19, 3.3))
    mas.push_back(Student('Даниил Кутергин', 4217, 2, 19, 3.7))
    mas.push_back(Student('Ярошенко Михаил', 4217, 2, 19, 4.9))

    print(a("Тестирование кучи"))
    print(a('Тестирование create_heap_from_list, __str__, get_size, get_max, is_empty'))
    heap = MaxHeap()
    print('get_size', heap.get_size())
    try:
        print('get_max', heap.get_max())
    except:
        print('Получить максимальное не получилось')
    print('is_empty', heap.is_empty())
    print(heap)

    print(a("Создание кучи из двусвязного списка"))
    heap.create_heap_from_list(mas)
    print('get_size', heap.get_size())
    print('get_max', heap.get_max())
    print('is_empty', heap.is_empty())
    print(heap)

    print(a('Тестирование how_much_is_in_heap, insert'))
    print('how_much_is_in_heap', heap.how_much_is_in_heap(4.9))
    heap.insert(Student('Ярошенко Михаил', 4217, 2, 19, 4.9))
    print('how_much_is_in_heap', heap.how_much_is_in_heap(4.9))

    print(a("Тестирование __contains__ и find"))
    print(heap)
    print('__contains__', 4.9 in heap)
    print('__contains__', 1 in heap)
    print('find', heap.find(3))
    print('find', heap.find(4.9))
    try:
        print('find', heap.find(1))  # не существует такого элемента в куче
    except:
        print('Не удалось найти')
    print(a("Тестирование delete"))
    heap.delete(4.9)
    print(heap)

    heap.save_to_txt('Heap')
    heap2 = MaxHeap()
    heap2.read_txt("Heap.txt")
    print(heap2)

    # -------------------------------------------------------------------------------------

    print("\n\n", a('Тестирование бенчмарками BinarySearchTree'))
    quantity_of_keys = 1000
    testing_Bin_Tree = BinarySearchTree()

    # --------------------------------------------------------------------------------------
    print(a('Тестирование add. Включение случайных ключей в дерево'))
    datas = [y / 10 for y in range(0, quantity_of_keys)]
    random_datas = []
    for x in range(len(datas)):
        r = randint(0, len(datas) - 1)
        random_datas.append(datas[r])
        datas.pop(r)

    timer = time()
    for x in random_datas:
        testing_Bin_Tree.add(Student('fio', 1, 1, 1, x))
    print("Включено", testing_Bin_Tree.get_size(), "элементов за", time() - timer)
    # -------------------------------------------------------------------------------------
    print(a('Тестирование remove. Исключение случайных частей из дерева'))
    datas = [y / 10 for y in range(0, quantity_of_keys)]
    random_datas = []
    for x in range(len(datas)):
        r = randint(0, len(datas) - 1)
        random_datas.append(datas[r])
        datas.pop(r)

    timer = time()
    for x in random_datas:
        testing_Bin_Tree.remove(x)
    print("Удалено", quantity_of_keys, "элементов за", time() - timer)
    # -------------------------------------------------------------------------------------

    print("\n", a('Тестирование бенчмарками MaxHeap'))
    testing_max_heap = MaxHeap()
    quantity_of_keys = 1000  # количество ключей

    # -------------------------------------------------------------------------------------
    print(a('Тестирование add. Включение случайных ключей в кучу'))
    datas = []
    for x in range(quantity_of_keys):
        datas.append(Student('fio', 1, 1, 1, randint(0, 50) / 10))
    timer = time()
    for x in datas:
        testing_max_heap.insert(x)
    print("Включено", len(datas), "элементов за", time() - timer)
    # -------------------------------------------------------------------------------------
    print(a('Тестирование delete. Удаление случайных ключей из кучи'))
    s = [x / 10 for x in range(0, 51)]
    datass = []
    for x in range(len(s)):
        r = randint(0, len(s)) - 1
        datass.append(r)
        s.pop(r)
    timer = time()
    for x in datass:
        testing_max_heap.delete(x)
    print("Удалено", len(datas), "элементов за", time() - timer)
