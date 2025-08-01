from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
from sqlalchemy.orm import declarative_base
from app.config.config import Database  # Assuming this contains your DB URL

# ✅ Create async engine
engine = create_async_engine(Database, echo=True)

# ✅ Create async sessionmaker
async_session_maker = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession  # Optional, but good for clarity
)

# ✅ Declare Base
Base = declarative_base()

# ✅ Dependency for FastAPI routes
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()
