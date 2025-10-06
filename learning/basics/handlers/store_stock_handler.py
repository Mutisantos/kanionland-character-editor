from .chain_handler import Handler
from .. import StoreStockService
from ..OOP import StoreTransaction


class StoreStockHandler(Handler):

    def __init__(self, store_stock_service: StoreStockService):
        self.store_stock_service = store_stock_service

    def handle(self, request: StoreTransaction) -> None:
        eq_object = request.equipable_object
        if self.store_stock_service.has_equipement(eq_object, request.amount):
            self.store_stock_service.sell_equipment(eq_object, request.amount)
            super().handle(request)
        else:
            print("Not enough stock for transaction")
