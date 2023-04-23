"""Реализация абстрактного класса, который обязывает реализовать методы для добавления вакансий в файл,
получения данных из файла по указанным критериям"""
from abc import ABC, abstractmethod


class Saver(ABC):

    @abstractmethod
    def save_in_file(self, resource=None):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary_input):
        pass

    @abstractmethod
    def search_words(self, search_words):
        pass

    @abstractmethod
    def json_results(self):
        pass

