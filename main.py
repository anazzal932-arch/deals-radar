from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models
from pydantic import BaseModel
from rapidfuzz import fuzz

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Radar Al Offers API")


class OfferCreate(BaseModel):
    store_name: str
    city: str
    source: str
    text: str
    image_url: str
    discount: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def clean_text(text: str):
    return " ".join(text.lower().strip().split())


def is_duplicate(existing_text: str, new_text: str, threshold: int = 90):
    return fuzz.ratio(clean_text(existing_text), clean_text(new_text)) >= threshold


@app.post("/offers/check_duplicate")
def check_duplicate(offer: OfferCreate, db: Session = Depends(get_db)):
    offers = db.query(models.Offer).filter(
        models.Offer.store_name == offer.store_name
    ).all()

    for e in offers:
        if is_duplicate(e.text, offer.text):
            return {"duplicate": True}

    return {"duplicate": False}


@app.post("/offers/")
def create_offer(offer: OfferCreate, db: Session = Depends(get_db)):
    offers = db.query(models.Offer).filter(
        models.Offer.store_name == offer.store_name
    ).all()

    for e in offers:
        if is_duplicate(e.text, offer.text):
            raise HTTPException(status_code=400, detail="Duplicate offer")

    db_offer = models.Offer(**offer.dict())
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)

    return db_offer


@app.get("/offers/")
def read_offers(limit: int = 50, db: Session = Depends(get_db)):
    return db.query(models.Offer).order_by(models.Offer.created_at.desc()).limit(limit).all()
