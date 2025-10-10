from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4


class PartEntity(SQLModel, table=True):
    __tablename__ = "parts"
    part_id: int = Field(primary_key=True, index=True)
    name: str = Field(unique=True)  # Linked to BodyPart enum values
    max_health: int
