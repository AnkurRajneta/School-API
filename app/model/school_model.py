from sqlalchemy import Column, String, Integer, Boolean
from app.config.database import Base

class School(Base):
    __tablename__ = "school"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,nullable = True)
    standard = Column(String, nullable=True)

    