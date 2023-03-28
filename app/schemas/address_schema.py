from typing import Optional
from pydantic import BaseModel, validator
from fastapi import HTTPException
from app.api.address import utils


# Address schema for creating a new address
class AddressCreate(BaseModel):
    name: str
    street: str
    city: str
    state: str
    country: str
    zip: str
    latitude: float
    longitude: float
    
    _validate_location = validator('latitude', 'longitude', allow_reuse=True)(utils.validate_location)
    _name_must_not_be_empty = validator('name', allow_reuse=True)(utils.name_must_not_be_empty)
    _street_must_not_be_empty = validator('street', allow_reuse=True)(utils.street_must_not_be_empty)
    _city_must_not_be_empty = validator('city', allow_reuse=True)(utils.city_must_not_be_empty)
    _state_must_not_be_empty = validator('state', allow_reuse=True)(utils.state_must_not_be_empty)
    _country_must_not_be_empty = validator('country', allow_reuse=True)(utils.country_must_not_be_empty)
    _zip_must_not_be_empty = validator('zip', allow_reuse=True)(utils.zip_must_not_be_empty)


    class Config:
        orm_mode = True


# Address schema for updating an existing address
class AddressUpdate(BaseModel):
    name: str
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    zip: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]

    _validate_location = validator('latitude', 'longitude', allow_reuse=True)(utils.validate_location)
    _name_must_not_be_empty = validator('name', allow_reuse=True)(utils.name_must_not_be_empty)
    _street_must_not_be_empty = validator('street', allow_reuse=True)(utils.street_must_not_be_empty)
    _city_must_not_be_empty = validator('city', allow_reuse=True)(utils.city_must_not_be_empty)
    _state_must_not_be_empty = validator('state', allow_reuse=True)(utils.state_must_not_be_empty)
    _country_must_not_be_empty = validator('country', allow_reuse=True)(utils.country_must_not_be_empty)
    _zip_must_not_be_empty = validator('zip', allow_reuse=True)(utils.zip_must_not_be_empty)

    class Config:
        orm_mode = True


# Address schema for reading an existing address
class Address(BaseModel):
    id: int
    name: str
    street: str
    city: str
    state: str
    country: str
    zip: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


# Address schema for returning a list of addresses within a given distance and location coordinates
class AddressesWithinDistance(BaseModel):
    id: int
    name: str
    street: str
    city: str
    state: str
    country: str
    zip: str
    latitude: float
    longitude: float
    distance_km: float

    class Config:
        orm_mode = True
