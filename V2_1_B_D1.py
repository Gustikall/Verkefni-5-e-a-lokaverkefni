# Höfundur: Ágúst Már Þórðarson
# Dagsetning: 08/11/26
# Verkefni: Bankareikningur
# Athugasemdir:
# Gast þú leyst þetta verkefni án hjálpar? Já

class BankAccount:
    def __init__(self, nr, stada):
        self.nr = nr
        self.stada = stada

    def deposit(self, upphaed):
        self.stada += upphaed

    def withdraw(self, upphaed):
        self.stada -= upphaed

    def get_balance(self):
        return self.stada

    def __str__(self):
        return f"Númer Bankareiknings: {self.nr} \n Staða: {self.stada} kr"

    def transfer(self, other_account, upphaed):
        other_account.stada += upphaed
        self.stada -= upphaed

account1 = BankAccount(1234,10000)
account2 = BankAccount(5678,20000)

account1.transfer(account2, 10000)
print(account1.stada, account2.stada)

