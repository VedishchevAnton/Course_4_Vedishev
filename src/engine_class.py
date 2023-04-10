"""Реализация абстрактного класса для работы с API сайтов с вакансиями"""
from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        pass
