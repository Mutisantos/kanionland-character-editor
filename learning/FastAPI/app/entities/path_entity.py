from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4

# Table to represent "sendas"


class PathEntity(SQLModel, table=True):
    __tablename__ = "paths"
    path_id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True)
    description: str
