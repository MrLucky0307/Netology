symbol = input("Введите символ разделения: ")

len_square = float(input("Введите длину стороны квадрата: "))
perimeter_square = len_square * 4
area_square = len_square ** 2
print("Периметр: ", perimeter_square)
print("Площадь: ", area_square)

len_rectangle = float(input("\nВведите длину прямоугольника: "))
width_rectangle = float(input("Введите ширину прямоугольника: "))
perimeter_rectangle = (len_rectangle + width_rectangle) * 2
area_rectangle = len_rectangle * width_rectangle
print("Периметр: ", perimeter_rectangle)
print("Площадь: ", area_rectangle)

print(symbol * int(perimeter_square + area_rectangle))

salary = float(input("Введите заработную плату в месяц: "))
mortgage_interest = float(input("Введите, какой процент(%) уходит на ипотеку: "))
interest_on_life = float(input("Введите, какой процент(%) уходит на жизнь: "))
print("На ипотеку было потрачено: ", salary / 100 * mortgage_interest * 12, " рублей")
print("Было накоплено: ", salary * 12 - salary / 100 * (mortgage_interest + interest_on_life) * 12, " рублей")