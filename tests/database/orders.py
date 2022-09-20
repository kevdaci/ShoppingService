from unittest import mock, TestCase
from src.database import orders
from src.model import order as order_model
from tests.mock import data

class OrdersDBUnitTest(TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		orders.OrdersDB.orders = []

	def test_orders_db_add(self):
		orders_db = orders.OrdersDB()
		returned_order = orders_db.add(data.mock_summary_db, 1.0)
		self.assertIsNotNone(returned_order.order_id)

	def test_orders_db_getAll(self):
		orders_db = orders.OrdersDB()
		orders_db.add(data.mock_summary_db, 1.0)
		self.assertEqual(len(orders_db.orders), 1)

	def test_orders_db_get(self):
		orders_db = orders.OrdersDB()
		returned_order = orders_db.add(data.mock_summary_db, 1.0)
		self.assertIsNotNone(orders_db.get(returned_order.order_id))