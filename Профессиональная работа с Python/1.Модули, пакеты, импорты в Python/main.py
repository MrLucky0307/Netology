from application import salary
from application.db import people
from datetime import datetime


def main():
    salary.calculate_salary()
    people.get_employees()
    print(datetime.today().strftime("%m/%d/%Y"))


if __name__ == '__main__':
    main()
