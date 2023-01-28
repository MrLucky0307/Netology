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