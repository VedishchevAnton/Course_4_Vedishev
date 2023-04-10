"""Реализация абстрактного класса, который обязывает реализовать методы для добавления вакансий в файл,
получения данных из файла по указанным критериям и удаления информации о вакансиях."""
from abc import ABC, abstractmethod


class Saver(ABC):
    def __init__(self, data: list) -> None:
        self._data = data

    @abstractmethod
    def add_vacancies(self):
        pass

    @abstractmethod
    def data_file(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass
