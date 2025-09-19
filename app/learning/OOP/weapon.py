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
