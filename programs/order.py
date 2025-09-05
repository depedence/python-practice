"""Программа для создания заказа."""

def order():
    """Функция для создания заказа."""

    while True:
        try:
            coffee_price = int(input("Введите цену кофе: "))

            if coffee_price <= 0:
                print('Нельзя вводить числа < или = 0')
                continue

            break
        except ValueError:
            print('Введите число!')

    while True:
        try:
            coffee_count = int(input('Введите количество: '))

            if coffee_count <= 0:
                print('Нельзя вводить числа < или = 0')
                continue
            break

        except ValueError:
            print('Введите число!')

    while True:
        try:
            discount = int(input('Введите вашу скидку(%): '))

            if discount < 0:
                print('Скидка не может быть отрицательной')
                continue
            if discount > 100:
                print('Извините, но такой скидки у нас не бывает')
                continue

            break
        except ValueError:
            print('Введите число!')

    if discount != 0:
        print(f'Цена со скидкой: {(coffee_count * coffee_price) * (1 - discount / 100)} руб.')
    else:
        print(f'Цена без скидки: {coffee_count * coffee_price} руб.')

order()
