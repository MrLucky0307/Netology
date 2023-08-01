with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_quantity = int(file.readline())
        ingredients = []
        for _ in range(ingredients_quantity):
            qty = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = qty
            ingredients.append({'ingredient_name': ingredient_name,
                                'quantity': quantity,
                                'measure': measure})
        file.readline()
        dish_book = {dish_name: ingredients}
        cook_book.update(dish_book)


def get_shop_list_by_dishes(dishes, persons):
    new_cook_book = {}
    for dish in dishes:
        for food in (cook_book[dish]):
            ingredients_list = dict([(food['ingredient_name'],
                                      {'measure': food['measure'],
                                       'quantity': int(food['quantity'])*persons})])
            if new_cook_book.get(food['ingredient_name']):
                sort = (int(new_cook_book[food['ingredient_name']]['quantity']) +
                        int(ingredients_list[food['ingredient_name']]['quantity']))
                new_cook_book[food['ingredient_name']]['quantity'] = sort
            else:
                new_cook_book.update(ingredients_list)
    print(new_cook_book)
    return


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 5)
