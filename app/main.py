from fastapi import FastAPI
from app.services.task_fetcher import fetch_tasks, filter_task
from app.services.notification_service import create_notification
from app.models.notification import Notification

app = FastAPI()


@app.get("/notifications", response_model=list[Notification])
def get_notification():
    tasks = fetch_tasks()
    due_tasks = filter_task(tasks)
    notifications = [create_notification(task) for task in due_tasks]

    return notifications
