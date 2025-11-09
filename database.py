from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)