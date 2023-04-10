"""Реализация класса с методами для пользователя"""


class UserOperations:
    def __init__(self, vacancies, filter_words=None, top_count=0):
        self.vacancies = vacancies
        self.filter_words = filter_words
        self.top_count = top_count
        self.list_vacancies = []
