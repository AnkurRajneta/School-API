from sqlalchemy.orm import Session
from app.repository.school_repository import school_repository
from app.schemas.school_schema import School_schema

class school_service:
    def __init__(self, db:Session):
        self.repo = school_repository(db)
        self.db = db

    def get_all_school(self):
        return self.repo.get_all_students()
    
    def create_student(self, structure: School_schema):
        return self.repo.create_student(structure)

    def update_student(self,structure:School_schema, school_id:int):
        return self.repo.update(structure, school_id)

    def delete_student(self, school_id:int):
        return self.repo.deleted(school_id)