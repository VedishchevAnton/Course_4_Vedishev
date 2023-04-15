"""Реализация класса SuperJobAPI, наследующегося от абстрактного класса, для работы с ресурсом SuperJob.ru"""
import requests
import os
from src.engine_class import Engine
from src.vacancy_class import Vacancy


class SuperJobAPI(Engine):

    def __init__(self):
        self.api_key: str = os.getenv('API_KEY')
        self.headers = {'X-Api-App-Id': self.api_key}
        self.url = "https://api.superjob.ru/2.0/vacancies/"

    def get_vacancies(self, search_query: str):
        """
            Метод для получения вакансий с помощью SuperJobApi.

            Search_query Ключевое слово для поиска вакансии.
            Return: Список объектов класса Vacancy.
            """
        params = {'keyword': search_query,
                  'count': 100,
                  }

        response = requests.get(self.url, headers=self.headers, params=params)
        if response.status_code == 200:
            data = response.json()
            vacancies_data = data['objects']
            vacancies = []
            for vacancy in vacancies_data:
                title = vacancy['profession']
                salary = SuperJobAPI.get_salary(vacancy)
                description = vacancy['candidat']
                url = vacancy['link']
                vacancy = Vacancy(title, salary, description, url)
                vacancies.append(vacancy)
            return vacancies
        else:
            return f'Error: {response.status_code}'

    @staticmethod
    def get_salary(vacancy, **kwargs):
        if vacancy.get('payment_to') == 0:
            salary = {'from': vacancy['payment_from'], 'currency': vacancy['currency']}
        elif vacancy.get('payment_from') == 0:
            salary = {'from': vacancy['payment_to'], 'currency': vacancy['currency']}
        else:
            salary = {'from': vacancy.get('payment_from', 0), 'to': vacancy.get('payment_to', 0),
                      'currency': vacancy.get('currency', 'rub')}
        return salary

