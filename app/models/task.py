from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class TaskStatus(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    DUE_SOON = "Due Soon"
    OVERDUE = "Overdue"
    CANCELLED = "Cancelled"


class Task(BaseModel):
    id: int
    title: str
    due_date: datetime
    user_id: int
    status: TaskStatus = TaskStatus.PENDING
