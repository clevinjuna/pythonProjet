from fastapi import Request, FastAPI
from json import JSONDecodeError
from list import List
from car import Car
from boat import Boat
from plane import Plane
from bike import Bike

from pydantic import BaseModel
from fastapi.responses import ORJSONResponse

# import JSONDecodeError

import writer
import subprocess
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()
class Item(BaseModel):
    name: str
    brand: str
    speedMax: int
    color: str
    year: int
    typeWheels: str


app = FastAPI()

Vehicles = []
car1 = Car("Rc 27", "Mercedes", 250, "Blue", 2009, "Hiver")
Vehicles.append(car1)
car2 = Car("Sd 55", "BMW", 120, "Red", 1955, "Autre")
Vehicles.append(car2)
boat1 = Boat("Sheisou", "BATO", 4, "Green", 1478, "Strong")
Vehicles.append(boat1)
bike = Bike("AMG 74", "Suzuki", 270, "Black", 2021, "Big")
Vehicles.append(bike)

@app.post("/items/")
async def create_item(item: Item):
    return item


@app.get("/")
def root():
    return {"message": "Api opérationnelle !"}


@app.get("/all")
def root():
    return {"message":  Vehicles}

@app.get("/one")
def root():
    return {"message":  Vehicles[0]}


@app.get('/start')
async def getInfo(request: Request):
    try:
        data = await request.json()
        for i in data:
            print(i)
    except JSONDecodeError:
        return JSONResponse({'error': 'il n y a pas de body'})
    except:
        return JSONResponse({'error': 'interne depuis le serveur'})
    print(f'{data}')
    return JSONResponse({'test': "test"})


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse({"message": "endpoint not found" })

