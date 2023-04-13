"""Реализация абстрактного класса, который обязывает реализовать методы для добавления вакансий в файл,
получения данных из файла по указанным критериям и удаления информации о вакансиях."""
from abc import ABC, abstractmethod


class Saver(ABC):
    def __init__(self, data: list) -> None:
        self.data = data

    @abstractmethod
    def dump_to_file(self):
        pass

