import pytest
from datetime import datetime
from app.models.task import Task, TaskStatus
from app.services.notification_service import create_notification


@pytest.fixture
def sample_task():
    return Task(
        id=1,
        title="Test Task",
        due_date=datetime.now(),
        user_id=123,
        status=TaskStatus.PENDING,
    )


def test_create_notification_pending(sample_task):
    notification = create_notification(sample_task)
    assert notification is not None
    assert notification.user_id == sample_task.user_id
    assert notification.message == f"Your task '{sample_task.title}' is pending"
    assert notification.channel == "email"


def test_create_notification_overdue(sample_task):
    sample_task.status = TaskStatus.OVERDUE
    notification = create_notification(sample_task)
    assert notification is not None
    assert notification.message == f"Your task '{sample_task.title}' is overdue"


def test_create_notification_cancelled(sample_task):
    sample_task.status = TaskStatus.CANCELLED
    notification = create_notification(sample_task)
    assert notification is not None
    assert notification.message == f"Your task '{sample_task.title}' has been cancelled"


def test_create_notification_due_soon(sample_task):
    sample_task.status = TaskStatus.DUE_SOON
    notification = create_notification(sample_task)
    assert notification is not None
    assert notification.message == f"Your task '{sample_task.title}' is due soon"


def test_create_notification_completed(sample_task):
    sample_task.status = TaskStatus.COMPLETED
    notification = create_notification(sample_task)
    assert notification is None


def test_create_notification_custom_channel(sample_task):
    notification = create_notification(sample_task, channel="sms")
    assert notification is not None
    assert notification.channel == "sms"
