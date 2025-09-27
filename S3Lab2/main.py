# Вариант 7: Двусвязанный список, Стек
from DubblyLinkedList import *
from Stek import *
import time


def printdubblylist(obj: DubblyLinkedList) -> None:  # печать списка с его длинной
    print(obj, obj.len())
    return


def stek_test(seq: str) -> bool:  # функция, использующая стек для решения скобок
    obj = Stek()
    t = {"]": "[", "}": "{", ")": "("}
    for xx in seq:
        if xx == "[" or xx == "{" or xx == "(":
            obj.push(xx)
        elif obj.get_data() == t[xx]:
            obj.pop()
        elif (xx == ")" or xx == "}" or xx == "]") and obj.len() == 0:
            return False
    if obj.len() == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    # тестирование двусвязанного списка
    print("***Тестирование двусвязного списка***")
    mas = DubblyLinkedList()  # тест функции push_back, push_beginning и len
    mas.push_back("a")
    printdubblylist(mas)
    mas.push_beginning("b")
    printdubblylist(mas)
    mas.push_back("c")
    printdubblylist(mas)
    mas.push_beginning("d")
    printdubblylist(mas)

    print(mas[0], mas[1], mas[2], mas[3])  # тестирование доступа по индексу
    # print(mas[-1])  # выход за пределы
    # print(mas[4])  # выход за пределы

    print("a:", "a" in mas, "b:", "b" in mas, "c:", "c" in mas, "d:", "d" in mas, "e:", "e" in mas)  # тестирование in

    mas.insert(0, "e")  # тестирование insert
    printdubblylist(mas)
    mas.insert(3, "f")
    printdubblylist(mas)
    mas.insert(6, "g")
    printdubblylist(mas)
    # mas.insert(-1, "a")  # выход за пределы
    # mas.insert(7, "a")  # выход за пределы

    mas.delete(0)  # тестирование удаления
    printdubblylist(mas)
    mas.delete(5)
    printdubblylist(mas)
    mas.delete(3)
    printdubblylist(mas)
    # mas.delete(-1)  # выход за пределы
    # mas.delete(10)  # выход за пределы
    mas.reverse()  # реверс
    print(mas)
    mas.insert(1, "g")  # Вставка после ревёрса работает -> сохранена полная работоспособность
    print(mas)

    # тестирование стека
    print("***Тестирование стека***")
    stk = Stek()
    stk.push('a')  # тест функции push и __str__
    stk.push('b')
    stk.push('c')
    print(stk)
    print(stk.pop())  # тест функции pop
    print(stk)
    print(stk.len())  # тест функции len
    print(stk.get_data())  # тест функции get_data
    print(stek_test("{}"))

    print("***Бенчмарк***")
    zig = 10
    # бенчмарк
    k = Stek()
    for x in range(zig):
        k.push(x)
    t0 = time.time()
    for x in range(zig):
        k.pop()
    t1 = time.time() - t0
    print(t1)

