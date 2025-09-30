from .equipable_object import EquipableObject
from .partEnum import Parts
from pydantic import Field

# This approach sets the class as inmutable
# State will remain read-only after initialization
# @dataclass(frozen=True)


class Weapon(EquipableObject):
    strength: int = Field(0, description="Strength of the weapon", ge=1)
    power: int = Field(0, description="Power of the weapon", ge=1)
    range: int = Field(0, description="Range of the weapon", ge=1)
    stealth: int = Field(0, description="Stealth of the weapon", ge=1)

    def __init__(
            self,
            id,
            name,
            weight,
            part: Parts,
            strength,
            power,
            range,
            stealth,
            price,
            description="",
            quality="Common"):
        super().__init__(id=id, name=name, price=price, weight=weight,
                         part=part, description=description, quality=quality)
        self.strength = strength  # FUE
        self.power = power        # POT
        self.stealth = stealth    # SIG
        self.range = range

    # Thanks to inheritance, we can override the protected method
    def _display_base_info(self):
        info = super()._display_base_info()
        info += f"Strength: {self.strength}\n"
        info += f"Power: {self.power}\n"
        info += f"Stealth: {self.stealth}\n"
        info += f"Range: {self.range}\n"
        return info

    # In the same fashion, we can override the public method
    def display_info(self):
        info = "---- ES UN ARMA! ---- \n"
        info += self._display_base_info()
        return info

    def __hash__(self):
        return hash(self.id)
