from .chain_handler import Handler
from OOP.store_transaction import StoreTransaction
from OOP.helpers.taxing_service import TaxingService


class TransactionCostHandler(Handler):
    def handle(self, request: StoreTransaction) -> None:
        item = request.item
        tax = TaxingService().calculate_tax(item)
        request.net_price = item.price
        request.tax = tax
        request.total_price = request.net_price + request.net_price * tax
        print(f"Got {request.total_price}$ from {request.amount} {item.name}")
        super().handle(request)


if __name__ == "__main__":
    print("Working")
