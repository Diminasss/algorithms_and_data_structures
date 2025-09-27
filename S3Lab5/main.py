# 26 % 20 + 1 = 7:
# 3 - двусвязный список поиск Фибоначчи по количеству страниц
# 11 - массив интерполяционный поиск по количеству страниц
import DubblyLinkedList
import Massive
from DubblyLinkedList import DoublyLinkedList
from Massive import DynamicArray
from book import Book
from faker import Faker
from random import randint
from time import time


def fab(text: str) -> str:
    a: str = "_" * 10
    return "\n" + a + text + a


if __name__ == '__main__':
    l_list: DoublyLinkedList = DoublyLinkedList()
    l_list.push_back(Book("Петров", "Мнемозина", 2, 1000, "1"))
    l_list.push_back(Book("Иванов", "Мнемозина", 125, 15, "2"))
    l_list.push_back(Book("Сидоров", "Мнемозина", 125, 10, "3"))
    l_list.push_back(Book("Kant", "Мнемозина", 10, 115, "4"))
    l_list.push_back(Book("Салагаев", "Мнемозина", 25, 150, "5"))
    l_list.push_back(Book("Попов", "Мнемозина", 221, 1000, "1"))
    l_list.push_back(Book("Лисевский", "Мнемозина", 103, 15, "2"))
    l_list.push_back(Book("Пупкин", "Мнемозина", 44, 10, "3"))
    l_list.push_back(Book("Potter", "Мнемозина", 11, 115, "4"))
    l_list.push_back(Book("Smith", "Мнемозина", 1001, 150, "5"))

    print("\033[34m\033[3m" + fab("Проверка поиска Фибоначчи в списке по количеству страниц. Выбрана сортировка "
                                  "подсчётом по возрастанию" + "\033[0m"))
    print(fab("Работа поиска, если список не отсортирован"))
    try:
        print(l_list.fibonacci_search(11))
    except DubblyLinkedList.NotSortedException:
        print("Ошибка из-за того, что список не отсортирован")

    l_list = l_list.counting_up_pages_sort()  # Список отсортирован

    print(fab("Проверка работы поиска на отсортированном списке существующим значением"))

    print("Ожидаемый результат: 2\nРезультат:", l_list.fibonacci_search(11))

    print(fab("Проверка работы поиска слишком маленьким значением"))
    try:
        print(l_list.fibonacci_search(1))
    except ValueError:
        print("Слишком маленькое значение")

    print(fab("Проверка работы поиска слишком большим значением"))
    try:
        print(l_list.fibonacci_search(1111111111111))
    except ValueError:
        print("Слишком большое значение")

    print(fab("Проверка работы поиска не большим, не маленьким, но не входящим элементом"))
    try:
        print(l_list.fibonacci_search(12))
    except ValueError:
        print("Элемент не найден")

    d_array = DynamicArray(10)
    d_array.add(Book("Петров", "Мнемозина", 2, 1000, "1"))
    d_array.add(Book("Иванов", "Мнемозина", 125, 15, "2"))
    d_array.add(Book("Сидоров", "Мнемозина", 125, 10, "3"))
    d_array.add(Book("Kant", "Мнемозина", 10, 115, "4"))
    d_array.add(Book("Салагаев", "Мнемозина", 25, 150, "5"))
    d_array.add(Book("Попов", "Мнемозина", 221, 1000, "1"))
    d_array.add(Book("Лисевский", "Мнемозина", 103, 15, "2"))
    d_array.add(Book("Пупкин", "Мнемозина", 44, 10, "3"))
    d_array.add(Book("Potter", "Мнемозина", 11, 115, "4"))
    d_array.add(Book("Smith", "Мнемозина", 1001, 150, "5"))

    print("\033[34m\033[3m" + fab("Проверка интерполяционного поиска в массиве по количеству страниц. Выбрана "
                                  "гномья сортировка по возрастанию" + "\033[0m"))
    print(fab("Работа поиска, если массив не отсортирован"))
    try:
        print(d_array.interpolation_search(11))
    except Massive.NotSortedException:
        print("Ошибка из-за того, что массив не отсортирован")

    d_array = d_array.gnome_up_pages_sort()  # массив отсортирован

    print(fab("Проверка работы поиска на отсортированном массиве существующим значением"))

    print("Ожидаемый результат: 2\nРезультат:", d_array.interpolation_search(11))

    print(fab("Проверка работы поиска слишком маленьким значением"))
    try:
        print(d_array.interpolation_search(1))
    except ValueError:
        print("Слишком маленькое значение")

    print(fab("Проверка работы поиска слишком большим значением"))
    try:
        print(d_array.interpolation_search(1111111111111))
    except ValueError:
        print("Слишком большое значение")

    print(fab("Проверка работы поиска не большим, не маленьким, но не входящим элементом"))
    try:
        print(d_array.interpolation_search(12))
    except ValueError:
        print("Элемент не найден")

    print("\033[34m\033[3m" + fab("__________Бенчмарки__________") + "\033[0m")

fake: Faker = Faker(locale='RU')
quantity_list: int = 10000
quantity_array: int = 10000
benchmark_list: DoublyLinkedList = DoublyLinkedList()
benchmark_array: DynamicArray = DynamicArray(quantity_array)
pages: int = 0

print(fab("______Заполнение списка______"))
timer1 = time()
for x in range(quantity_list):
    pages = randint(10, 1000)
    benchmark_list.push_back(Book(author=fake.name(), publishing_house='Мнемозина', pages=pages,
                                  cost=randint(100, 10000) / 10, isbn=fake.numerify(text='%%%-%-%%%%-%%%%-%%%-%%')))
timer2 = time()
print("Список заполнен на", len(benchmark_list), "элементов")

print(fab("Сортировка списка"))
timer3 = time()
benchmark_list = benchmark_list.counting_up_pages_sort()
timer4 = time()
print("Список отсортирован")

print(fab('Поиск элемента'))
timer5 = time()
place = benchmark_list.fibonacci_search(pages)
timer6 = time()
print("Место элемента:", place)
print(fab(f"Результаты теста List на {len(benchmark_list)} элементов"))
print(f"Заполнение:          {timer2 - timer1} мс\n"
      f"Сортировка подсчётом:{timer4 - timer3} мс\n"
      f"Поиск Фибоначчи:     {timer6 - timer5} мс\n"
      f"Всего:               {(timer2 - timer1) + (timer4 - timer3) + (timer6 - timer5)} мс")

print(fab("______Заполнение массива______"))
timer1 = time()
for x in range(quantity_array):
    pages = randint(10, 1000)
    benchmark_array.add(Book(author=fake.name(), publishing_house='Мнемозина', pages=pages,
                             cost=randint(100, 10000) / 10, isbn=fake.numerify(text='%%%-%-%%%%-%%%%-%%%-%%')))
timer2 = time()
print("Массив заполнен на", len(benchmark_array), "элементов")

print(fab("Сортировка массива"))
timer3 = time()
benchmark_array = benchmark_array.gnome_up_pages_sort()
timer4 = time()
print("Список отсортирован")

print(fab('Поиск элемента'))
timer5 = time()
place = benchmark_array.interpolation_search(pages)
timer6 = time()
print("Место элемента:", place)
print(fab(f"Результаты теста Array на {len(benchmark_array)} элементов"))
print(f"Заполнение:            {timer2 - timer1} мс\n"
      f"Гномья сортировка:     {timer4 - timer3} мс\n"
      f"Интерполяционный поиск:{timer6 - timer5} мс\n"
      f"Всего:                 {(timer2 - timer1) + (timer4 - timer3) + (timer6 - timer5)} мс")
