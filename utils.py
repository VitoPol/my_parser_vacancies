from re import search
from typing import Iterator


def save_to_file(list_of_vacancies: list):
    with open("vacancies.txt", "w", encoding="utf-8") as file:
        for vacancy in list_of_vacancies:
            file.write(vacancy.__repr__() + "\n\n")


def get_vacancies() -> list:
    with open("vacancies.txt", encoding="utf-8") as file:
        content = file.read()
    content = content.strip().split("\n\n")
    return content


def get_salary_text(text: str) -> int:
    salary = search(r"Зарплата: \D*(\d+\s?\d*)", text)
    if not salary:
        return 0
    salary = salary[1].replace(" ", "")
    return int(salary)


def get_top_salaries(list_of_vacancies: list, count: int = 10) -> list:
    top_list = sorted(list_of_vacancies, key=get_salary_text, reverse=True)
    count = min(count, len(top_list))
    return top_list[:count]


def print_list(list_: list) -> None:
    for item in list_:
        print(item, "\n")
