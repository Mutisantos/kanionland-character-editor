from .equipable_object import EquipableObject
from .part_enum import BodyPart
from pydantic import Field

# Syntax for extending EquipableObject


class Armor(EquipableObject):
    defense: int = Field(0, description="Defense of the armor")
    balance: int = Field(0, description="Balance of the armor")
    spirit: int = Field(0, description="Spirit of the armor")
    stealth: int = Field(0, description="Stealth of the armor")

    def __init__(self, id, name, weight, part: BodyPart,
                 defense, balance, spirit, stealth, description="",
                 quality="Common",
                 price=1):
        super().__init__(id=id, name=name, price=price, weight=weight,
                         part=part, description=description, quality=quality)
        self.defense = defense  # DEF
        self.balance = balance  # EQU
        self.spirit = spirit    # ESP
        self.stealth = stealth  # SIG

    def __hash__(self):
        return hash(self.id)
