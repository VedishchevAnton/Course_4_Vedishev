"""Основные методы для реализации программы"""
from src.headhunter_api import HeadHunterAPI
from src.superjob_api import SuperJobAPI
from src.jsonsaver_class import JSONSaver
from src.user_operations import UserOperations

API_KEY = 'v3.r.137482765.bec7916c78cac4d8735ecab826d1fa6d374196d3.b0819ec4fbe617fcea37ae324dd6804053e04b87'


def search_query():
    """
    Метод получения поискового запроса
    """
    return input("Введите поисковый запрос(например Python): ")


def resource_selection():
    """
    Метод выбора ресурса
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


def get_user_request():
    """
    Метод поиска запрашиваемых данных на выбранном ресурсе
    """
    while True:
        if resource_selection() == 1:
            hh = HeadHunterAPI()
            return hh.get_vacancies(search_query())
        elif resource_selection() == 2:
            sj = SuperJobAPI()
            return sj.get_vacancies(search_query())
        elif resource_selection() == 3:
            hh = HeadHunterAPI()
            hh_vacancies = hh.get_vacancies(search_query())
            sj = SuperJobAPI()
            sj_vacancies = sj.get_vacancies(search_query())
            return hh_vacancies + sj_vacancies


def work_with_file(vacancies):
    """
    Метод работы с данными от лица пользователя
    """
    while True:
        print(
            "Если хотите сохранить файл и выйти, нажмите '1'\n"
            "Если хотите произвести сортировку вакансий по ключевому слову, нажмите '2'\n"
            "Если хотите произвести сортировку вакансий по заработной плате, нажмите '3'\n"
            "Если хотите произвести сортировку по выбранным вами вакансиям, нажмите '4'"
        )

        user = input()
        if user == '1':
            return vacancies
        elif user == '2':
            filter_words = input("Введите ключевое слово для фильтрации вакансий: ")
            vacancies = UserOperations(vacancies, filter_words,
                                       top_count=0).filter_vacancies()
            if not vacancies:
                print("Нет вакансий, соответствующих заданным критериям.")
                return
            print("Операция выполнена!")
        elif user == '3':
            vacancies = UserOperations(vacancies).sorting()  # Сортировка полученных данных
            print("Операция выполнена!")
        elif user == '4':
            while True:
                try:
                    top_count = float(input("Введите количество вакансий: "))
                    vacancies = UserOperations(vacancies, top_count).get_top()  # Отсортировка топ N-количества вакансий
                    print("Операция выполнена!")
                    break
                except ValueError:
                    print("Вы ввели не число. Пожалуйста, попробуйте снова.")
        else:
            print("Неверное значение! Введите цифру от 1 - 4!")


def check_vacancies_data():
    """
    Метод проверки найденных по запросу вакансий
    """
    while True:
        vacancies_data = get_user_request()
        for vacancies in vacancies_data:
            if vacancies:
                return vacancies_data
            print("Ваш запрос не найден!")


def main():
    print('Вас приветствует программа по сбору и обработке данных с ресурсов HeadHunter.ru и SuperJob.ru.')
    print()
    vacancies_data = check_vacancies_data()
    json_saver = JSONSaver(vacancies_data)
    json_saver.add_vacancies()
    vacancies = json_saver.data_file()
    user_vacancies = work_with_file(vacancies)
    JSONSaver(user_vacancies).get_user_file()
    print("Данные сохранены и записаны в файл 'user_data.json'")
