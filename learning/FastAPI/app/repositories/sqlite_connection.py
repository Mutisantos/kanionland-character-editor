from typing import Annotated
from fastapi import Depends, FastAPI
from sqlmodel import SQLModel, Session, create_engine

sqlite_name = "kanionlandv2.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

db_engine = create_engine(sqlite_url, connect_args={
                          "check_same_thread": False})


def create_all_tables(app: FastAPI):
    SQLModel.metadata.create_all(db_engine)
    yield

# Create a database connection session with the parameters provided previously


def get_session():
    with Session(db_engine) as session:
        yield session


# Session component will be defined as a dependency
# Other modules can use this dependency to access the database session
SessionDependency = Annotated[Session, Depends(get_session)]
