from app.models.task import TaskStatus
from app.models.notification import Notification


def create_notification(task, channel="email") -> Notification:
    if task.status == TaskStatus.OVERDUE:
        message = f"Your task '{task.title}' is overdue."
    elif task.status == TaskStatus.CANCELLED:
        message = f"Your task '{task.title}' has been cancelled."
    elif task.status == TaskStatus.DUE_SOON:
        message = f"Your task '{task.title}' is due soon."
    elif task.status == TaskStatus.PENDING:
        message = f"Your task '{task.title}' is pending."
    else:
        return None

    return Notification(user_id=task.user_id, message=message, channel=channel)
