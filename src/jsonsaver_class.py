"""Реализация класса для работы с информацией о вакансиях в JSON-файл"""
import json
from src.saver_class import Saver
from src.headhunter_api import HeadHunterAPI


class JSONSaver(Saver):
    def __init__(self, filename):
        self.filename = filename
        self.vacancies = []

    def dump_to_file(self, **kwargs):
        """
        Метод записи файла с вакансиями
        :param **kwargs:
        """
        with open("data.json", 'w', encoding='utf-8') as outfile:
            json.dump(self.filename, outfile, indent=1, ensure_ascii=False)
