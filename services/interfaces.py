from abc import ABC, abstractmethod

class OrderProcessor(ABC):

    @abstractmethod
    def prepare_order(self, order_id: str):
        pass