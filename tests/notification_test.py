from datetime import datetime, timedelta
from app.services.task_fetcher import fetch_tasks, filter_task
from app.models.task import TaskStatus, TaskDB


def test_fetch_task(db):
    # Add test data
    task = TaskDB(
        title="Test Task",
        due_date=datetime.now() + timedelta(days=1),
        user_id=1,
        status=TaskStatus.PENDING,
    )
    db.add(task)
    db.commit()

    tasks = fetch_tasks()
    assert len(tasks) > 0
    assert tasks[0].title == "Test Task"


def test_filter_task(db):
    # Add test data for different statuses
    overdue_task = TaskDB(
        title="Overdue Task",
        due_date=datetime.now() - timedelta(days=1),
        user_id=1,
        status=TaskStatus.OVERDUE,
    )
    due_soon_task = TaskDB(
        title="Due Soon Task",
        due_date=datetime.now() + timedelta(hours=1),
        user_id=1,
        status=TaskStatus.DUE_SOON,
    )
    db.add_all([overdue_task, due_soon_task])
    db.commit()

    tasks = fetch_tasks()
    due_tasks = filter_task(tasks)
    assert len(due_tasks) == 2
    assert all(
        task.status in [TaskStatus.OVERDUE, TaskStatus.DUE_SOON] for task in due_tasks
    )
