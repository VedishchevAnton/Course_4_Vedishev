from src.headhunter_api import HeadHunterAPI
from src.superjob_api import SuperJobAPI
from src.jsonsaver_class import JSONSaver


def get_user_query():
    """
    Метод получения поискового запроса
    """
    return input("Введите поисковый запрос(например Python developer): ")


def get_user_resource():
    """
    Метод выбора ресурса
    """
    user_input = input()
    if user_input == '1':
        print('Вы выбрали HeadHunter.ru')
        hh = HeadHunterAPI()
        return hh.get_vacancies(get_user_query())
    elif user_input == '2':
        print('Вы выбрали Superjob.ru')
        sj = SuperJobAPI()
        return sj.get_vacancies(get_user_query())
    else:
        print('Некорректный ввод')


def data_filter(vacancies):
    """
    Метод работы с полученными вакансиями
    """
    while True:
        print("Вы зашли в меню работы с данными:\n"
              "Если вы хотите сохранить полученные данные в файл и выйти, нажмите '1'\n"
              "Если вы хотите произвести фильтрацию вакансий по ключевому слову, нажмите '2'"
              )
        user_input = input()
        if user_input == '1':
            json_saver = JSONSaver(vacancies)
            return json_saver.dump_to_file()
        elif user_input == '2':
            filter_words = input("Введите ключевое слово для фильтрации вакансий: ")
            sorted_vacancies = sorted(vacancies, key=lambda x: x[filter_words])
            json_saver = JSONSaver(sorted_vacancies)
            return json_saver.dump_to_file()


def main():
    print("Вас приветствует программа по сбору и обработке данных с ресурсов HeadHunter.ru и SuperJob.ru!\n"
          "Если вы хотите выбрать HeadHunter.ru, нажмите '1'\n"
          "Если вы хотите выбрать SuperJob.ru, нажмите '2'"
          )
    user_input = get_user_resource()
    data_filter(user_input)
