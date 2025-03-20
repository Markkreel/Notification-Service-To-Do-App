from datetime import datetime
from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLAlchemyEnum
from pydantic import BaseModel
from app.database import Base


class TaskStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    DUE_SOON = "Due Soon"
    OVERDUE = "Overdue"
    CANCELLED = "Cancelled"


class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    due_date = Column(DateTime)
    user_id = Column(Integer, index=True)
    status = Column(SQLAlchemyEnum(TaskStatus), default=TaskStatus.PENDING)


class Task(BaseModel):
    id: int
    title: str
    due_date: datetime
    user_id: int
    status: TaskStatus = TaskStatus.PENDING

    class Config:
        from_attributes = True
