from .partEnum import Parts
from pydantic import BaseModel
from pydantic import Field


class EquipableObject(BaseModel):
    # Default already has empty/none values, so it's not required to do it explicitly
    name: str = Field(..., description="Name of the item")
    weight: int = Field(1, description="Weight of the item", ge=1)
    part: Parts = Field(
        Parts.TORSO, description="Part of the body where the item is equipped")
    description: str = Field("", description="Description of the item")
    quality: str = Field("Common", description="Quality of the item")
    price: int = Field(0, description="Price of the item")

    # Replaced by pydantic implicit init
    # def __init__(
    #         self,
    #         name,
    #         weight,
    #         part: Parts,
    #         price,
    #         description="",
    #         quality="Common"):
    #     self.name = name
    #     self.weight = weight
    #     self.description = description
    #     self.quality = quality  # e.g., Common, Rare, Epic, Legendary
    #     self.part = part  # Part of the body where the item is equipped
    #     self.price = price

    # Single underscore states that the method is protected
    # Therefore, its scope is limited to the class and its subclasses
    def _display_base_info(self):
        info = f"Name: {self.name}\n"
        info += f"Weight: {self.weight}\n"
        info += f"Description: {self.description}\n"
        info += f"Quality: {self.quality}\n"
        info += f"Price: {self.price}\n"
        info += f"Equipped on: {self.part.name}\n"
        return info

    def display_info(self):
        info = self._display_base_info()
        return info
