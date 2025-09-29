from learning.OOP.store_transaction import StoreTransaction
from learning.OOP.services.taxing_service import TaxingService
from learning.datastructures.handlers.chain_handler import Handler


class TransactionCostHandler(Handler):
    def handle(self, request: StoreTransaction) -> None:
        item = request.item
        tax = TaxingService().calculate_tax(item)
        request.net_price = item.price
        request.tax = tax
        request.total_price = request.net_price + request.net_price * tax
        self._next_handler.handle(request)
        print(f"Got {request.total_price}$ from {request.amount} {item.name}")


if __name__ == "__main__":
    print("Working")
