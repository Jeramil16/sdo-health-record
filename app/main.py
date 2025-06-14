
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from .models import Base, engine, SessionLocal, PersonnelRecord
from .utils import generate_qr_code
from uuid import uuid4
from datetime import date
import os

app = FastAPI()

# Mount static and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Create DB tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = next(get_db())):
    records = db.query(PersonnelRecord).all()
    return templates.TemplateResponse("index.html", {"request": request, "records": records})

@app.get("/view/{token}", response_class=HTMLResponse)
def view_by_token(token: str, request: Request, db: Session = next(get_db())):
    record = db.query(PersonnelRecord).filter(PersonnelRecord.qr_token == token).first()
    if not record:
        return HTMLResponse("Invalid or expired token", status_code=404)
    return templates.TemplateResponse("view.html", {"request": request, "record": record})
