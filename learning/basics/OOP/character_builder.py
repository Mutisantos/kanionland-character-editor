"""
Character Builder Class
"""
from typing import Optional
from .partEnum import Parts


class CharacterBuilder:
    def __init__(self):
        self._name: str = None
        self._race: str = None
        self._gender: str = None
        self._aura: int = 0
        self._money: int = 0
        self._title: str = None
        self._hunger: int = 100
        self._thrist: int = 100
        self._sleep: int = 100
        self._parts: Optional[list[Parts]] = None

    # Building methods for each attribute
    def name(self, v: str): self._name = v; return self
    def race(self, v: str): self._race = v; return self
    def gender(self, v: str): self._gender = v; return self
    def age(self, v: int): self._age = v; return self
    def weight(self, v: int): self._weight = v; return self
    def height(self, v: int): self._height = v; return self
    def aura(self, v: int): self._aura = v; return self
    def money(self, v: int): self._money = v; return self
    def title(self, v: str): self._title = v; return self
    def hunger(self, v: int): self._hunger = v; return self
    def thrist(self, v: int): self._thrist = v; return self
    def sleep(self, v: int): self._sleep = v; return self
    def parts(self, v: list[Parts]): self._parts = v; return self

    # Optional: seed from an existing Character (copy-builder)
    @classmethod
    def from_character(cls, c) -> "CharacterBuilder":
        from .character import Character  # Import here to avoid circular import
        build_chara = cls()
        build_chara._name = c.name
        build_chara._race = c.race
        build_chara._gender = c.gender
        build_chara._age = c.age
        build_chara._weight = c.weight
        build_chara._height = c.height
        build_chara._aura = c.aura
        build_chara._money = c.money
        build_chara._title = c.title
        build_chara._hunger = c.hunger
        build_chara._thrist = c.thirst
        build_chara._sleep = c.sleep
        build_chara._parts = c.parts
        return build_chara

    def build(self) -> "Character":
        from .character import Character  # Import here to avoid circular import
        parts_arg = self._parts if self._parts is not None else Parts.get_basic_body()
        return Character(
            name=self._name,
            race=self._race,
            gender=self._gender,
            age=self._age,
            weight=self._weight,
            height=self._height,
            aura=self._aura,
            money=self._money,
            title=self._title,
            hunger=self._hunger,
            thirst=self._thirst,
            sleep=self._sleep,
            parts=parts_arg
        )
