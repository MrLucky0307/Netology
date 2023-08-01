print("Введите дату своего дня рождения")
birthday_day = int(input("Число: "))
birthday_month = input("Месяц: ")

if birthday_day in range(21, 32) and birthday_month == "март":
    print("Овен")
elif birthday_day in range(1, 21) and birthday_month == "апрель":
    print("Овен")
elif birthday_day in range(21, 31) and birthday_month == "апрель":
    print("Телец")
elif birthday_day in range(1, 22) and birthday_month == "май":
    print("Телец")
elif birthday_day in range(22, 31) and birthday_month == "май":
    print("Близнецы")
elif birthday_day in range(1, 22) and birthday_month == "июнь":
    print("Близнецы")
elif birthday_day in range(22, 31) and birthday_month == "июнь":
    print("Рак")
elif birthday_day in range(1, 23) and birthday_month == "июль":
    print("Рак")
elif birthday_day in range(23, 32) and birthday_month == "июль":
    print("Лев")
elif birthday_day in range(1, 22) and birthday_month == "август":
    print("Лев")
elif birthday_day in range(22, 32) and birthday_month == "август":
    print("Дева")
elif birthday_day in range(1, 24) and birthday_month == "сентябрь":
    print("Дева")
elif birthday_day in range(24, 31) and birthday_month == "сентябрь":
    print("Весы")
elif birthday_day in range(1, 24) and birthday_month == "октябрь":
    print("Весы")
elif birthday_day in range(24, 32) and birthday_month == "октябрь":
    print("Скорпион")
elif birthday_day in range(1, 23) and birthday_month == "ноябрь":
    print("Скорпион")
elif birthday_day in range(23, 31) and birthday_month == "ноябрь":
    print("Стрелец")
elif birthday_day in range(1, 23) and birthday_month == "декабрь":
    print("Стрелец")
elif birthday_day in range(23, 32) and birthday_month == "декабрь":
    print("Козерог")
elif birthday_day in range(1, 21) and birthday_month == "январь":
    print("Козерог")
elif birthday_day in range(21, 32) and birthday_month == "январь":
    print("Водолей")
elif birthday_day in range(1, 20) and birthday_month == "февраль":
    print("Водолей")
elif birthday_day in range(20, 30) and birthday_month == "февраль":
    print("Рыбы")
elif birthday_day in range(1, 21) and birthday_month == "март":
    print("Рыбы")
