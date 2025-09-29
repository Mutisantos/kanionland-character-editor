from app.learning.OOP.services.store_stock_service import StoreStockService
from .chain_handler import Handler
from app.learning.OOP.store_transaction import StoreTransaction


class StoreStockHandler(Handler):

    def __init__(self, store_stock_service: StoreStockService):
        self.store_stock_service = store_stock_service

    def handle(self, request: StoreTransaction) -> None:
        item = request.item
        if (self.store_stock_service.has_equipement(item, request.amount)):
            self.store_stock_service.sell_equipement(item, request.amount)
            self._next_handler.handle(request)
        else:
            print("Item out of stock")
