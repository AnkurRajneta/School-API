from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import Session
from app.repository.school_repository import SchoolRepository
from app.schemas.school_schema import School_schema

class school_service:
    def __init__(self, db:AsyncSession):
        self.repo = SchoolRepository(db)
        self.db = db

    async def get_all_school(self):
        return await self.repo.get_all_students()
    
    async def create_student(self, structure: School_schema):
        return await self.repo.create_student(structure)

    async def update_student(self,structure:School_schema, school_id:int):
        return await self.repo.update(structure, school_id)

    async def delete_student(self, school_id:int):
        return await self.repo.deleted(school_id)