from src.static.items import ITEMS


def order_summary(items): 
	summary = create_item_summary(items)
	total_cost = get_total_cost(summary)
	response = {'summary': summary, 'total': total_cost}, 200
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
		summary.append(item_summary)
	return summary

def get_total_cost(summary):
	total = 0.0
	for item in summary:
		total += item['cost']
	return total
