"""Реализация класса для работы с информацией о вакансиях в JSON-файл"""
import json
from src.saver_class import Saver


class JSONSaver(Saver):

    def __init__(self, data: list):
        super().__init__(data)

    def add_vacancies(self):
        """
        Метод записи файла с вакансиями
        """
        with open("data_file.json", 'w', encoding='utf-8') as outfile:
            json.dump(self._data, outfile, indent=1, ensure_ascii=False)

    def data_file(self):
        """
        Метод открытия файла с вакансиями
        """
        try:
            with open('data_file.json', 'r', encoding='utf-8') as file:
                raw_json = file.read()
                d_f = json.loads(raw_json)
                return d_f
        except FileNotFoundError:
            print("Файл не найден.")

    def delete_vacancies(self):
        """
        Метод удаления файла с вакансиями
        """
        try:
            with open("data_file.json", "w") as f:
                pass
        except FileNotFoundError:
            print("Файл не найден.")

    def get_user_file(self):
        """
        Метод записи файла с вакансиями, после операций пользователя
        """
        with open("user_data.json", 'w', encoding='utf-8') as outfile:
            json.dump(self._data, outfile, indent=1, ensure_ascii=False)
