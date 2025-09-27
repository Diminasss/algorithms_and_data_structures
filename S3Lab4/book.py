from typing import Generic, TypeVar

T = TypeVar('T')


class Book(Generic[T]):
    def __init__(self, author: str, publishing_house: str, pages: int, cost: int | float, isbn: str) -> None:
        self.author: str = author
        self.publishing_house: str = publishing_house
        self.pages: int = pages
        self.cost: int | float = cost
        self.isbn: str = isbn

    def __str__(self) -> str:
        return (f"\nАвтор: {self.author}, "
                f"Издательство: {self.publishing_house}, "
                f"Количество страниц {self.pages}, "
                f"Цена: {self.cost}, "
                f"ISBN: {self.isbn}")
