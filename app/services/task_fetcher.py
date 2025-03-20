from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.task import Task, TaskStatus, TaskDB
from app.database import get_db


def fetch_tasks() -> list[Task]:
    db = next(get_db())
    tasks = db.query(TaskDB).all()
    return [Task.from_orm(task) for task in tasks]


def filter_task(tasks: list[Task]) -> list[Task]:
    return [task for task in tasks if task.status in [TaskStatus.OVERDUE, TaskStatus.DUE_SOON]]
        Task(
            id=1,
            title="Complete Project Proposal",
            due_date=datetime(2024, 2, 15, 17, 0),
            user_id=101,
            status=TaskStatus.OVERDUE,
        ),
        Task(
            id=2,
            title="Review Code Changes",
            due_date=datetime(2025, 3, 21, 12, 0),
            user_id=102,
            status=TaskStatus.DUE_SOON,
        ),
        Task(
            id=3,
            title="Deploy Application Update",
            due_date=datetime(2024, 2, 8, 9, 0),
            user_id=103,
            status=TaskStatus.COMPLETED,
        ),
    ]
    return tasks


def filter_task(tasks: list[Task]) -> list[Task]:
    now = datetime.now()
    due_tasks = []
    for task in tasks:
        if task.status not in [
            TaskStatus.COMPLETED,
            TaskStatus.CANCELLED,
            TaskStatus.IN_PROGRESS,
        ]:
            if task.due_date <= now:
                task.status = TaskStatus.OVERDUE
                due_tasks.append(task)
            elif task.due_date - now <= timedelta(days=7):
                task.status = TaskStatus.DUE_SOON
                due_tasks.append(task)
    return due_tasks
