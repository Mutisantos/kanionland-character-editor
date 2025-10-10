from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

# In order to operate over databases using SQLModel, a new class representing the table must exist.
# This class is separated from the model class as a decoupled solution following the SOLID principles
# and Clean Architecture principles.


class ClassRankEntity(SQLModel, table=True):
    __tablename__ = "ranks"
    # SQLModel also provides Field operations as pydantic, for SQL definitions
    rank_id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True)
    description: str
    requiered_experience: int
