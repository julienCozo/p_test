"""
Models for peak
"""
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """ """

    pass


class Peak(Base):
    """ """

    __tablename__ = "peak"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    lat = Column(Float)
    lon = Column(Float)
    altitude = Column(Float)
