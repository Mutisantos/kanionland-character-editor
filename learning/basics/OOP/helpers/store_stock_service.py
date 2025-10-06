from typing import Dict

from learning.basics.OOP import Item
from learning.basics.OOP import EquipableObject


class StoreStockService:
    equipment_stock = Dict[EquipableObject, int]
    item_stock = Dict[Item, int]

    def __init__(self):
        self.equipment_stock = {}
        self.item_stock = {}

    def has_equipement(self, item: EquipableObject, amount: int):
        if item in self.equipment_stock.keys() and self.equipment_stock[item] >= amount:
            return True
        return False

    def add_equipment(self, item: EquipableObject, amount: int):
        if item in self.equipment_stock.keys():
            self.equipment_stock[item] += amount
        else:
            self.equipment_stock[item] = amount

    def add_item(self, item: Item, amount: int):
        if item in self.item_stock.keys():
            self.item_stock[item] += amount
        else:
            self.item_stock[item] = amount

    def sell_equipment(self, item: EquipableObject, amount: int):
        if item in self.equipment_stock.keys() and self.equipment_stock[item] >= amount:
            self.equipment_stock[item] -= amount
        else:
            print("Not enough items in stock")

    def sell_item(self, item: Item, amount: int):
        if item in self.equipment_stock.keys() and self.equipment_stock[item] >= amount:
            self.equipment_stock[item] -= amount
            print(f"Sold {amount} of {item.name}")
        else:
            print("Not enough items in stock")
