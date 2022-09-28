import requests
import json
from utils import *
from classes import *


def main():
    list_of_vacancies = []
    search_text = input("Введите искомую профессию: ")
    count_of_vacancies = input("Введите количество выводимых самых высокооплачиваемых вакансий: ")
    if not count_of_vacancies.isdigit():
        print("Не число, так что будет 10")
        count_of_vacancies = 10
    Superjob.get_request(list_of_vacancies, search_text=search_text)
    HH.get_request(list_of_vacancies, search_text=search_text)
    save_to_file(list_of_vacancies)
    print()
    print_list(get_top_salaries(get_vacancies(), int(count_of_vacancies)))


if __name__ == "__main__":
    main()
