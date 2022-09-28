from abc import ABC, abstractmethod
import requests

import utils


class Vacancy:
    def __init__(self, name: str, link: str, snippet: dict, salary: dict):
        self._name = name
        self._link = link
        self._snippet = snippet
        self._salary = salary

    def __repr__(self):
        return f"""Вакансия: {self._name}
Ссылка: {self._link}
Зарплата: {self._salary['from']}{' - ' + str(self._salary['to']) if self._salary['to'] else ''} {self._salary['currency']}
Требования: {self._snippet['requirement'] if self._snippet["requirement"] else 'не указано'}
Обязанности: {self._snippet['responsibility'] if self._snippet['responsibility'] else 'не указано'}"""


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(Engine):
    url = "https://api.hh.ru/vacancies"

    def get_request(self, search_text: str = "", count_of_vacancies: int = 1000) -> list:
        all_vacancies = []
        for page in range(int(count_of_vacancies / 20)):
            data = requests.get(self.url, {"text": search_text, "page": page, "only_with_salary": "true"})
            if data.status_code != 200:
                break
            for item in data.json()["items"]:
                all_vacancies.append(Vacancy(item["name"], item["alternate_url"], item["snippet"], item["salary"]))
        return all_vacancies


class Superjob(Engine):
    def get_request(self):
        pass
