from OOP.equipable_object import EquipableObject


class TaxingService:
    def __init__(self):
        self.tax_rates = {
            "Common": 0.1,
            "Uncommon": 0.2,
            "Rare": 0.3,
            "Epic": 0.4,
            "Legendary": 0.5,
            "Default": 0.15
        }

    def calculate_tax(self, item: EquipableObject) -> int:
        if (item.quality in self.tax_rates):
            return item.price * self.tax_rates[item.quality]
        return item.price * self.tax_rates["Default"]
