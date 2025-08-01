from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.school_schema import School_schema
from app.model.school_model import School

class SchoolRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    # ✅ Get all students
    async def get_all_students(self):
        stmt = select(School)
        result = await self.db.execute(stmt)
        return result.scalars().all()  # ❌ Do NOT await .all() — it's not a coroutine

    # ✅ Create student
    async def create_student(self, structure: School_schema):
        new_student = School(name=structure.name, standard=structure.standard)
        self.db.add(new_student)
        await self.db.commit()
        await self.db.refresh(new_student)
        return new_student  # ❌ Do NOT await a normal object

    # ✅ Update student
    async def update(self, structure: School_schema, school_id: int):
        stmt = select(School).where(School.id == school_id)
        result = await self.db.execute(stmt)
        updated_file = result.scalars().first()

        if not updated_file:
            return None

        updated_file.name = structure.name
        updated_file.standard = structure.standard
        await self.db.commit()
        await self.db.refresh(updated_file)
        return updated_file

    # ✅ Delete student
    async def deleted(self, school_id: int):
        stmt = select(School).where(School.id == school_id)
        result = await self.db.execute(stmt)
        deleted_file = result.scalars().first()  # ❌ you missed () — should be .first()

        if not deleted_file:
            return False

        await self.db.delete(deleted_file)
        await self.db.commit()
        return True
