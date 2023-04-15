import json
import os
from src.saver_class import Saver


class JSONSaver(Saver):
    def __init__(self):
        self.file_name: str = 'JSON.json'

    def save_in_file(self, headhunter=None, superjob=None):
        """
        Функция сохраняет данные о вакансиях в файл JSON.
        """
        if headhunter is not None and superjob is None:
            # Если указан только аргумент headhunter, сохраняем словарь в формате JSON для вакансий headhunter
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump(
                    sorted([vars(vacancy) for vacancy in headhunter], key=lambda x: x['salary']['from'], reverse=True),
                    file,
                    ensure_ascii=False,
                    indent=4
                )
        elif superjob is not None and headhunter is None:
            # Если указан только аргумент superjob, сохраняем словарь в формате JSON для вакансий superjob
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump(
                    sorted([vars(vacancy) for vacancy in superjob], key=lambda x: x['salary']['from'], reverse=True),
                    file,
                    ensure_ascii=False,
                    indent=4
                )
        elif headhunter is not None and superjob is not None:
            # При получении обоих аргументов для каждого создаем свой JSON-файл и сохраняем в каждый словарь с их API
            with open('JSON_HH.json', 'w', encoding='utf-8') as file:
                json.dump(
                    [vars(vacancy) for vacancy in headhunter],
                    file,
                    ensure_ascii=False,
                    indent=4
                )  # headhunter
            with open('JSON_SJ.json', 'w', encoding='utf-8') as file:
                json.dump(
                    [vars(vacancy) for vacancy in superjob],
                    file,
                    ensure_ascii=False,
                    indent=4
                )  # superjob

            # Открыть первый файл JSON и сохранить данные
            with open('JSON_HH.json', 'r', encoding='utf-8') as file:
                json_hh = json.load(file)
            # Открыть второй файл JSON и сохранить данные
            with open('JSON_SJ.json', 'r', encoding='utf-8') as file:
                json_sj = json.load(file)

            vacancies = json_hh + json_sj  # складываем два словаря

            # Сортируем по зарплате (вначале самое большое значение) и сохраняем в общий JSON-файл
            sorted_vacancies = sorted(vacancies, key=lambda v: v['salary']['from'], reverse=True)
            with open(self.file_name, 'w', encoding='utf-8') as file:
                json.dump(sorted_vacancies,
                          file,
                          ensure_ascii=False,
                          indent=4
                          )

            # Удаляем временные JSON-файлы
            os.remove("JSON_HH.json")
            os.remove("JSON_SJ.json")

        else:
            print('')  # если нет аргументов

    def get_vacancies_by_salary(self, salary_input):
        """
        Возвращает список вакансий с заданной зарплатой.
        Зарплата должна быть в формате "100 000-150 000 руб."
        Возвращает список вакансий.
        """
        # Открываем файл JSON и загрузите его содержимое
        with open(self.file_name, 'r', encoding='utf-8') as file:
            vacancy = json.load(file)

        # Создание пустого списка для хранения совпадающих вакансий
        test_dict = []

        # Разделение заданного ввода зарплаты на зарплату и валюту
        try:
            salary, currency = salary_input.split(' ')
        except:
            # Если пользовательский ввод содержит только зарплату, предположим, что валюта указана в рублях
            salary = salary_input
            currency = ['руб', 'rur', 'rub', 'RUR']

        # Проверяем, указана ли валюта в рублях, т.к. параметры для hh и sj настроены на поиск только по России и в
        # рублях
        if currency in ['руб', 'RUR', 'rub']:
            currency = ['руб', 'rur', 'rub', 'RUR']

        # Перебираем каждую вакансию в загруженном JSON-файле
        for vac in vacancy:
            try:
                # Проверяем, соответствует ли зарплата введенным данным и входит ли валюта в разрешенные валюты
                if int(vac['salary']['from']) >= int(salary) and vac['salary']['currency'] in currency:
                    test_dict.append(vac)
                # Если валюта USD, конвертируем зарплату в рубли (по цб от 14.04.2023) и проверяем, совпадает ли она
                # с введенной
                elif vac['salary']['currency'] in ['usd', 'USD'] and int(vac['salary']['from']) * 83 >= int(salary):
                    test_dict.append(vac)
            except:
                # Если вакансии без информации о зарплате, то пропускаем
                continue

        # Открываем тот же JSON-файл еще раз и перезаписываем его обновленным списком подходящих вакансий
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(test_dict, file, ensure_ascii=False, indent=4)

    def search_words(self, search_words):
        """ Функция позволяет искать вакансии по заданным ключевым словам """
        # Если запрос пустой, возвращает все вакансии из файла
        if not isinstance(search_words, str):
            return "Error: запрос должен быть строкой"
        if search_words == '':
            with open(self.file_name, 'r', encoding='utf-8') as file:
                vacancies = json.load(file)
            return vacancies
        else:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                vacancies = json.load(file)
            # Иначе происходит поиск вакансий по ключевым словам
            result = []
            for vacancy in vacancies:
                for word in search_words.split():
                    if word.lower() in vacancy['description'].lower():
                        result.append(vacancy)
                        break
            return result

    def json_results(self):
        """
        Вывод итоговой информации по JSON-файлу
        """
        # Открываем файл в режиме чтения
        with open(self.file_name, 'r', encoding='utf-8') as file:
            # Загружаем содержимое файла в переменную final как словарь
            final_result = json.load(file)
        # Возвращаем итоговый словарь
        return final_result
