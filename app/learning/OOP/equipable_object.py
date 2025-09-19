from partEnum import Parts


class EquipableObject:

    def __init__(
            self,
            name,
            weight,
            part: Parts,
            description="",
            quality="Common"):
        self.name = name
        self.weight = weight
        self.description = description
        self.quality = quality  # e.g., Common, Rare, Epic, Legendary
        self.part = part  # Part of the body where the item is equipped

    # Single underscore states that the method is protected
    # Therefore, its scope is limited to the class and its subclasses
    def _display_base_info(self):
        info = f"Name: {self.name}\n"
        info += f"Weight: {self.weight}\n"
        info += f"Description: {self.description}\n"
        info += f"Quality: {self.quality}\n"
        info += f"Equipped on: {self.part.name}\n"
        return info

    def display_info(self):
        info = self._display_base_info()
        return info
