from equipable_object import EquipableObject
from partEnum import Parts


class Weapon(EquipableObject):
    def __init__(
            self,
            name,
            weight,
            part: Parts,
            strength,
            power,
            range,
            stealth,
            description="",
            quality="Common"):
        super().__init__(name, weight, part, description, quality)
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
