from .chain_handler import Handler
from OOP.helpers.store_stock_service import StoreStockService
from OOP.store_transaction import StoreTransaction


class StoreStockHandler(Handler):

    def __init__(self, store_stock_service: StoreStockService):
        self.store_stock_service = store_stock_service

    def handle(self, request: StoreTransaction) -> None:
        item = request.item
        if (self.store_stock_service.has_equipement(item, request.amount)):
            self.store_stock_service.sell_equipement(item, request.amount)
            super().handle(request)
        else:
            print("Not enough stock for transaction")
