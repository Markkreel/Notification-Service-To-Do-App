"""This module contains test fixtures and configuration for the notification service tests.
Provides common setup and teardown functionality used across test cases.
"""

import os
import sys
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models.task import TaskDB

# Add the project root directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Use in-memory SQLite for tests
TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

test_engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(scope="function")
def db():
    # Create all tables before each test
    Base.metadata.create_all(bind=test_engine)

    # Create a new session for the test
    db = TestSessionLocal()
    try:
        yield db
    finally:
        # Close the session
        db.close()
        # Clear all tables after each test
        Base.metadata.drop_all(bind=test_engine)
        Base.metadata.create_all(bind=test_engine)
