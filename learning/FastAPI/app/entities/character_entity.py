from sqlmodel import Relationship, SQLModel, Field
from uuid import UUID, uuid4
from typing import Optional
from .character_rank_entity import CharacterRankEntity


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
    # Many-to-one relationship to character_ranks
    # First, must state the foreign key to link the other table to this table
    rank_level: Optional[int] = Field(
        default=None,
        foreign_key="character_ranks.rank_level"
    )
    # Then, must state the relationship to the other table
    # Back-populates property states which field is used to link to the other table
    rank: Optional[CharacterRankEntity] = Relationship(
        back_populates="characters",
        sa_relationship_kwargs={"order_by": "character_ranks.rank_level"}
    )

    # This approach has direct access to the Part table, but data at the junction table won't be accessible
    # parts: List[PartEntity] = Relationship(back_populates="characters", link_model=CharacterPartLink)
    # This approach has access to the junction table, but requires a join to access the Part table
    # parts: List["CharacterPartLink"] = Relationship()
