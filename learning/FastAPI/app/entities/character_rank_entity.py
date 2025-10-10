# In order to operate over databases using SQLModel, a new class representing the table must exist.
# This class is separated from the model class as a decoupled solution following the SOLID principles
# and Clean Architecture principles.
from typing import TYPE_CHECKING, List
from sqlmodel import Column, Identity, Integer, Relationship, SQLModel, Field

# Avoid circular imports
if TYPE_CHECKING:
    from .character_entity import CharacterEntity


class CharacterRankEntity(SQLModel, table=True):
    __tablename__ = "character_ranks"
    # SQLModel also provides Field operations as pydantic, for SQL definitions
    rank_level: int = Field(sa_column=Column(
        "rank_level", Integer, Identity(), primary_key=True))
    name: str = Field(unique=True)
    description: str
    requiered_experience: int
    # One-to-many relationship to characters
    # Back-populates property states which field is used to link to the other table
    characters: List["CharacterEntity"] = Relationship(
        back_populates="rank",
        sa_relationship_kwargs={"lazy": "selectin"}
    )
