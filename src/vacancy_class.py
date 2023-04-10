"""Реализация класса для работы с вакансиями"""


class Vacancy:
    __slots__ = ('__name', '__url', '__description', '__payment')

    def __init__(self, name: str, url: str, description: str, payment: str):
        self.__name = name
        self.__url = url
        self.__description = description
        self.__payment = payment

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def description(self):
        return self.__description

    @property
    def payment(self):
        return self.__payment

    def __str__(self):
        return f"Название профессии: {self.__name}\n" \
               f"url: {self.__url}\n" \
               f"Требования: {self.__description}\n" \
               f"Зарплата: {self.__payment}"

    def __lt__(self, other):
        return int(self.__payment) < int(other.__payment)

    def __le__(self, other):
        return int(self.__payment) <= int(other.__payment)
