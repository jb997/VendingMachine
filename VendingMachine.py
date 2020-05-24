class Vending_machine(object):
    def __init__(self):
        self.items = {"coke": 100, "7up": 100, "chocolate": 60, "crisps": 75}
        self.coins = {"1 pound": 100, "50p": 50, "20p": 20, "10p": 10, "5p": 5}
        self.money = 0

    def vend(self, item_name):
        if item_name not in self.items:
            return "Sorry, item not available, you cunt"
        if self.money >= self.items[item_name]:
            change = self.money - self.items[item_name]
            returned_coins = []
            for coin in self.coins:
                if self.coins[coin] <= change:
                    returned_coins.append(coin)
                    change -= self.coins[coin]
            return "{} and {} change".format(item_name, returned_coins)
        return "Not enough money!"

    def insert_coin(self, coin):
        self.money += coin

vm = Vending_machine()
print vm.vend("butt plug")

vm.insert_coin(100)
print vm.vend("chocolate")