from datetime import datetime, timedelta
from app.models.task import Task, TaskStatus


def fetch_tasks() -> list[Task]:
    tasks = [
        Task(
            id=1,
            title="Complete Project Proposal",
            due_date=datetime(2026, 2, 15, 17, 0),
            user_id=101,
            status=TaskStatus.PENDING,
        ),
        Task(
            id=2,
            title="Review Code Changes",
            due_date=datetime(2025, 3, 21, 12, 0),
            user_id=102,
            status=TaskStatus.IN_PROGRESS,
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
            TaskStatus.OVERDUE,
            TaskStatus.DUE_SOON,
        ]:
            if task.due_date <= now:
                task.status = TaskStatus.OVERDUE
                due_tasks.append(task)
            elif task.due_date - now <= timedelta(days=7):
                task.status = TaskStatus.DUE_SOON
                due_tasks.append(task)
    return due_tasks
