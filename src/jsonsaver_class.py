"""Реализация класса для работы с информацией о вакансиях в JSON-файл"""
import json
from src.saver_class import Saver
from src.headhunter_api import HeadHunterAPI


class JSONSaver(Saver):

    def __init__(self, data: list):
        super().__init__(data)

    def dump_to_file(self):
        """
        Метод записи файла с вакансиями
        """
        with open("data.json", 'w', encoding='utf-8') as outfile:
            json.dump(self.data, outfile, indent=1, ensure_ascii=False)
