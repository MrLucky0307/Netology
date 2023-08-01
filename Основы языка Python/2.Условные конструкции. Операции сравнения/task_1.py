basic_rate = 10
final_rate = 0
delimiter = ', '
districts_list = ["Центральный", "Северо-Западный", "Южный", "Северо-Кавказский",
                  "Приволжский", "Уральский", "Сибирский", "Дальневосточный"]
district = input(f"Введите название округа ({delimiter.join(districts_list)}): ")
if district == districts_list[-1]:
    print(district)
    print("\nВаша процентная ставка по ипотеке составила 2%.")
elif district in districts_list[:-1]:
    number_of_children = int(input("Введите количество детей: "))
    salary_project = input("Владеете зарплатным проектом в нашем банке? (Да/Нет): ")
    insurance = input("Оформить страхование ипотеки? (Да/Нет): ")
    final_rate = basic_rate
    if number_of_children > 3:
        final_rate -= 1
    if salary_project == "Да":
        final_rate -= 0.5
    if insurance == "Да":
        final_rate -= 1.5
    print("\nВаша процентная ставка по ипотеке составила " + str(final_rate) + "%.")
else:
    print("Неверно введено название округа!")
