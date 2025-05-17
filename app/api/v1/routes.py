from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductOut
from app.api.deps import get_db


router = APIRouter()
@router.get("/products", response_model=list[ProductOut])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
    
@router.get("/ping")
def ping():
    return {"message":"pong"}

