from datetime import datetime, timedelta
from app.models.task import Task, TaskStatus, TaskDB
from app.database import get_db


def fetch_tasks() -> list[Task]:
    db = next(get_db())
    tasks = db.query(TaskDB).all()
    return [Task.from_orm(task) for task in tasks]


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
