from src.headhunter_api import HeadHunterAPI
from src.superjob_api import SuperJobAPI
from src.jsonsaver_class import JSONSaver


def get_search_query():
    """Функция для получения поискового запроса от пользователя"""
    query = input("Введите поисковый запрос: ")
    return query


def get_user_resource(user_query=None):
    """Функция для получения платформы, с которой пользователь хочет получить вакансии"""
    platform_ = input("Выберите платформу (hh.ru - 1, superjob.ru - 2, обе платформы - 3): ")
    if platform_ == '1':
        print('Вы выбрали HeadHunter.ru!')
        hh = HeadHunterAPI()
        return hh.get_vacancies(user_query)
    elif platform_ == "2":
        print('Вы выбрали Superjob.ru!')
        sj = SuperJobAPI()
        return sj.get_vacancies(user_query)
    elif platform_ == "3":
        print('Вы выбрали обе платформы!')
        hh = HeadHunterAPI()
        sj = SuperJobAPI()
        vacancies = hh.get_vacancies(user_query)
        vacancies.extend(sj.get_vacancies(user_query))
        return vacancies
    else:
        print('Некорректный ввод')
        return []


def data_filter(data):
    """
    Метод работы с полученными вакансиями
    """
    while True:
        print("Вы зашли в меню работы с данными:\n"
              "Если вы хотите сохранить полученные данные в файл и выйти, нажмите '1'\n"
              "Если вы хотите произвести фильтрацию вакансий по ключевому слову, нажмите '2'\n"
              "Если вы хотите вывести top-N вакансий по зарплате, нажмите '3"
              )
        user_input = input()
        if user_input == '1':
            return data
        elif user_input == '2':
            filter_words = input("Введите ключевое слово для фильтрации вакансий: ")
            filtered_vacancies = [vacancy for vacancy in data if filter_words in vacancy['description']]
            if not filtered_vacancies:
                print("Нет вакансий, содержащих данное ключевое слово")
            else:
                return filtered_vacancies
        elif user_input == '3':
            pass


def main():
    print("Вас приветствует программа по сбору и обработке данных с ресурсов HeadHunter.ru и SuperJob.ru!")
    user_query = get_search_query().lower()
    user_request = get_user_resource()
    data_filter(user_request)
    json_saver = JSONSaver(user_request)
    json_saver.dump_to_file()
