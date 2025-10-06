from pydantic import Field
from .character import Character
from .equipable_object import EquipableObject

# The request object that traverses all handlers in the chain


class StoreTransaction:
    buyer: Character = Field(..., description="Buyer of the transaction")
    equipable_object: EquipableObject = Field(..., description="Item of the transaction")
    amount: int = Field(..., description="Amount of items wanted")
    net_price: float = Field(..., description="Net price of the transaction")
    tax: float = Field(..., description="Tax of the transaction")
    total_price: float = Field(..., description="Total price of the transaction")

    def __init__(self, buyer: Character, item: EquipableObject, amount: int = 1):
        self.buyer = buyer
        self.equipable_object = item
        self.amount = amount

    def __str__(self):
        return f"{self.buyer.name} bought {self.equipable_object.type}: {self.equipable_object.name} x {self.amount}"
