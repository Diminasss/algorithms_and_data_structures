from typing import Generic, TypeVar, Union


T = TypeVar('T')


class Student(Generic[T]):
    def __init__(self, fio: str, group_number: int, course: int, age: int, average_mark: Union[int, float]) -> None:
        self.fio = fio
        self.group_number = group_number
        self.course = course
        self.age = age
        self.key = average_mark

    def __str__(self) -> str:
        return (f"_____-----Студент-----_____\n"
                f"ФИО: {self.fio}\n"
                f"Номер группы: {self.group_number}\n"
                f"Курс: {self.course}\n"
                f"Возраст: {self.age}\n"
                f"Средний балл: {self.key}\n")
