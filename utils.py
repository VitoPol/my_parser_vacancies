import requests
import json
import re

def save_to_file(list_of_vacancies: list):
    with open("vacancies.txt", "w", encoding="utf-8") as file:
        for vacancy in list_of_vacancies:
            file.write(vacancy.__repr__() + "\n\n")
