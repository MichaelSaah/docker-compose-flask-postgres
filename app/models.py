from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
