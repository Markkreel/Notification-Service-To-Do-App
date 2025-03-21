# Notification Service for To-Do App

A FastAPI-based notification service that monitors tasks in a To-Do application and generates notifications for tasks that are due soon or overdue.

## Features

- Monitors task due dates and statuses
- Automatically identifies tasks that are:
  - Due within 7 days (marked as DUE_SOON)
  - Past their due date (marked as OVERDUE)
- Generates notifications for tasks requiring attention
- RESTful API endpoint for retrieving notifications

## Project Structure

```
.
├── app/
│   ├── models/
│   │   ├── notification.py
│   │   └── task.py
│   ├── services/
│   │   ├── notification_service.py
│   │   └── task_fetcher.py
│   └── main.py
├── tests/
│   └── notification_test.py
├── Dockerfile
└── requirements.txt
```

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Service

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```
2. The service will be available at `http://127.0.0.1:8000`

## API Endpoints

### GET /notifications

Returns a list of notifications for tasks that are either due soon or overdue.

Response format:

```json
[
  {
    "task_id": 1,
    "title": "Task Title",
    "message": "Task is due soon",
    "status": "DUE_SOON"
  }
]
```

## Testing

Run the test suite using pytest:

```bash
pytest tests/
```

## Docker Support

The service can be containerized using the provided Dockerfile.

**Last Updated:** 21-03-2025 ⸺ **Last Reviewed:** 21-03-2025
