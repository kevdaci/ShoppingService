from flask import Blueprint, request
import src.service.order as order_service

order = Blueprint("order", __name__, url_prefix="/order")


@order.get('')
def get_orders():
	return order_service.get_orders()

@order.get('/<order_id>')
def get_order(order_id):
	return order_service.get_order(order_id)

@order.post('')
def order_summary():
	items = request.json['items']
	return order_service.order_summary(items)
