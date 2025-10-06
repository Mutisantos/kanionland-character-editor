from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from models.race_enum import Race

# In order to operate over databases using SQLModel, a new class representing the table must exist.
# This class is separated from the model class as a decoupled solution following the SOLID principles
# and Clean Architecture principles.


class CharacterEntity(SQLModel, table=True):
    __tablename__ = "characters"
    # SQLModel also provides Field operations as pydantic, for SQL definitions
    char_id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True)
    race: str
    gender: str
    age: int
    weight: int
    height: int
    aura: int
    money: int
    title: str
    hunger: int
    thirst: int
    sleep: int
