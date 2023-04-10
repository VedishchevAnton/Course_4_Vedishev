"""Основные методы для реализации программы"""
from src.headhunter_api import HeadHunterAPI
from src.superjob_api import SuperJobAPI
from src.vacancy_class import Vacancy
from src.jsonsaver_class import JSONSaver
from src.user_operations import UserOperations

API_KEY = 'v3.r.137482765.bec7916c78cac4d8735ecab826d1fa6d374196d3.b0819ec4fbe617fcea37ae324dd6804053e04b87'


def search_query():
    """
    Функция получения поискового запроса
    """
    return input("Введите поисковый запрос(например Python): ")


def resource_selection():
    """
    Функция выбора ресурса
    """
    print(
        "Выберите ресурс для поиска и обработки вакансии: \n"
        "Если вы хотите выбрать HeadHunter.ru, нажмите '1'\n"
        "Если вы хотите выбрать SuperJob.ru, нажмите '2'\n"
        "Если вы хотите использовать оба ресурса, нажмите '3'"
    )
    while True:
        resource = input()
        if resource == '1':
            print('Вы выбрали HeadHunter.ru')
            return 1
        elif resource == '2':
            print('Вы выбрали Superjob.ru')
            return 2
        elif resource == '3':
            print('Вы выбрали оба ресурса ')
            return 3
        else:
            print("Некорректный ввод данных! Следуйте инструкциям, которые указаны выше.")
