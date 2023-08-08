"""
Application init
"""
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List, AnyStr
from fastapi import FastAPI, HTTPException
from .database import SessionLocal, engine
import mpeak.models as models
from mpeak.controller import (
    read_peaks,
    read_peak,
    read_peak_by_name,
    create_peak,
    update_peak,
    delete_peak,
    boucing_peaks,
)
from mpeak.schemas import PeakSchema, PeakCreateSchema

app = FastAPI(title="Peak Api")
models.Base.metadata.create_all(bind=engine)


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


@app.get("/", response_model=AnyStr)
def root_call():
    return "Welcome on moutain peak API"


@app.get("/peaks", response_model=List[PeakSchema])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return read_peaks(db, skip=skip, limit=limit)


@app.get("/boucing_peaks", response_model=List[PeakSchema])
def peak_in_a_box(
    min_lat: float,
    max_lat: float,
    min_lon: float,
    max_lon: float,
    db: Session = Depends(get_db),
):
    return boucing_peaks(
        db, min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon
    )


@app.get("/peak/{peak_id}", response_model=PeakSchema)
def get(peak_id: int, db: Session = Depends(get_db)):
    peak = read_peak(db, peak_id=peak_id)
    if peak is None:
        raise HTTPException(status_code=404, detail="Peak not found")
    return peak


@app.post("/peak", response_model=PeakSchema)
def create(new_peak: PeakCreateSchema, db: Session = Depends(get_db)):
    peak = read_peak_by_name(db, new_peak.name)
    if peak:
        raise HTTPException(status_code=400, detail="Peak already exist")

    return create_peak(db, peak=new_peak)


@app.put("/peak/{peak_id}", response_model=PeakSchema)
def update(peak_id: int, new_peak: PeakSchema, db: Session = Depends(get_db)):
    peak = read_peak(db, peak_id=peak_id)
    if peak is None:
        raise HTTPException(status_code=404, detail="Peak not found")

    return update_peak(db, peak_id=peak_id, peak=new_peak)


@app.delete("/peak/{peak_id}")
def delete(peak_id: int, db: Session = Depends(get_db)):
    peak = read_peak(db, peak_id=peak_id)
    if peak is None:
        raise HTTPException(status_code=404, detail="Peak not found")
    return delete_peak(db, peak_id=peak_id)
