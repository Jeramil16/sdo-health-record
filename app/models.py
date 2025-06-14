
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./sdo_health.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class PersonnelRecord(Base):
    __tablename__ = "personnel_records"

    id = Column(Integer, primary_key=True, index=True)
    employee_number = Column(String, unique=True, index=True)
    name = Column(String)
    age = Column(Integer)
    unit_office = Column(String)
    gender = Column(String)
    past_medical_history = Column(Text)
    current_medical_condition = Column(Text)
    maintenance_medicines = Column(Text)
    vaccinations = Column(Text)
    heart_rate = Column(Integer)
    respiratory_rate = Column(Integer)
    blood_pressure = Column(String)
    temperature = Column(Float)
    height = Column(Float)
    weight = Column(Float)
    bmi = Column(Float)
    vital_signs_taken_by = Column(String)
    record_date = Column(Date)
    qr_token = Column(String, unique=True)
