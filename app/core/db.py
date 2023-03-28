from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models.address_models import Base



SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine, checkfirst=True)
