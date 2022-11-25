from pprint import pprint

file_path = "recipes.txt"


def make_cook_book(menu="recipes.txt"):
    cook_book = {}
    with open(menu, encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            count = int(file.readline())
            ingridients_list = []
            for item in range(count):
                ingridient = file.readline().strip()
                ingtidient_split = ingridient.split(' | ')
                ingridients = {'ingridient_name': ingtidient_split[0], 'quantity': int(ingtidient_split[1]),
                               'measure': ingtidient_split[2]}
                ingridients_list.append(ingridients)
            file.readline()
            cook_book[dish_name] = ingridients_list
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingridient_list = dict()
    cook_book = make_cook_book()

    for dish_name in dishes:
        if dish_name in cook_book:
            for ingridients in cook_book[dish_name]:
                measure_quantity_list = {}
                if ingridients['ingridient_name'] not in ingridient_list:
                    measure_quantity_list['measure'] = ingridients['measure']
                    measure_quantity_list['quantity'] = ingridients['quantity'] * person_count
                    ingridient_list[ingridients['ingridient_name']] = measure_quantity_list
                else:
                    ingridient_list[ingridients['ingridient_name']]['quantity'] = \
                        ingridient_list[ingridients['ingridient_name']]['quantity'] + \
                        ingridients['quantity'] * person_count

        else:
            print("Блюдо отсутсвует в меню")
    return ingridient_list


pprint(make_cook_book(file_path))
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 22))
