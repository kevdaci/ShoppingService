import uuid

class Order():

	def __init__(self, summary, total):
		self.order_id = str(uuid.uuid4())
		self.summary = summary
		self.total = total
