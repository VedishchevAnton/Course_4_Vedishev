"""Реализация абстрактного класса, который обязывает реализовать методы для добавления вакансий в файл,
получения данных из файла по указанным критериям и удаления информации о вакансиях."""
from abc import ABC, abstractmethod


class Saver(ABC):

    @abstractmethod
    def dump_to_file(self, vacancy):
        pass

    # @abstractmethod
    # def get_vacancies(self, criteria):
    #     pass
    #
    # @abstractmethod
    # def delete_vacancy(self, vacancy_id):
    #     pass
