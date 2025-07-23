from sqlalchemy.orm import Session
from app.schemas.school_schema import School_schema
from app.model.school_model import School

class school_repository:
    def __init__(self, db:Session):
        self.db = db
    
    def get_all_students(self):
        return self.db.query(School).all()
    
    def create_student(self,structure:School_schema):
        new_student = School(name = structure.name, standard = structure.standard)
        self.db.add(new_student)
        self.db.commit()
        self.db.refresh(new_student)
        return new_student
    
    def update(self, structure:School_schema, school_id:int):
        updated_file = self.db.query(School).filter(School.id == school_id).first()
        updated_file.name = structure.name
        updated_file.standard = structure.standard
        return updated_file
     
    def deleted(self, school_id:int):
        deleted_file = self.db.query(School).filter(School.id == school_id).first()
        if not deleted_file:
            return False
        
        self.db.delete(deleted_file)
        self.db.commit()
        return True