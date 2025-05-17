from fastapi import FastAPI
from app.api.v1.routes import router as product_router
from app.core.config import engine, Base
from app.models import product  # Asegura que SQLAlchemy vea el modelo


Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Ecommerce", version="1.0.0")
app.include_router(product_router, prefix="/api/v1")