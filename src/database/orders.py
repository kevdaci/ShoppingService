from src.model.order import Order


class OrdersDB():
	orders = []

	def add(self, summary, total):
		order = Order(summary, total)
		self.orders.append(order)
		return order

	def getAll(self):
		return self.orders

	def get(self, order_id):
		specific_order = [order for order in self.orders if order.order_id == order_id][0]
		return specific_order



