# Routers will be the equivalent of controllers in Spring
# Endpoints must hold a tag stating the domain/resource they are handling, so they can be grouped
from fastapi import APIRouter, Depends
from ..repositories.rank_repository import RankRepository

router = APIRouter()

# Decorator defines the endpoint action and path for the function


@router.get("/character-ranks", tags=["ranks"])
def get_all_ranks(repo: RankRepository = Depends(RankRepository)):
    return repo.get_all_ranks()


# Executed with the script fastapi dev/run (switched between Development and Production modes)
# Development mode allows hot-swapping every time a change is made to the code
# shows the server running and where the documentation is available (using OpenAPI and Swagger)

if __name__ == "__main__":
    # Uvicorn direct execution will be used for debugging purposes
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
