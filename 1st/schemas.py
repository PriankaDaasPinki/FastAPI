from pydantic import BaseModel
from typing import List, Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status_id: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


class StatusBase(BaseModel):
    name: str

class StatusCreate(StatusBase):
    pass

class Status(StatusBase):
    id: int
    tasks: List[Task] = []

    class Config:
        orm_mode = True
