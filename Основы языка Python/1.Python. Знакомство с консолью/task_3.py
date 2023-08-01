symbol = input("Введите символ разделения: ")

round_value = input("Введите значение округления результатов после запятой: ")

len_square = float(input("\nВведите длину стороны квадрата: "))
perimeter_square = round(len_square * 4, int(round_value))
area_square = round(len_square ** 2, int(round_value))
print("Периметр: ", perimeter_square)
print("Площадь: ", area_square)

len_rectangle = float(input("\nВведите длину прямоугольника: "))
width_rectangle = float(input("Введите ширину прямоугольника: "))
perimeter_rectangle = round((len_rectangle + width_rectangle) * 2, int(round_value))
area_rectangle = round(len_rectangle * width_rectangle, int(round_value))
print("Периметр: ", perimeter_rectangle)
print("Площадь: ", area_rectangle)

print(symbol * int(perimeter_square + area_rectangle))

salary = float(input("Введите заработную плату в месяц: "))
mortgage_interest = float(input("Введите, какой процент(%) от з/п уходит на ипотеку: "))
interest_on_life = float(input("Введите, какой процент(%) от з/п уходит на жизнь: "))
print("На ипотеку было потрачено: ", salary / 100 * mortgage_interest * 12, " рублей")
print("Было накоплено: ", salary * 12 - salary / 100 * (mortgage_interest + interest_on_life) * 12, " рублей")
