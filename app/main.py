"""
FastAPI application for notification service.
This module provides endpoints to fetch and filter tasks,
and create notifications based on due tasks.
"""

from fastapi import FastAPI
from app.services.task_fetcher import fetch_tasks, filter_task
from app.services.notification_service import create_notification
from app.models.notification import Notification

app = FastAPI()


@app.get("/notifications", response_model=list[Notification])
def get_notification() -> list[Notification]:
    """
    Fetch and filter tasks to create notifications.

    Returns:
        list[Notification]: A list of notifications generated from due tasks.
    """
    tasks = fetch_tasks()
    due_tasks = filter_task(tasks)
    notifications = [create_notification(task) for task in due_tasks]

    return notifications
