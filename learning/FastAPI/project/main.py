# The entrypoint for FastAPI applications
# Usage of uvicorn will allow hosting the python application as a web server
from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi import FastAPI
from uuid import uuid4
from fastapi import Depends
from models.character import Character
from databases.character_repository import CharacterRepository
from databases.sqlite_connection import create_all_tables, SessionDependency

app = FastAPI(lifespan=create_all_tables)

# Decorator defines the endpoint action and path for the function


@app.get("/")
def read_root():
    char_a = Character(name="Gazz Leudos", race="Kanion", gender="M", age=21, weight=42, height=90,
                       aura=430, money=2500, title="Frost Knight", hunger=100, thirst=100, sleep=100)
    return {"Message": "Hello Worlds", "Character": char_a}


@app.get("/time/{iso_code}")
# Parameters either pathvariables or queryparameters must be type-safe
def read_time(iso_code: str = "CO"):
    country_code = iso_code.upper()
    timezone_str = __country_timezones.get(country_code)
    if not timezone_str:
        return {"Error": "Invalid ISO code"}
    tz = ZoneInfo(timezone_str)
    return {"Time": datetime.now(tz)}


@app.get("/characters")
def get_all_characters(repo: CharacterRepository = Depends(CharacterRepository)):
    return repo.get_all_characters()

# As a difference from Spring approach, dependencies are solved on runtime


@app.post("/characters")
def create_character(json_character: dict, repo: CharacterRepository = Depends(CharacterRepository)):
    try:
        char_a = Character.model_validate(json_character)
    except ValueError as e:
        exception_params = e.errors()[0]
        return f"Error at Field: {exception_params["loc"][0].upper()}: {exception_params["msg"]}"
    char_a.char_id = uuid4()
    repo.create_character(char_a)
    return {"Character": char_a}


@app.get("/characters/{name}")
def get_character_by_name(
    name: str,
    repo: CharacterRepository = Depends(CharacterRepository)
):
    return repo.get_character_by_name(name)


__country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "US": "America/New_York",
    "AR": "America/Argentina/Buenos_Aires",
    "CL": "America/Santiago",
    "PE": "America/Lima",
    "ES": "Europe/Madrid"
}

# Executed with the script fastapi dev/run (switched between Development and Production modes)
# Development mode allows hot-swapping every time a change is made to the code
# shows the server running and where the documentation is available (using OpenAPI and Swagger)

if __name__ == "__main__":
    # Uvicorn direct execution will be used for debugging purposes
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
