from enum import Enum


class Race(str, Enum):
    KANION = "Kanion"
    ORTHYS = "Orthys"
    PUMIBLU = "Pumiblu"
    FIERCY = "Fiercy"
    ZI_BUM = "Zi-Bum"
    LENTILLANO = "Lentillano"
    EYESHADE = "Eyeshade"
    LUIN = "Luin"
    XYRION = "Xyrion"
    CETARA = "Cetara"
    DENDROLIAN = "Dendrolian"
    KEYUI = "Keyui"
    UNTOLD = "Untold"
    SKETCHE = "Sketche"
    PRIMAL = "Primal"
    ROBOT = "Robot"
    ALIEN = "Alien"
    OTHER = "Other"

    @property
    def name(self):
        return self.value.lower().capitalize()

    @classmethod
    def get_enum_by_name(cls, name: str) -> 'Race':
        try:
            return cls[name.upper()]
        except KeyError:
            return cls.OTHER


if __name__ == "__main__":
    print(Race.get_enum_by_name("kAniON").name)
    print(Race.get_enum_by_name("Human").name)
