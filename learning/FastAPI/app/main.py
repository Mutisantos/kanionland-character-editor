# The entrypoint for FastAPI applications
# Usage of uvicorn will allow hosting the python application as a web server
from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi import FastAPI
from .models.character import Character
from .repositories.sqlite_connection import create_all_tables
from .routers.characters_router import router

app = FastAPI(lifespan=create_all_tables)
app.include_router(router)

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
