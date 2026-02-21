from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base


DB_URL = 'postgresql://postgres:admin@localhost/Booking'
engine = create_engine(DB_URL)


SessionLocal = sessionmaker

Base = declarative_base()