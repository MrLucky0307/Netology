salary = float(input("Введите заработную плату в месяц: "))
mortgage_interest = float(input("Введите, какой процент(%) от з/п уходит на ипотеку: "))
interest_on_life = float(input("Введите, какой процент(%) от з/п уходит на жизнь: "))
print("На ипотеку было потрачено: ", salary / 100 * mortgage_interest * 12, " рублей")
print("Было накоплено: ", salary * 12 - salary / 100 * (mortgage_interest + interest_on_life) * 12, " рублей")
