from unittest import mock, TestCase
from src.service import order

data = {
    "items": [
        {
            "name": "orange",
            "quantity": 3
        },
        {
            "name": "apple",
            "quantity": 4
        }
    ]
}

class OrderServiceUnitTest(TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_order_summary_http_status(self):
		response = order.order_summary(data['items'])
		status_code = response[1]
		self.assertEqual(status_code, 200)

	def test_order_summary_total(self):
		response = order.order_summary(data['items'])
		response_body = response[0]
		self.assertEqual(response_body['total'], 3.15)

	def test_order_summary_items(self):
		response = order.order_summary(data['items'])
		response_body = response[0]
		summary = response_body['summary']
		self.assertEqual(summary[0], {"cost": 0.75, "name": "orange", "quantity": 3})
		self.assertEqual(summary[1], {"cost": 2.4, "name": "apple", "quantity": 4})