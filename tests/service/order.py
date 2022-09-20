from unittest import mock, TestCase
from src.service import order
from src.database import orders
from src.model import order as order_model
from tests.mock import data



class OrderServiceUnitTest(TestCase):

	def setUp(self):
		mock_order = order_model.Order({}, 1.7)
		mock_order.order_id = 'abc123'
		self.orders_db_getAll = orders.OrdersDB.getAll
		self.orders_db_add = orders.OrdersDB.get
		self.orders_db_get = orders.OrdersDB.add
		orders.OrdersDB.getAll = mock.MagicMock(return_value=[mock_order])
		orders.OrdersDB.add = mock.MagicMock(return_value=mock_order)
		orders.OrdersDB.get = mock.MagicMock(return_value=mock_order)
		
	def tearDown(self):
		orders.OrdersDB.getAll = self.orders_db_getAll
		orders.OrdersDB.add = self.orders_db_add
		orders.OrdersDB.get = self.orders_db_get

	def test_order_summary_get_orders(self):
		response = order.get_orders()
		response_body = response[0]
		status_code = response[1]
		self.assertIsNotNone(response_body)
		self.assertIsNotNone(response_body['orders'])

	def test_order_summary_get_order(self):
		response = order.get_order('abc123')
		response_body = response[0]
		status_code = response[1]
		self.assertEqual(response_body['order_id'], 'abc123')

	def test_order_summary_http_status(self):
		response = order.order_summary(data.request_data['items'])
		status_code = response[1]
		self.assertEqual(status_code, 200)

	def test_order_summary_total(self):
		response = order.order_summary(data.request_data['items'])
		response_body = response[0]
		self.assertEqual(response_body['total'], 1.7)

	def test_order_summary_items(self):
		response = order.order_summary(data.request_data['items'])
		response_body = response[0]
		summary = response_body['summary']
		self.assertEqual(summary[0], {"cost": 0.5, "name": "orange", "quantity": 3})
		self.assertEqual(summary[1], {"cost": 1.2, "name": "apple", "quantity": 4})