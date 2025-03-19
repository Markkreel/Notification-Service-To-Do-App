from app.services.task_fetcher import fetch_tasks, filter_task
from app.models.task import TaskStatus


def test_fetch_task():
    tasks = fetch_tasks()
    assert len(tasks) > 0


def test_filter_task():
    tasks = fetch_tasks()
    due_tasks = filter_task(tasks)
    assert all(
        task.status in [TaskStatus.OVERDUE, TaskStatus.DUE_SOON] for task in due_tasks
    )
