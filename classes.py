from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
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

    @classmethod
    def get_request(cls, list_of_vacancies: list = [], search_text: str = "", count_of_vacancies: int = 1000, currency: str = "RUR") -> list:
        for page in range(int(count_of_vacancies / 20)):
            data = requests.get(cls.url, {"text": search_text, "page": page, "only_with_salary": "true"})
            if data.status_code != 200:
                break
            for item in data.json()["items"]:
                if currency == "any" or item["salary"]["currency"] == currency:
                    list_of_vacancies.append(Vacancy(item["name"], item["alternate_url"], item["snippet"], item["salary"]))
        return list_of_vacancies


class Superjob(Engine):
    url = "https://spb.superjob.ru/vacancy/search/"

    @classmethod
    def get_request(cls, list_of_vacancies: list = [], search_text: str = "") -> list:
        for i in range(50):
            data = requests.get(cls.url, {"keywords": search_text, "page": i + 1})
            soup = BeautifulSoup(data.text, "lxml")
            vacancy_blocks = soup.find_all("div", class_="_2lp1U _2J-3z _3B5DQ")
            for item in vacancy_blocks:
                name_vacancy = item.find("span", class_="_9fIP1 _249GZ _1jb_5 QLdOc").text
                link_vacancy = "https://spb.superjob.ru/" + item.find("a").get("href")
                salary_vacancy = {"from": item.find("span", class_="_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi").text, "currency": "RUR", "to": None}
                salary_vacancy["from"] = salary_vacancy["from"].replace(" ", " ")
                snippet_vacancy = {"responsibility": item.find("div", class_="_2d_Of _2J-3z _3B5DQ").text, "requirement": None}
                list_of_vacancies.append(Vacancy(name_vacancy, link_vacancy, snippet_vacancy, salary_vacancy))
            if '<span class="_115dd">Дальше</span>' not in data.text:
                break
        return list_of_vacancies
