from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="app/templates")  

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.school_schema import School_schema, Section
from app.service.school_services import school_service
from app.config.database import get_db
from typing import List
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/students/1.1", response_model=List[Section])
def get_all_students(db: Session = Depends(get_db)):
    service = school_service(db)
    return service.get_all_school()


@router.post("/students/1.2", response_model=Section)
def create_student(structure: School_schema, db: Session = Depends(get_db)):
    service = school_service(db)
    return service.create_student(structure)


@router.put("/students/1.3/{school_id}", response_model=Section)
def update_student(school_id: int, structure: School_schema, db: Session = Depends(get_db)):
    service = school_service(db)
    result = service.update_student(structure, school_id)
    if not result:
        raise HTTPException(status_code=404, detail="Student not found")
    return result


@router.delete("/students/1.4/{school_id}")
def delete_student(school_id: int, db: Session = Depends(get_db)):
    service = school_service(db)
    result = service.delete_student(school_id)
    if not result:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"deleted": True}


@router.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse("routes.html", {"request": request})

