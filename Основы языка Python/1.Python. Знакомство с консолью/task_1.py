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
