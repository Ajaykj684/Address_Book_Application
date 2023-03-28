from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import address_schema
from app.api.address import crud
from app.core.db import SessionLocal


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#To get all addresses
@router.get("/get_all_addresses", response_model=List[address_schema.Address])
def read_all_addresses(db: Session = Depends(get_db)):
    try:
        addresses = crud.get_all_addresses(db)
        if addresses is None:
            raise HTTPException(status_code=404, detail="Address not found")
        return addresses
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

#To create new address
@router.post("/create_address", response_model=address_schema.AddressCreate)
def create_address(address: address_schema.AddressCreate, db: Session = Depends(get_db)):
    try:
        db_address = crud.create_address(db, address)
        return db_address
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


#To update an existing address
@router.put("/update_address/{address_id}", response_model=address_schema.Address)
def update_address(address_id: int, address: address_schema.AddressUpdate, db: Session = Depends(get_db)):
    try:
        db_address = crud.update_address(db, address_id, address)
        if db_address is None:
            raise HTTPException(status_code=404, detail="Address not found")
        return db_address
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


#To delete an address
@router.delete("/delete_address/{address_id}", response_model=address_schema.Address)
def delete_address(address_id: int, db: Session = Depends(get_db)):
    db_address = crud.delete_address(db, address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


#To get all addresses within given distance
@router.get("/get_addresses_within_distance", response_model=list[address_schema.Address])
def read_addresses_within_distance(latitude: float, longitude: float, distance: float, db: Session = Depends(get_db)):
    try:
        addresses = crud.get_addresses_within_distance(db, latitude, longitude, distance)
        if addresses is None:
            raise HTTPException(status_code=404, detail="No Address found")
        return addresses
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
 
 
#To get a specific address using Id
@router.get("/get_address/{address_id}", response_model=address_schema.Address)
def read_address(address_id: int, db: Session = Depends(get_db)):
    db_address = crud.get_address(db, address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

