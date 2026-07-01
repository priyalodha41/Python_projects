import datetime


class Order:
    _order_counter = 1

    def __init__(self, customer, cart):
        self.order_id = Order._order_counter
        Order._order_counter += 1
        self.customer = customer
        self.items = list(cart.items)
        self.total_amount = cart.total()
        self.status = "Pending"
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        # Deduct stock now that the order is confirmed
        for item in self.items:
            item.product.decrease_stock(item.quantity)

        cart.clear()
        customer.orders.append(self)

    def update_status(self, status):
        self.status = status

    def __str__(self):
        lines = [f"Order #{self.order_id} | Date: {self.date} | Status: {self.status}"]
        for item in self.items:
            lines.append(f"  - {item.product.name} x {item.quantity} = \u20b9{item.subtotal:.2f}")
        lines.append(f"  Total: \u20b9{self.total_amount:.2f}")
        return "\n".join(lines)