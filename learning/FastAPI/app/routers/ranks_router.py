# Routers will be the equivalent of controllers in Spring
# Endpoints must hold a tag stating the domain/resource they are handling, so they can be grouped
from uuid import uuid4
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, HTTPException, status, Depends
from ..models.character import Character
from ..repositories.character_repository import CharacterRepository
from ..repositories.sqlite_connection import create_all_tables

router = APIRouter()

# Decorator defines the endpoint action and path for the function


@router.get("/character-ranks", tags=["characters"])
def get_all_ranks(repo: CharacterRepository = Depends(CharacterRepository)):
    return repo.get_all_characters()


# Executed with the script fastapi dev/run (switched between Development and Production modes)
# Development mode allows hot-swapping every time a change is made to the code
# shows the server running and where the documentation is available (using OpenAPI and Swagger)

if __name__ == "__main__":
    # Uvicorn direct execution will be used for debugging purposes
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
