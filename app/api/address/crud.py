from sqlalchemy.orm import Session
from geopy.distance import geodesic
from typing import List
from app.schemas import address_schema
from app.models import address_models


#To create an address
def create_address(db: Session, address: address_schema.AddressCreate):
    db_address = address_models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


#To get address of a specific Id
def get_address(db: Session, address_id: int):
    return db.query(address_models.Address).filter(address_models.Address.id == address_id).first()


#To get all addressess
def get_all_addresses(db: Session)-> List[address_models.Address]:
    return db.query(address_models.Address).all()


#To update values in a specific address
def update_address(db: Session, address_id: int, address: address_schema.AddressUpdate):
    db_address = db.query(address_models.Address).filter(address_models.Address.id == address_id).first()
    if db_address:
        for key, value in address.dict(exclude_unset=True).items():
            setattr(db_address, key, value)
        db.commit()
        db.refresh(db_address)
    return db_address



#To delete an address
def delete_address(db: Session, address_id: int):
    db_address = db.query(address_models.Address).filter(address_models.Address.id == address_id).first()
    if db_address:
        db.delete(db_address)
        db.commit()
    return db_address


#To get addresses that are within in given distance, lattitude and longitude.
def get_addresses_within_distance(db: Session, latitude: float, longitude: float, distance: float):
    addresses = db.query(address_models.Address).all()
    result = []
    for address in addresses:
        if address.latitude and address.longitude:
            dist = geodesic((latitude, longitude), (address.latitude, address.longitude)).km
            if dist <= distance:
                result.append(address)
    return result
