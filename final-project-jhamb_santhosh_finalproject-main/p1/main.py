# 1) Design a Web Server running a Web API service that accepts data from distributed sources (e.g. mobile phones, computers, sensors) into a persistent datastore

# Load necessary packages
from fastapi import FastAPI
from databases import Database

# Set up FastAPI 
app = FastAPI(root_path="/myapp")

# GET / that returns "Hello World!"
@app.get("/")
async def root():
    return {"message": "Hello World!"}

# Specify the database to be used
database = Database("sqlite:///housing.db")

@app.on_event("startup")
async def open_database():
         await database.connect()

@app.on_event("shutdown")
async def close_database():
     await database.disconnect()

# GET /readings that returns all readings in the database
@app.get("/readings")
async def read_readings():
    return await database.fetch_all("SELECT * FROM train")

# GET all readings for a specified Street type
@app.get("/readings/street/{Street}")
async def read_reading(Street: str):
    return await database.fetch_all("SELECT * FROM train WHERE Street = :Street",
    {"Street":Street})     

# GET all readings for a specific year in which the house was built
@app.get("/readings/yearbuilt/{YearBuilt}")
async def read_reading(YearBuilt: int):
    return await database.fetch_all("SELECT * FROM train WHERE YearBuilt = :YearBuilt",
    {"YearBuilt":YearBuilt})     

# GET average sale price for a specific street type
@app.get("/readings/street/{Street}/saleprice/avg")
async def read_reading(Street: str):
    return await database.fetch_all("SELECT AVG(SalePrice) FROM train WHERE Street = :Street",
    {"Street":Street})

# GET minimum sale price for a specific street type
@app.get("/readings/street/{Street}/saleprice/min")
async def read_reading(Street: str):
    return await database.fetch_all("SELECT MIN(SalePrice) FROM train WHERE Street = :Street",
    {"Street":Street})

# GET maximum sale price for a specific street type
@app.get("/readings/street/{Street}/saleprice/max")
async def read_reading(Street: str):
    return await database.fetch_all("SELECT MAX(SalePrice) FROM train WHERE Street = :Street",
    {"Street":Street})

