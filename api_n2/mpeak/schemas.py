"""
Schemas for peak
"""
from pydantic import BaseModel


class PeakBase(BaseModel):
    name: str
    lat: float
    lon: float
    altitude: float

    class Config:
        orm_mode = True


class PeakSchema(PeakBase):
    """ """

    id: int


class PeakCreateSchema(PeakBase):
    pass
