from equipable_object import EquipableObject
from partEnum import Parts

# Syntax for extending EquipableObject


class Armor(EquipableObject):
    def __init__(self, name, weight, part: Parts,
                 defense, balance, spirit, stealth, description="",
                 quality="Common"):
        super().__init__(name, weight, part, description, quality)
        self.defense = defense  # DEF
        self.balance = balance  # EQU
        self.spirit = spirit    # ESP
        self.stealth = stealth  # SIG
