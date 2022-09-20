from unittest import mock, TestCase
from src import create_app
from src.service import order

class OrderControllerUnitTest(TestCase):

	def setUp(self):
		created_app = create_app()
		self.app = created_app.test_client()
		self.order_summary_service = order.order_summary
		mock_response = {'summary': {}, 'total': 3.15}, 200
		order.order_summary = mock.MagicMock(return_value=mock_response)

	def tearDown(self):
		order.order_summary = self.order_summary_service

	def test_order_summary(self):
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
		response = self.app.post('/order', json=data)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json['total'], 3.15)


if __name__ == "__main__":
	unittest.main()