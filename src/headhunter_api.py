"""Реализация класса HeadHunterAPI, наследующегося от абстрактного класса, для работы с ресурсом HeadHunter.ru"""
import requests
from src.engine_class import Engine


class HeadHunterAPI(Engine):
    def __init__(self):
        self.vacancies = []

    def get_vacancies(self, search_query: str):
        """
        Метод настройки запроса
        :return: json object
        """
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": search_query,
            "page": 10,
            "per_page": 100,
            "area": 113,  # Россия
            "only_with_salary": True
        }
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            vacancies = response.json()["items"]
            for vacancy in vacancies:
                self.vacancies.append({'name': vacancy['name'],
                                       'url': vacancy['url'],
                                       'description': vacancy['snippet']['requirement'],
                                       'payment': vacancy['salary']
                                       })
            return self.vacancies
        else:
            return f'Error: {response.status_code}'
