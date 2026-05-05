#  Это mock CORBA

from services.interfaces import OrderProcessor

class MockCorbaOrderProcessor(OrderProcessor):

    def __init__(self, db):
        self.db = db

    def prepare_order(self, order_id: str):
        print(f"[CORBA MOCK] Preparing order {order_id}")
        self.db.update_order_status(order_id, "Ready")