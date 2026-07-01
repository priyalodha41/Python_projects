from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount
        self.status = "Pending"

    @abstractmethod
    def pay(self):
        pass

    def display_payment(self):
        print(f"Amount: \u20b9{self.amount:.2f} | Status: {self.status}")


class UPI(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def pay(self):
        print(f"Processing UPI payment of \u20b9{self.amount:.2f} via {self.upi_id}...")
        self.status = "Paid"


class Card(Payment):
    def __init__(self, amount, card_number, card_holder, expiry_date):
        super().__init__(amount)
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiry_date = expiry_date

    def _masked_number(self):
        if len(self.card_number) >= 4:
            return "**** **** **** " + self.card_number[-4:]
        return self.card_number

    def pay(self):
        print(f"Processing Card payment of \u20b9{self.amount:.2f} using card {self._masked_number()}...")
        self.status = "Paid"

    def display_payment(self):
        print(f"Card Holder: {self.card_holder} | Card: {self._masked_number()} | "
              f"Amount: \u20b9{self.amount:.2f} | Status: {self.status}")


class CashOnDelivery(Payment):
    def pay(self):
        print(f"Cash on Delivery selected for \u20b9{self.amount:.2f}. Pay at the time of delivery.")
        self.status = "Pending (COD)"