"""Реализация класса для работы с информацией о вакансиях в JSON-файл"""
import json
from src.saver_class import Saver


class JSONSaver(Saver):
    def __init__(self, data: list):
        super().__init__(data)

    def add_vacancies(self):
        """
        Функция записи файла с вакансиями
        """
        with open("data_file.json", 'w', encoding='utf-8') as outfile:
            json.dump(self._data, outfile, indent=1, ensure_ascii=False)
