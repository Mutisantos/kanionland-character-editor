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


@router.get("/characters", tags=["characters"])
def get_all_characters(repo: CharacterRepository = Depends(CharacterRepository)):
    return repo.get_all_characters()


# As a difference from Spring approach, dependencies are solved on runtime
@router.post("/characters", status_code=status.HTTP_201_CREATED, tags=["characters"])
def create_character(json_character: dict, repo: CharacterRepository = Depends(CharacterRepository)):
    try:
        char_a = Character.model_validate(json_character)
        char_a.char_id = uuid4()
        repo.create_character(char_a)
        return {"Character": char_a, "id": str(char_a.char_id)}
    except ValueError as e:
        exception_params = e.errors()[0]
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error at Field: {exception_params['loc'][0].upper()}: {exception_params['msg']}"
        )
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error while creating Character: {str(e.__cause__)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error while creating Character: {str(e)}"
        )


@router.get("/characters/{name}", tags=["characters"])
def get_character_by_name(
    name: str,
    repo: CharacterRepository = Depends(CharacterRepository)
):
    return repo.get_character_by_name(name)


@router.delete("/characters/{name}", tags=["characters"])
def delete_character_by_name(
    name: str,
    repo: CharacterRepository = Depends(CharacterRepository)
):
    return repo.delete_character_by_name(name)


@router.patch("/characters/{name}", status_code=status.HTTP_200_OK, tags=["characters"])
def update_character_by_name(
    name: str,
    json_character: dict,
    repo: CharacterRepository = Depends(CharacterRepository)
):
    return repo.patch_character_by_name(name, json_character)


# Executed with the script fastapi dev/run (switched between Development and Production modes)
# Development mode allows hot-swapping every time a change is made to the code
# shows the server running and where the documentation is available (using OpenAPI and Swagger)

if __name__ == "__main__":
    # Uvicorn direct execution will be used for debugging purposes
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
