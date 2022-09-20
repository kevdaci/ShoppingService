from src.static.items import ITEMS
from src.database.orders import OrdersDB


ordersDB = OrdersDB()

def get_orders():
	orders_dict = [
		{ 'order_id': order.order_id, 'summary': order.summary, 'total': order.total }
		for order in ordersDB.getAll()
	]
	return { 'orders': orders_dict }, 200


def get_order(order_id):
	order = ordersDB.get(order_id)
	order_dict = { 'order_id': order.order_id, 'summary': order.summary, 'total': order.total }
	return order_dict, 200

def order_summary(items): 
	summary = create_item_summary(items)
	total_cost = get_total_cost(summary)
	response_body = { 'summary': summary, 'total': total_cost }
	order = ordersDB.add(response_body['summary'], response_body['total'])
	response_body['order_id'] = order.order_id
	response = response_body, 200
	return response

def create_item_summary(items):
	summary = []
	for item in items:
		item_name = item['name']
		item_quantity = item['quantity']
		item_summary = { 
		    'name': item_name,
			'quantity': item_quantity, 
			'cost': ITEMS[item_name] * item_quantity
		}
		apply_discount(item_summary)
		summary.append(item_summary)
	return summary

def get_total_cost(summary):
	total = 0.0
	for item in summary:
		total += item['cost']
	return total

def apply_discount(item_summary):
	item_name = item_summary['name']
	if(item_name == 'apple'):
		sale = item_summary['quantity'] - (item_summary['quantity'] // 2)
		item_summary['cost'] = ITEMS[item_name] * sale
	if(item_name == 'orange'):
		sale = item_summary['quantity'] // 3
		remaining_orange = item_summary['quantity'] % 3
		item_summary['cost'] = (2 * ITEMS[item_name] * sale) + (ITEMS[item_name] * remaining_orange)
