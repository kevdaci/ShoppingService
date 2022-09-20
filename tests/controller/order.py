from unittest import mock, TestCase
from src import create_app
from src.service import order

from tests.mock import data

class OrderControllerUnitTest(TestCase):

	def setUp(self):
		created_app = create_app()
		self.app = created_app.test_client()
		self.order_summary_service = order.order_summary
		self.get_orders_service = order.get_orders
		self.get_order_service = order.get_order
		order.order_summary = mock.MagicMock(return_value=data.mock_summary)
		order.get_orders = mock.MagicMock(return_value=data.mock_orders)
		order.get_order = mock.MagicMock(return_value=data.mock_order)

	def tearDown(self):
		order.order_summary = self.order_summary_service
		order.get_orders = self.get_orders_service
		order.get_order = self.get_order_service

	def test_get_orders(self):
		response = self.app.get('/order', json=data.request_data)
		self.assertEqual(response.status_code, 200)
		self.assertIsNotNone(response.json)

	def test_get_order(self):
		order_id = 'ed854482-89a1-4423-aff6-91991a389e46'
		response = self.app.get(f'/order/{order_id}', json=data.request_data)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json['order_id'], order_id)

	def test_order_summary(self):
		response = self.app.post('/order', json=data.request_data)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json['total'], 1.7)


