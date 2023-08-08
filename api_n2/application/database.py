from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URL = "mongodb://mongo:27017"
mongo_client = AsyncIOMotorClient(MONGODB_URL)
mongo_db = mongo_client.peak_db
peak_collection = mongo_db.peak_info


pg_url = "postgresql://meteo:france@db/mpeak"
engine = create_engine(pg_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
