# time: O(n)
# memory: O(1)
class Cashbox:
    def __init__(self, banknotes):
        self.counter = defaultdict(int)
        self.banknotes = banknotes

    def deposit(self, banknote):
        self.counter[banknote] += 1
        
    def withdraw(self, amount) -> bool:
        i = len(self.banknotes) - 1
        while amount > 0 and i >= 0:
            value = self.banknotes[i]
            count = min(self.counter[value], amount // value)    
            amount -= count * value
            self.counter[value] -= count
            i -= 1

        return amount == 0

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cashbox = Cashbox([ 5, 10, 20 ])
        LEMONADE_COST = 5

        for bill in bills:
            cashbox.deposit(bill)
            change = bill - LEMONADE_COST
            if not cashbox.withdraw(change):
                return False

        return True
