"""Реализация класса SuperJobAPI, наследующегося от абстрактного класса, для работы с ресурсом SuperJob.ru"""
import requests
import os
from src.engine_class import Engine


class SuperJobAPI(Engine):

    def __init__(self):
        self.vacancies = []
        self.api_key: str = os.getenv('API_KEY')
        self.headers = {'X-Api-App-Id': self.api_key}
        self.url = "https://api.superjob.ru/2.0/vacancies/"

    def get_vacancies(self, search_query: str):
        params = {'keyword': search_query,
                  'count': 100,
                  'page': 1
                  }

        response = requests.get(self.url, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            vacancies_data = data['objects']
            for vacancy in vacancies_data:
                vacancy_data = {'name': vacancy['profession'],
                                'url': vacancy['link'],
                                'description': vacancy['candidat'],
                                'payment': vacancy['payment_from']
                                }
                self.vacancies.append(vacancy_data)
            return self.vacancies
        else:
            return f'Error: {response.status_code}'
