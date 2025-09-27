# 26 % 20 + 1 = 7 (3, 11 = [Гномья + Автор, Подсчётом - кол-во страниц], [Вставками + стоимость, Слиянием - Автор])
from DubblyLinkedList import DoublyLinkedList
from Massive import DynamicArray
from book import Book
from time import time
from faker import Faker
from random import randint

l_list = DoublyLinkedList()
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

print("______Сортировка слиянием списка по полю автор по убыванию______\n", l_list.merge_down_author_sort())
print("______Сортировка подсчётом списка по полю страницы по убыванию______\n", l_list.counting_down_pages_sort())
print("______Несортированный список после сортировки______\n", l_list)

a_array = DynamicArray(10)
a_array.add(Book("Петров", "Мнемозина", 2, 1000, "1"))
a_array.add(Book("Иванов", "Мнемозина", 125, 15, "2"))
a_array.add(Book("Сидоров", "Мнемозина", 125, 10, "3"))
a_array.add(Book("Kant", "Мнемозина", 10, 115, "4"))
a_array.add(Book("Салагаев", "Мнемозина", 25, 150, "5"))
a_array.add(Book("Попов", "Мнемозина", 221, 1000, "1"))
a_array.add(Book("Лисевский", "Мнемозина", 103, 15, "2"))
a_array.add(Book("Пупкин", "Мнемозина", 44, 10, "3"))
a_array.add(Book("Potter", "Мнемозина", 11, 115, "4"))
a_array.add(Book("Smith", "Мнемозина", 1001, 150, "5"))
print("______Сортировка вставками списка по полю цена по возрастанию______\n", a_array.insertion_up_cost_sort())
print("______Сортировка гномья списка по полю автор по возрастанию______\n", a_array.gnome_up_author_sort())
print("______Несортированный массив после сортировки______\n", a_array)

count = 247  # количество элементов в структуре
benchmark_array = DynamicArray(count)
fake = Faker(locale='RU')

print("______Заполнение массива______\n")
for x in range(count):
    benchmark_array.add(Book(fake.name(), 'Мнемозина', randint(10, 1000), randint(100, 10000) / 10,
                             fake.numerify(text='%%%-%-%%%%-%%%%-%%%-%%')))
print(f"______Массив заполнен на {len(benchmark_array)} элементов______\n")

print("______Начало гномьей сортировки______\n")
timer = time()
a = benchmark_array.gnome_up_author_sort()
print(f"______Гномья сортировка окончена за {time() - timer} мс______\n")

print("______Начало сортировки вставками______\n")
timer = time()
a = benchmark_array.insertion_up_cost_sort()
print(f"______Cортировка вставками окончена за {time() - timer} мс______\n")

count = 247  # количество элементов в структуре
benchmark_list = DoublyLinkedList()
fake = Faker(locale='RU')

print("______Заполнение списка______\n")
for x in range(count):
    benchmark_list.push_back(Book(fake.name(), 'Мнемозина', randint(10, 1000), randint(100, 10000) / 10,
                                  fake.numerify(text='%%%-%-%%%%-%%%%-%%%-%%')))
print(f"______Список заполнен на {len(benchmark_list)} элементов______\n")

print("______Начало сортировки подсчётом______\n")
timer = time()
a = benchmark_list.counting_down_pages_sort()
print(f"______Cортировка подсчётом окончена за {time() - timer} мс______\n")

print("______Начало сортировки слиянием______\n")
timer = time()
a = benchmark_list.merge_down_author_sort()
print(f"______Cортировка слиянием окончена за {time() - timer} мс______\n")
