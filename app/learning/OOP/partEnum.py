from enum import Enum
from typing import Union


class Parts(Enum):
    HEAD = ("Head", 100)
    LEFT_ARM = ("Left Arm", 100)
    RIGHT_ARM = ("Right Arm", 100)
    TORSO = ("Torso", 100)
    LEFT_LEG = ("Left Leg", 100)
    RIGHT_LEG = ("Right Leg", 100)
    TAIL = ("Tail", 100)
    LEFT_EAR_ARM = ("Left Ear-Arm", 100)
    RIGHT_EAR_ARM = ("LeRightft Ear-Arm", 100)

    def __init__(self, name: str, healthPercentage: int = 100):
        self._name = name
        self.maxHealth = healthPercentage

    @property
    def name(self):
        return self._name

    @staticmethod
    # With Union, the method can return either a Parts or None
    def get_enum_by_name(name: str) -> Union['Parts', None]:
        # next method works as a findFirst in java streams
        return next(filter(lambda part: part.name == name, Parts), None)
        # The compression list alternative uses a for cycle
        # return next((part for part in Parts if part.name == name), None)

    @staticmethod
    def get_basic_body():
        return [
            Parts.HEAD,
            Parts.LEFT_ARM,
            Parts.RIGHT_ARM,
            Parts.TORSO,
            Parts.LEFT_LEG,
            Parts.RIGHT_LEG
        ]
