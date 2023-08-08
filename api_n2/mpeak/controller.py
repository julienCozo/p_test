"""
Controller for peak
"""
from sqlalchemy.orm import Session
from mpeak.models import Peak
from application.database import SessionLocal

from fastapi import Depends, HTTPException
from mpeak.schemas import PeakSchema, PeakCreateSchema


def read_peaks(db: Session, skip: int = 0, limit: int = 100):
    peaks = db.query(Peak).offset(skip).limit(limit).all()
    return peaks


def boucing_peaks(
    db: Session, min_lat: float, max_lat: float, min_lon: float, max_lon: float
):
    peaks = (
        db.query(Peak)
        .filter(
            Peak.lat > min_lat,
            Peak.lat < max_lat,
            Peak.lon > min_lon,
            Peak.lon < max_lon,
        )
        .all()
    )
    return peaks


def read_peak(db: Session, peak_id: int):
    peak = db.query(Peak).filter(Peak.id == peak_id).first()
    return peak


def read_peak_by_name(db: Session, peak_name: str):
    peak = db.query(Peak).filter(Peak.name == peak_name).first()
    return peak


def create_peak(db: Session, peak: PeakCreateSchema):
    db_peak = Peak(name=peak.name, altitude=peak.altitude, lat=peak.lat, lon=peak.lon)
    db.add(db_peak)
    db.commit()
    db.refresh(db_peak)
    return db_peak


def update_peak(db: Session, peak_id: int, peak: PeakSchema):
    db_peak = db.query(Peak).filter(Peak.id == peak_id).first()
    if db_peak:
        db_peak.name = peak.name
        db_peak.altitude = peak.altitude
        db_peak.lat = peak.lat
        db_peak.lon = peak.lon
        db.commit()
        db.refresh(db_peak)
    return db_peak


def delete_peak(db: Session, peak_id: int):
    db_peak = db.query(Peak).filter(Peak.id == peak_id).first()
    if db_peak:
        db.delete(db_peak)
        db.commit()
        return {"message": "Peak deleted"}
    else:
        raise HTTPException(status_code=404, detail="Peak not found")
