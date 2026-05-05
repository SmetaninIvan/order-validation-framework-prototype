class MockDBClient:

    def __init__(self):
        self.storage = {}

    def create_order(self, order_name):
        self.storage[order_name] = "New"

    def get_order_status(self, order_name):
        return self.storage.get(order_name)

    def update_order_status(self, order_name, status):
        self.storage[order_name] = status