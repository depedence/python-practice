"""Программа для расчета общей стоимости товаров."""

while True:
    try:
        product_price = int(input("Введите цену продукта: "))
        break
    except ValueError:
        print("Введите корректную цену, нужно ввести число")

while True:
    try:
        product_count = int(input("Введите количество продукта: "))
        break
    except ValueError:
        print("Введите корректное количество, нужно ввести число")

print(f"Общая стоимость: {product_price * product_count} рублей")

try:
    with open("src/total_cost.txt", "w") as file:
        file.write(f"Цена продукта: {product_price} рублей\n")
        file.write(f"Количество продукта: {product_count} штук\n")
        file.write(f"Общая стоимость чека: {product_price * product_count} рублей")
except FileNotFoundError as e:
    print(f"Ошибка при записи в файл: {e}")
