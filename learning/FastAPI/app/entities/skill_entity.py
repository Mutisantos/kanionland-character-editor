from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

# In order to operate over databases using SQLModel, a new class representing the table must exist.
# This class is separated from the model class as a decoupled solution following the SOLID principles
# and Clean Architecture principles.


class SkillEntity(SQLModel, table=True):
    __tablename__ = "skills"
    # SQLModel also provides Field operations as pydantic, for SQL definitions
    skill_id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True)
    description: str
    required_exp: int
    physical_cost: int
    mental_cost: int
    is_upgradable: bool
    upgrade_points: int
    upgrade_level: int
