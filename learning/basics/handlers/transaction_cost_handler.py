from learning.basics import TaxingService
from learning.basics.OOP import StoreTransaction
from .chain_handler import Handler


class TransactionCostHandler(Handler):
    def handle(self, request: StoreTransaction) -> None:
        item = request.equipable_object
        tax = TaxingService().calculate_tax(item)
        request.net_price = item.price
        request.tax = tax
        request.total_price = request.net_price + request.net_price * tax
        print(f"Got {request.total_price}$ from {request.amount} {item.name}")
        super().handle(request)


if __name__ == "__main__":
    print("Working")
