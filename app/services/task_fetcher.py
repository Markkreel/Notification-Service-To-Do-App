from datetime import datetime
from app.models.task import Task, TaskStatus


def fetch_tasks() -> list[Task]:
    tasks = [
        Task(
            id=1,
            title="Complete Project Proposal",
            due_date=datetime(2024, 2, 15, 17, 0),
            user_id=101,
            status=TaskStatus.PENDING,
        ),
        Task(
            id=2,
            title="Review Code Changes",
            due_date=datetime(2024, 2, 10, 12, 0),
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
