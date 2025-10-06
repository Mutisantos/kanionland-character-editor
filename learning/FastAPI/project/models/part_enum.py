from enum import Enum
from typing import Union


class BodyPart(str, Enum):
    HEAD = "Head"
    LEFT_ARM = "Left Arm"
    RIGHT_ARM = "Right Arm"
    TORSO = "Torso"
    LEFT_LEG = "Left Leg"
    RIGHT_LEG = "Right Leg"
    TAIL = "Tail"
    LEFT_EAR_ARM = "Left Ear-Arm"
    RIGHT_EAR_ARM = "Right Ear-Arm"

    @property
    def max_health(self) -> int:
        # Preserve your specific health values
        health_map = {
            "Head": 100,
            "Left Arm": 50,
            "Right Arm": 20,
            "Torso": 20,
            "Left Leg": 20,
            "Right Leg": 20,
            "Tail": 30,
            "Left Ear-Arm": 35,
            "Right Ear-Arm": 35
        }
        return health_map[self.value]

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
            BodyPart.HEAD,
            BodyPart.LEFT_ARM,
            BodyPart.RIGHT_ARM,
            BodyPart.TORSO,
            BodyPart.LEFT_LEG,
            BodyPart.RIGHT_LEG
        ]
