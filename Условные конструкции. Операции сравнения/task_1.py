basic_rate = 10
final_rate = 0

district = input("Введите название округа (Центральный, Северо-Западный, \nЮжный, Северо-Кавказский, Приволжский, Уральский, \nСибирский, Дальневосточный): ")
number_of_children = int(input("Введите количество детей: "))
salary_project = input("Владеете зарплатным проектом в нашем банке? (Да/Нет): ")
insurance = input("Оформить страхование ипотеки? (Да/Нет): ")

if district == "Дальневосточный" or "Уральский":
  final_rate = 2
else:
  final_rate = basic_rate
  if number_of_children > 3:
    final_rate = final_rate - 1
  if salary_project == "Да":
    final_rate = final_rate - 0.5
  if insurance == "Да":
    final_rate = final_rate - 1.5

print("\nВаша процентная ставка по ипотеке составила " + str(final_rate) + " %.")