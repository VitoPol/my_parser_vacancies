import requests
import json
from utils import *
from classes import *


def main():
    list_of_vacancies = []
    search_text = input("Введите искомую профессию: ")
    HH.get_request(list_of_vacancies, search_text=search_text)
    Superjob.get_request(list_of_vacancies, search_text=search_text)
    save_to_file(list_of_vacancies)
    test()


if __name__ == "__main__":
    main()
