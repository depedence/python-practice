try:
    product_price = int(input("Введите цену продукта: "))
except ValueError:
    print("Введите корректную цену, нужно ввести число")

try:
    product_count = int(input("Введите количество продукта: "))
except ValueError:
    print("Введите корректное количество, нужно ввести число")

print(f"Общая стоимость: {product_price * product_count} рублей")
