from pydantic import BaseModel

class School_schema(BaseModel):
    name:str
    standard:str

class Section(School_schema):
    id:int

    class Config:
        from_attributes = True

