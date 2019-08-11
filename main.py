from decorator import logger_path


@logger_path()
def read_and_format():
    '''Задача №1'''
    global cook_book
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as f:

        @logger_path()
        def create_dish():
            '''Создание списков под каждое блюдо'''
            dish = []
            count = int(f.readline().strip())
            cycle = 0
            while cycle != count:
                cycle += 1
                dish.append(create_ingredients())
            f.readline().strip()
            return dish

        @logger_path()
        def create_ingredients():
            '''Наполняем списки блюд ингридиентами'''
            l1 = f.readline().strip()
            l2 = l1.split(' | ', 3)
            # вспомогательные переменные
            ingredients = {'ingredient_name': l2[0],
                           'quantity': l2[1],
                           'measure': l2[2]}
            return ingredients

        for line in f:
            line = line.strip()
            cook_book[line] = create_dish()


@logger_path()
def get_shop_list_by_dishes(dishes, person_count):
    '''Задача №2'''
    read_and_format()
    global result
    result = {}
    for dish in dishes:
        if dish not in cook_book.keys():
            print(f'"{dish}" - нет рецепта или некорректный ввод :(')
        else:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient['quantity'] = int(ingredient['quantity']) * person_count
                if ingredient['ingredient_name'] not in result.keys():
                    result[ingredient['ingredient_name']] = {'quantity': ingredient['quantity'],
                                                             'measure': ingredient['measure']}
                else:
                    d1 = result[ingredient['ingredient_name']]
                    d2 = d1['quantity'] + ingredient['quantity']
                    d1.update({'quantity': d2})
                    # вспомогательные переменные


def main():
    print()
    print('1 - Задача №1')
    print('2 - Задача №2')
    print('q - Выход')
    while True:
        print()
        user_input = input('Выбор задачи: ')
        print()
        if user_input == '1':
            read_and_format()
            print(cook_book)
        elif user_input == '2':
            print('Формат ввода: Блюдо1, Блюдо2, Блюдо3, ...')
            dish_input = input('Что готовим? ').split(', ')
            ppl_input = int(input('На сколько человек? '))
            if ppl_input <= 0:
                print('Так не бывает :)')
            else:
                get_shop_list_by_dishes(dish_input, ppl_input)
                print(result)
        elif user_input == 'q':
            print('До встречи!')
            break
        else:
            print('Некорректная команда!')


if __name__ == "__main__":
    main()

# print(globals())
