from src.headhunter_api import HeadHunterAPI
from src.superjob_api import SuperJobAPI
from src.jsonsaver_class import JSONSaver
from bs4 import BeautifulSoup


def user_interaction():
    """
    Функция, для взаимодействия с пользователем
    """
    hh_api, sj_api = choice_platform()  # выбор платформы для сбора и обработки данных
    hh_vacancies, sj_vacancies = get_from_platform(hh_api, sj_api)  # получение вакансий для выбранных платформ
    filter_word_input = filter_words()  # получение ключевых слов для фильтрации
    salary_input = salary_sort()  # получение минимальной зарплаты
    get_result(hh_vacancies, sj_vacancies, filter_word_input, salary_input)  # вывод результатов поиска


def choice_platform():
    """
    Функция выбора платформы.
    """
    while True:
        platform_ = input("Выберите платформу (hh.ru - 1, superjob.ru - 2): ")
        if platform_ == '1':
            print('Вы выбрали HeadHunter.ru!')
            hh_api = HeadHunterAPI()  # создание экземпляра класса headhunter
            return hh_api, None
        elif platform_ == "2":
            print('Вы выбрали Superjob.ru!')
            sj_api = SuperJobAPI()  # создание экземпляра класса superjob
            return sj_api, None
        # elif platform_ == "3":
        #     print('Вы выбрали обе платформы!')
        #     hh_api = HeadHunterAPI()
        #     sj_api = SuperJobAPI()
        #     return hh_api, sj_api
        else:
            print('Вы не ввели платформу')
            continue


def get_from_platform(hh_api, sj_api):
    """
    Функция получения данных с платформы.
    """
    try:
        search_query = input("Введите поисковый запрос: ")
        if hh_api:
            hh_vacancies = hh_api.get_vacancies(search_query)  # получение данных из headhunter
            return hh_vacancies, None
        elif sj_api:
            sj_vacancies = sj_api.get_vacancies(search_query)  # получение данных из superjob
            return sj_vacancies, None
        if hh_api and sj_api:  # получение данных с обоих ресурсов
            hh_vacancies = hh_api.get_vacancies(search_query)
            sj_vacancies = sj_api.get_vacancies(search_query)
            return hh_vacancies, sj_vacancies
    except:
        print('Некорректный запрос')


def filter_words():
    """
    Функция запрашивает у пользователя ввод ключевых слов для фильтрации вакансий по
    описанию.
    """
    user_input = input("Введите ключевые слова для фильтрации вакансий в описании:\n")
    return user_input


def remove_tags(text):
    """
    Функция удаления тегов
    """
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def salary_sort():
    """
    Функция сортировки по зарплате
    """
    while True:
        salary_min = input("Введите минимальную зарплату для поиска (rub): ")
        if not salary_min.strip():
            print("Вы не ввели минимальную зарплату. Минимальное значение будет равно 0")
            return '0'
        try:
            salary_min = int(salary_min)
            return salary_min
        except ValueError:
            print("Некорректное значение. Минимальное значение будет равно 0")
            return '0'


def print_top_vacancies(final):
    """
    Функция выводит top N вакансий на основе информации о зарплате.
    """
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    if len(final) > 0:
        for n in range(top_n):
            # проверяем доступна ли информация о зарплате
            if final[n]['salary']['from'] == 0:
                salary_text = 'Зарплата не указана'
            else:
                salary_text = f"Зарплата: {final[n]['salary']['from']} руб"

            # вывод информацию о вакансии
            print(f"{final[n]['title']}\n"
                  f"{salary_text}\n"
                  f"Описание вакансии:\n{remove_tags(final[n]['description'])}\n"
                  f"Ссылка: {final[n]['url']}\n")
    else:
        print('Вакансий по вашему запросу нет')


def get_result(hh_vacancies, sj_vacancies, filter_word_input, salary_input):
    """
    Функция вывода результатов поиска вакансий
    """
    json_saver = JSONSaver()  # создание экземпляра класса для сохранения результатов в JSON-файл
    json_saver.save_in_file(headhunter=hh_vacancies, superjob=sj_vacancies)  # добавление полученных данных в JSON-файл
    json_saver.search_words(filter_word_input)  # фильтрация вакансий по ключевым словам
    json_saver.get_vacancies_by_salary(salary_input)  # фильтрация вакансий по зарплате
    final = json_saver.json_results()  # получение итогового результата
    print_top_vacancies(final)
