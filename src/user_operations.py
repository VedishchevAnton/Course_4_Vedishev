"""Реализация класса с методами для пользователя"""


class UserOperations:
    def __init__(self, vacancies, filter_words=None, top_count=0):
        self.vacancies = vacancies
        self.filter_words = filter_words
        self.top_count = top_count
        self.list_vacancies = []

    def filter_vacancies(self):
        """
        Метод сортировки вакансий по ключевым словам пользователя
        """
        for i in self.vacancies:
            if i['description'] is not None:
                if self.filter_words.lower() in i['description'].lower():
                    self.list_vacancies.append(i)
        return self.list_vacancies

    def sorting(self):
        """
        Метод сортировки вакансий по зарплате
        """
        sorted_data = sorted(self.vacancies, key=lambda x: self.get_salary_range(x['payment']), reverse=True)
        return sorted_data

    def get_salary_range(self, payment):
        """
        Метод для получения среднего значения зарплаты из диапазона
        """
        if type(payment) != int:
            if payment['currency'] == 'USD':  # Переводим доллар в рубли(пока так)
                if payment['to'] is not None:
                    payment['to'] *= 80
                if payment['from'] is not None:
                    payment['from'] *= 80
                payment['currency'] = 'RUR(from USD(80))'
            if payment['currency'] == 'EUR':
                if payment['to'] is not None:
                    payment['to'] *= 85
                if payment['from'] is not None:
                    payment['from'] *= 85
                payment['currency'] = 'RUR(from EUR(85))'
            if payment['currency'] == 'KZT':
                if payment['to'] is not None:
                    payment['to'] *= 0.15
                if payment['from'] is not None:
                    payment['from'] *= 0.15
                payment['currency'] = 'RUR(from KZT(0,15))'
            if payment['to'] == None:
                return payment['from']
            if payment['from'] == None:
                return payment['to']
            return (payment['to'] + payment['from']) / 2  # Считаем среднее значение зарплаты из значений to и from
        else:
            return payment

    def get_top(self):
        """
        Должен возвращать топ записей из вакансий по зарплате
        """
        top = []
        counter = 0
        for v in self.vacancies:
            if counter < self.filter_words:
                top.append(v)
                counter += 1
            else:
                break
        return top



