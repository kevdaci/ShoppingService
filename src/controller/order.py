from flask import Blueprint, request
import src.service.order as order_service

order = Blueprint("order", __name__, url_prefix="/order")


@order.post('')
def order_summary():
	items = request.json['items']
	return order_service.order_summary(items)
