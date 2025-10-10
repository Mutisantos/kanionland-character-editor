# Each python file is treated as a module
# Due to that, any file can be imported with their methods and classes
# From-Import statement allows to import only specific elements in module
from .race_enum import Race
from .equipable_object import EquipableObject
from .item import Item
from .armor import Armor
from .weapon import Weapon
from .part_enum import BodyPart
from typing import Dict, Tuple, Optional
from pydantic import BaseModel
from pydantic import Field
from uuid import UUID


class Character(BaseModel):

    # Class attribute definition and scope through Field declarations
    char_id: UUID | None = Field(
        description="ID of the character", default=None)
    name: str = Field(..., description="Name of the character")
    # Race won't have a default value as it is required and valid
    race: Race = Field(..., description="Race of the character")
    gender: str = Field(..., description="Gender of the character")
    age: int = Field(1, description="Age of the character", ge=1)
    weight: int = Field(1, description="Weight of the character", ge=1)
    height: int = Field(1, description="Height of the character", ge=1)
    aura: int = Field(0, description="Aura of the character", ge=0)
    money: int = Field(0, description="Money of the character", ge=0)
    title: str = Field("", description="Title of the character")
    hunger: int = Field(100, description="Character's Hunger", ge=0, le=100)
    thirst: int = Field(100, description="Character's Thirst", ge=0, le=100)
    sleep: int = Field(100, description="Character's Sleep", ge=0, le=100)
    # If the list is provided, the elements must belong to the BodyPart enum
    parts: list[BodyPart] = Field(description="Parts of the character",
                                  default=BodyPart.get_basic_body())
    inventory: Dict[str, Tuple[Item, int]] = Field(
        description="Inventory of the character", default={})
    equipped_items: Dict[BodyPart, list[EquipableObject]] = Field(
        description="Equipped items of the character", default={})

    # Constructor method, where all attributes have their type defined
    # pydantic constructor is used instead of __init__
    # def __init__(
    #         self,
    #         name: str,
    #         race: str,
    #         gender: str,
    #         age: int,
    #         weight: int,
    #         height: int,
    #         aura: int,
    #         money: int,
    #         title: str,
    #         hunger: int,
    #         thrist: int,
    #         sleep: int,
    #         parts: list[Parts] = Parts.get_basic_body()):
    #     self.name = name
    #     self.race = race
    #     self.gender = gender
    #     self.age = age
    #     self.weight = weight
    #     self.height = height
    #     self.aura = aura
    #     self.money = money
    #     self.title = title
    #     self.hunger = hunger
    #     self.thrist = thrist
    #     self.sleep = sleep
    #     self.parts = parts
    #     self.inventory: Dict[str, Tuple[Item, int]] = {}
    #     self.equipped_items: Dict[Parts, list[EquipableObject]] = {}

    @classmethod
    def builder(cls) -> "CharacterBuilder":
        from .character_builder import CharacterBuilder
        return CharacterBuilder()

    # Return a dictionary representation of the Character's attributes.
    def to_dict(self):
        return self.__dict__.copy()

    @property
    def aura(self) -> int:
        return self._aura

    @aura.setter
    # Using setter method as validations are performed on assignment
    def aura(self, value: int):
        # Handle initial assignment during __init__
        if not hasattr(self, '_aura'):
            self._aura = value
            return
        # For subsequent assignments, enforce the rule that aura cannot be lowered
        if value <= self._aura:
            raise ValueError("Aura cannot be lowered")
        self._aura = value

    @aura.deleter
    # Using deleter decorator, blocking "del" python operation
    def aura(self):
        raise AttributeError("Aura cannot be deleted")

    # Arrow notation states which type the method returns
    def display_info(self) -> str:
        info = f"Name: {self.name}\n"
        info += f"The: {self.title}\n"
        return info

    def withdraw_money(self, amount) -> int:
        if amount > self.money:
            raise ValueError(f"Insufficient funds withdrawing {amount}")
        self.money -= amount
        return self.money

    def deposit_money(self, amount) -> int:
        self.money += amount
        return self.money

    def update_hunger(self, amount):
        operation = "increased" if amount > 0 else "decreased"
        self.hunger = max(0, min(100, self.hunger + amount))
        return self.__base_state_reporter("Hunger", self.hunger, operation)

    def update_thirst(self, amount):
        operation = "increased" if amount > 0 else "decreased"
        self.thirst = max(0, min(100, self.thirst + amount))
        return self.__base_state_reporter("Thirst", self.thirst, operation)

    def update_sleep(self, amount):
        operation = "increased" if amount > 0 else "decreased"
        self.sleep = max(0, min(100, self.sleep + amount))
        return self.__base_state_reporter("Sleep", self.sleep, operation)

    # Double underscore state that the method is private
    # Therefore, its scope is limited to the class
    # Also, private methods know already that self is the first argument
    def __base_state_reporter(self, stat, amount, operation) -> str:
        return f"{stat} level {operation} to: {amount}"

    def add_item(self, item: Item, amount=1):
        new_amount = 0
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if item.name in self.inventory:
            new_amount = current_amount + amount
            existing_item, current_amount = self.inventory[item.name]
            self.inventory[item.name] = (
                existing_item, new_amount)
        else:
            new_amount = amount
            self.inventory[item.name] = (item, amount)
        return f"({new_amount}) {item.name}(s) were added to inventory."

    # Similar to Optional<T> in Java, it can encapsulate a value or None
    def has_item(self, item_name: str) -> Optional[Tuple[Item, int]]:
        if item_name in self.inventory:
            return self.inventory[item_name]
        return None

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

    """Return a string representation of the character's equipped items.
    params: None
    returns: str -
        Formatted string of equipped items or a message if none are equipped
    """

    def show_equipment(self):
        if not self.equipped_items:
            return "No items equipped."
        equipped_list = f"Equipped Items for {self.name}:\n"
        for part, items in self.equipped_items.items():
            equipped_list += f"--- {part.name} ---\n"
            for item in items:
                equipped_list += item.display_info()
                if (isinstance(item, Armor)):
                    equipped_list += f"Tipo: Armadura\n"
                elif (isinstance(item, Weapon)):
                    equipped_list += f":Es un arma!\n"
        return equipped_list

    # Method docstring uses triple quotes
    """Add an equipable item to the character equipment
    params: equipable_item: EquipableObject - The item to be equipped
    returns: str - Confirmation message
    """

    def equip_item(self, equipable_item: EquipableObject):
        msg = ""
        if not self.can_equip(equipable_item):
            msg = f"Cannot equip {equipable_item.name}:"
            msg += f"{self.name} doesn't have: {equipable_item.part.name}."
            return msg
        if equipable_item.part in self.equipped_items:
            self.equipped_items[equipable_item.part].append(equipable_item)
        else:
            self.equipped_items[equipable_item.part] = [equipable_item]
        msg = f"{self.name} Equipped {equipable_item.name}"
        msg += f" on {equipable_item.part.name}."
        return msg

    def can_equip(self, equipable_item: EquipableObject):
        return equipable_item.part in self.parts
