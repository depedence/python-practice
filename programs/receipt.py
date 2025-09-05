"""ООП и Классы"""

class Order:
    """Класс создания заказа"""

    def __init__(self):
        self.items = []
        self.total = 0
        self.discount = 0

    def add_item(self, name, price):
        self.items.append((name, price))

        self.total += price

    def apply_discount(self, percent):
        self.discount = percent

        self.total = self.total * (1 - percent / 100)

    def print_receipt(self):
        print('Чек:')

        for item in self.items:
            print(f"- {item[0]}: {item[1]} руб.")

        print(f"Со скидкой {self.discount}%: {self.total}")

order = Order()
order.add_item('Американо', 150)
order.add_item('Торт', 230)
order.apply_discount(15)
order.print_receipt()
