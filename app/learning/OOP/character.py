from equipable_object import EquipableObject
from item import Item
from partEnum import Parts
from typing import Dict, Tuple


class Character:
    # Constructor method
    def __init__(
            self,
            name,
            race,
            gender,
            age,
            weight,
            height,
            aura,
            money,
            title,
            hunger,
            thrist,
            sleep,
            parts=Parts.get_basic_body()):
        self.name = name
        self.race = race
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.aura = aura
        self.money = money
        self.title = title
        self.hunger = hunger
        self.thirst = thrist
        self.sleep = sleep
        self.inventory: Dict[str, Tuple[Item, int]] = {}
        self.parts = parts
        self.equipped_items: Dict[Parts, list[EquipableObject]] = {}

    def to_dict(self):
        """Return a dictionary representation of the Character's attributes."""
        return self.__dict__.copy()

    def display_info(self):
        info = f"Name: {self.name}\n"
        info += f"The: {self.title}\n"
        return info

    def withdraw_money(self, amount):
        if amount > self.money:
            return "Insufficient funds"
        self.money -= amount
        return f"Withdrawal of {amount} successful. New balance: {self.money}"

    def deposit_money(self, amount):
        self.money += amount
        return f"Deposit of {amount} successful. New balance: {self.money}"

    def update_hunger(self, amount):
        operation = "increased" if amount > 0 else "decreased"
        self.hunger = max(0, min(100, self.hunger + amount))
        return f"Hunger level {operation} to: {self.hunger}"

    def update_thirst(self, amount):
        operation = "increased" if amount > 0 else "decreased"
        self.thirst = max(0, min(100, self.thirst + amount))
        return f"Thirst level {operation} to: {self.thirst}"

    def update_sleep(self, amount):
        operation = "increased" if amount > 0 else "decreased"
        self.sleep = max(0, min(100, self.sleep + amount))
        return f"Sleep level {operation} to: {self.sleep}"

    def add_item(self, item: Item, amount=1):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if item.name in self.inventory:
            existing_item, current_amount = self.inventory[item.name]
            self.inventory[item.name] = (
                existing_item, current_amount + amount)
        else:
            self.inventory[item.name] = (item, amount)
        return f"Item {item.name} added to inventory."

    def consume_item(self, item: str, amount=1):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if item in self.inventory.keys():
            existing_item, current_amount = self.inventory[item]
            new_amount = current_amount - amount
            if new_amount == 0:
                del self.inventory[item]
            elif new_amount < 0:
                raise ValueError(f"Not enough {item} in inventory to consume.")
            else:
                self.inventory[item] = (existing_item, new_amount)
            return f"Item {item} consumed from inventory."
        else:
            return f"Item {item} not found in inventory."

    def show_inventory(self):
        if not self.inventory:
            return "Inventory is empty."
        inventory_list = "Inventory:\n"
        for item, item_amount in self.inventory.values():
            inventory_list += "-------\n" + item.display_info(item_amount)
        return inventory_list

    def show_equipment(self):
        if not self.equipped_items:
            return "No items equipped."
        equipped_list = f"Equipped Items for {self.name}:\n"
        for part, items in self.equipped_items.items():
            equipped_list += f"--- {part.name} ---\n"
            for item in items:
                equipped_list += item.display_info() + "\n"
        return equipped_list

    def equip_item(self, equipable_item: EquipableObject):
        if equipable_item.part not in self.parts:
            return f"Cannot equip {equipable_item.name}."
        + f"No such body part: {equipable_item.part.name}."
        if equipable_item.part in self.equipped_items:
            self.equipped_items[equipable_item.part].append(equipable_item)
        else:
            self.equipped_items[equipable_item.part] = [equipable_item]
        return f"Equipped {equipable_item.name} to {equipable_item.part.name}."
