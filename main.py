from utils import *
from classes import *


def main():
    list_of_vacancies = []
    search_text = input("Введите искомую профессию: ")
    print("Идёт обработка данных...\n")
    Superjob.get_request(list_of_vacancies, search_text=search_text)
    HH.get_request(list_of_vacancies, search_text=search_text)
    save_to_file(list_of_vacancies)
    while True:
        user_input = input("\n1 - топ-N вакансий по зарплате\n2 - N случайных вакансий\nexit - выход\n>>> ")
        print()
        match user_input.lower():
            case "1":
                count_of_vacancies = input("Введите количество выводимых самых высокооплачиваемых вакансий: ")
                if not count_of_vacancies.isdigit():
                    print("Не число, так что будет 10")
                    count_of_vacancies = 10
                print_list(get_top_salaries(get_vacancies(), int(count_of_vacancies)))
            case "2":
                count_of_vacancies = input("Введите количество выводимых случайных вакансий: ")
                if not count_of_vacancies.isdigit():
                    print("Не число, так что будет 10")
                    count_of_vacancies = 10
                print_list(get_random_vacancy(get_vacancies(), int(count_of_vacancies)))
            case "exit":
                break
            case _:
                print("Некорректный ввод")
                continue


if __name__ == "__main__":
    main()
