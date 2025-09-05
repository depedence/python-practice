class Wallet:
    def __init__(self, initial_balance=0):
        self.history = []
        self.balance = initial_balance

    def deposit(self, amount, description):
        self.history.append({"type": "deposit", "amount": amount, "description": description})
        self.balance += amount

    def spend(self, amount, description):
        if self.balance >= amount:
            self.history.append({"type": "spend", "amount": amount, "description": description})
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def show_history(self):
        print('История операций: ')

        for operation in self.history:
            if operation["type"] == "deposit":
                print(f"+ {operation['amount']} руб. ({operation['description']})")
            else:
                print(f"- {operation['amount']} руб. ({operation['description']})")

wallet = Wallet(1000)
wallet.deposit(500, "Зарплата")
wallet.spend(300, "Продукты")
wallet.spend(200, "Кофе")
wallet.show_history()
print(f'Текущий баланс: {wallet.get_balance()} руб.')
