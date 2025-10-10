from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class PartEntity(SQLModel, table=True):
    __tablename__ = "parts"
    part_id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True, index=True)  # Linked to BodyPart enum values
    max_health: int
